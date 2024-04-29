import os
import pandas as pd
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain_openai import ChatOpenAI
from src.mcqgen.templates import Template,Template_2

load_dotenv()
key=os.getenv("OPENAI_API_KEY")


llm=ChatOpenAI(openai_api_key=key,model="gpt-3.5-turbo",temperature=0.9)

mcq_gen_prompt=PromptTemplate(
    input_variables=["text","number","tone","response_json"],
    template=Template
)
mcq_evaluation_prompt=PromptTemplate(
    input_variables=["quiz"],
    template=Template_2
    )

mcq_gen_chain=LLMChain(llm=llm,prompt=mcq_gen_prompt,output_key="quiz",verbose=True)
mcq_eval_chain=LLMChain(llm=llm, prompt=mcq_evaluation_prompt, output_key="review", verbose=True)

gen_eval_chain=SequentialChain(chains=[mcq_gen_chain,mcq_eval_chain], input_variables=["text", "number", "tone", "response_json"],
                                        output_variables=["quiz", "review"], verbose=True,)

