from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from tools.tools import geturl

def lookup(name:str)-> str:
    llm=ChatOpenAI(temperature=0,model_name="gpt-3.5-turbo")
    template= "For the given name - {name}, I want you to give me the link to their LinkedIn profile page,"\
              "your answer should only contain a URL"

    agent_tool=[
        Tool(name='Crawl Google 4 linkedin profile page',
             func=geturl,
             description="use for getting linkedin URL")]
    agent=initialize_agent(tools=agent_tool,llm=llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    prompt_template=PromptTemplate(template=template, input_variables=['name'])
    linkedin= agent.run(prompt_template.format_prompt(name=name))
    return linkedin

