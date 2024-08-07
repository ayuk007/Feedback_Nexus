from langchain_core.prompts import ChatPromptTemplate
from dataclasses import dataclass

@dataclass
class PromptTemplates:
    negative_prompt_template = ChatPromptTemplate.from_messages(
        [
        ("system", """You are an helpful assistant, keep yourself in the designation, don't include anything about firm. 
         Don't include the details of user."""),
        ("human",
         'Generate a response addressing this negative feedback: {feedback}'),
        ]
    )

    positive_prompt_template = ChatPromptTemplate.from_messages(
        [
        ("system", """You are an helpful assistant, keep yourself in the designation, don't include anything about firm. 
         Don't include the details of user."""),
        ("human",
         "Generate a thank you note for positive feedback: {feedback}")
        ]
    )

    neutral_prompt_template = ChatPromptTemplate.from_messages(
        [
        ("system", """You are an helpful assistant, keep yourself in the designation, don't include anything about firm. 
         Don't include the details of user."""),
        ("human",
         "Generate a reuqest for more details for this neutral feedback: {feedback}")
        ]
    )

    escalate_prompt_template = ChatPromptTemplate.from_messages(
        [
        ("system", """You are an helpful assistant, keep yourself in the designation, don't include anything about firm. 
         Don't include the details of user."""),
        ("human",
         "Generate a message to escalate this feedback to a human agent: {feedback}")
        ]
    )

    classification_prompt_template = ChatPromptTemplate.from_messages(
        [
        ("system", "You are an helpful assistant."),
        ("human",
         "Classify the sentiment of this feedback as positive, negative, neutral or escalate: {feedback}.")
        ]
    )
