from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
import os
from dotenv import load_dotenv
load_dotenv()

# Initialize the Mistral AI LLM with the API key from .env
llm = ChatMistralAI(model="mistral-small-2506", temperature=0)

# 1st Agent : Search Agent
def build_search_agent():
    return create_agent(
        model = llm,
        tools = [web_search]
    )

# 2nd Agent : Reading Agent
def build_reader_agent():
    return create_agent(
        model = llm,
        tools = [scrape_url]
    )

# Writer Chain
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """ Write a detailed research report on the topic below:
     Topic: {topic}
     Research Gathered: {research}
     Structure the report as: 
     - Introduction 
     - Key Findings
     - Conclusion
     - Sources (list the URLs used for research)
     Use the research gathered to support your points.
     Be detailed, factual and professional in tone. Avoid speculation and ensure all claims are backed by the research provided.""")
])
writer_chain = writer_prompt | llm | StrOutputParser()

# Critic Chain
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Your task is to evaluate the quality of the report based on the research provided. Be honest and specific."),
    ("human", """ Review the following research report and evaluate it strictly:
     Report: 
     {report}

     Respond in this exact format:
     
     Score: X/10

     Strengths:
     - ....
     - ....
     - ....

     Areas to improve:
     - ....
     - ....
     - ....
     
     One Line Summary of Feedback: .....

     Evaluate the report based on:
     - Accuracy: Are the claims in the report supported by the research?
     - Depth: Does the report provide a deep analysis of the topic?
     - Clarity: Is the report well-structured and easy to understand?
     - Use of Sources: Are the sources properly cited and relevant?
     Provide specific feedback on what was done well and what could be improved.""")
])
critic_chain = critic_prompt | llm | StrOutputParser()
