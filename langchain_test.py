#YAJAT
import os
from typing import Tuple

from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from external.linkedin import linkedin
from searchusingagent import lookup as linkedin_lookup_agent
from output import parser, Summary
load_dotenv()

def langchainn(name:str)-> Tuple[Summary,str]:

    print("Hello LangChain")

    geturl = linkedin_lookup_agent(name=name)
    linkeddata = linkedin(linkedin_profile_url=geturl)

    summary_template = """
    Given the information {information} about a person I want you to create:
    1. A short summary.
    2. Two interesting facts about them.
    3. Interesting topic about them.
    4. 2 Creative ice breakers to start a conversation with them.
    \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={"format_instructions": parser.get_format_instructions()})

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    result = chain.run(information=linkeddata)
    return parser.parse(result), linkeddata.get("profile_pic_url")


if __name__=="__main__":
    print("Hello LangChain!")
    result=langchainn(name="Elon Musk")
    print(result)
