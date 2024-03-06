#YAJAT
import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from external.linkedin import linkedin
from searchusingagent import lookup as linkedin_lookup_agent


if __name__ == "__main__":
    load_dotenv()
   #linkedin_data = linkedin(linkedin_profile_url="https://www.linkedin.com/in/williamhgates/")
    #print(linkedin_data.json())


    print("Hello LangChain")

    geturl = linkedin_lookup_agent(name="Bill gates")

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template)


    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")


    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    linkeddata=linkedin(linkedin_profile_url=geturl)
    print(chain.run(information=linkeddata))
