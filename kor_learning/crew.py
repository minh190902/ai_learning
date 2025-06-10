import os
import asyncio

import re
import time
import ast
import ast
import json
from typing import Iterator, AsyncGenerator, Dict, Any

from crewai import Crew, Process
from crewai.task import TaskOutput

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from .model_provider_manager import provider_config

from .agents import Agents
from .tasks import Tasks

# class AILearningBasicCrew:
#     def __init__(self) -> None:
#         # Init agents and tasks
#         self.agents = Agents()
#         self.tasks = Tasks()
        
#     def planning_kickoff(self, inputs: Dict[str, Any]):
        

class AILearningCrew:
    def __init__(self) -> None:
        # Init agents and tasks
        self.agents = Agents()
        self.tasks = Tasks()

    def planning_kickoff(self, inputs: Dict[str, Any]):
        """
        Kickoff full multi-agent planning process
        """
        # Initialize Agents
        skill_assessment_agent = self.agents.skill_assessment_agent(
            model_provider=inputs["model_provider"],
            model_id=inputs["model_id"],
            temperature=0,
        )
        goal_analysis_agent = self.agents.goal_analysis_agent(
            model_provider=inputs["model_provider"],
            model_id=inputs["model_id"],
            temperature=0,
        )
        curriculum_planning_agent = self.agents.curriculum_planning_agent(
            model_provider=inputs["model_provider"],
            model_id=inputs["model_id"],
            temperature=0,
        )
        schedule_optimization_agent = self.agents.schedule_optimization_agent(
            model_provider=inputs["model_provider"],
            model_id=inputs["model_id"],
            temperature=0,
        )
        planning_agent = self.agents.planning_agent(
            model_provider=inputs["model_provider"],
            model_id=inputs["model_id"],
            temperature=0,
        )
        xml_structure_agent = self.agents.xml_structure_agent(
            model_provider=inputs["model_provider"],
            model_id=inputs["model_id"],
            temperature=0,
        )

        # Initialize Tasks
        skill_assessment_task = self.tasks.skill_assessment_task(skill_assessment_agent)
        goal_analysis_task = self.tasks.goal_analysis_task(goal_analysis_agent)
        curriculum_planning_task = self.tasks.curriculum_planning_task(curriculum_planning_agent)
        schedule_optimization_task = self.tasks.schedule_optimization_task(schedule_optimization_agent)
        planning_task = self.tasks.planning_task(planning_agent)
        xml_structure_task = self.tasks.xml_structure_task(xml_structure_agent)

        assessment_crew = Crew(
            name="Goal Analysis Crew",
            agents=[goal_analysis_agent],
            tasks=[goal_analysis_task],
            verbose=True,
        )
        
        planning_crew = Crew(
            name="Curriculum and Schedule Planning Crew",
            agents=[
                curriculum_planning_agent, 
                schedule_optimization_agent],
            tasks=[
                curriculum_planning_task, 
                schedule_optimization_task]
        )
        exec_crew = Crew(
            name="Korean AI Learning Crew",
            agents=[
                planning_agent,
                xml_structure_agent,
            ],
            tasks=[
                planning_task,
                xml_structure_task,
            ],
            verbose=True,
        )

        assessment_result = assessment_crew.kickoff(inputs=inputs)
        if not assessment_result:
            raise Exception("Assessment crew failed to complete tasks")
        
        # planning_inputs = {
        #     "weekly_study_hours": inputs["weekly_study_hours"],
        #     "assessment_results": skill_assessment_task.output.raw,
        #     "goal_hierarchy": goal_analysis_task.output.raw,
        # }
        # planning_result = planning_crew.kickoff(inputs=planning_inputs)
        # if not planning_result:
        #     raise Exception("Planning crew failed to complete tasks")
        
        # exec_inputs = {
        #     "curriculum_plan": curriculum_planning_task.output.raw,
        #     "schedule_plan": schedule_optimization_task.output.raw,
        #     "xml_structure": xml_structure_task.output.raw,
        # }
        
        return goal_analysis_task.output.raw