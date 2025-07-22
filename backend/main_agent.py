from agno.agent import Agent, RunResponse
from agno.models.cerebras import Cerebras
from typing import List, Literal
from pydantic import BaseModel, Field
import time
from .functions.metadata_to_pdf import create_dpp_pdf

questions_list=[]


class DPPify:
    def generate_dpp_metadata(self,topic_name: str, total_questions: int, difficulty_level: str, api_key: str, language: str = "English"):
        time.sleep(2)
        class Question(BaseModel):
            text: str

        class DPP(BaseModel):
            topic: str
            language: str
            instructions: str
            questions: List[Question] = Field(f"A list of {total_questions} questions.")

        with open("backend/prompts/dpp_creater_system_prompt.txt","r") as file:
            system_prompt=file.read()

        user_prompt=f"""
Topic name: {topic_name}
Language: {language} 
Total number of questions: {total_questions} 
Difficulty level: {difficulty_level}"""
        
        agent = Agent(
            model=Cerebras(id="qwen-3-235b-a22b",api_key=api_key),
            system_message=system_prompt,
            response_model=DPP,
        )

        response=(agent.run(user_prompt).content)


        for r in response.questions:
            questions_list.append(r.text)

        output={
            "topic_name": response.topic,
            "dpp_laguage":  response.language,
            "instruction": response.instructions,
            "questions": questions_list
        }

        return output


    def run(self,topic_name: str, total_q: int, level: str, api_key: str):
        dpp = self.generate_dpp_metadata(
            topic_name=topic_name,
            total_questions=total_q,
            difficulty_level=level,
            api_key=api_key
        )


        path = create_dpp_pdf(
            topic_name=dpp["topic_name"],
            questions=dpp["questions"],
            instrucions=dpp["instruction"],
            total_q=total_q,
        )

        return path



