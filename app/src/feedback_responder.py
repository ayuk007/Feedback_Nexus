from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableBranch
from langchain_core.output_parsers import StrOutputParser
from src.prompt_templates import PromptTemplates

load_dotenv()

class FeedbackResponder:
    def __init__(self) -> None:
        self.model = ChatGroq(model = "mixtral-8x7b-32768", temperature = 0)
        self.classification_prompt = PromptTemplates.classification_prompt_template
        self.positive_prompt = PromptTemplates.positive_prompt_template
        self.neutral_prompt = PromptTemplates.neutral_prompt_template
        self.negative_prompt = PromptTemplates.negative_prompt_template
        self.escalated_prompt = PromptTemplates.escalate_prompt_template
        self.create_branch()

    def generate_response(self, feedback: str, model: str, temperature: float):
        # self.model.model = model
        self.model.temperature = temperature
        chain = self.classification_prompt | self.model | StrOutputParser() | self.branch
        feedback_response = chain.invoke({"feedback": feedback})
        return feedback_response
    
    def create_branch(self) -> None:
        self.branch = RunnableBranch(
            (
                lambda x: "positive" in x,
                self.positive_prompt | self.model | StrOutputParser()
            ),
            (
                lambda x: "negative" in x,
                self.negative_prompt | self.model | StrOutputParser()
            ),
            (
                lambda x: "neutral" in x,
                self.neutral_prompt | self.model | StrOutputParser()
            ),
            self.escalated_prompt | self.model | StrOutputParser()
        )