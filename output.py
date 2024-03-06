from typing import List

from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field


class Summary(BaseModel):
    summary: str = Field(description="summary")
    facts: List[str] = Field(description="interesting facts about them")
    topics_of_interest: List[str] = Field(description="topic that might interest the person")
    ice_breakers: List[str] = Field(description="ice breaker list")
    def to_dict(self):
        return {"summary": self.summary,
                "facts": self.facts,
                "topics_of_interest":self.topics_of_interest,
                "ice_breakers":self.ice_breakers}


parser:PydanticOutputParser = PydanticOutputParser(pydantic_object=Summary)