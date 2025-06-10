from typing import List

from crewai import Task, Agent
from crewai.project import CrewBase, crew, task

@CrewBase
class Tasks:
    tasks_config = 'config/tasks.yaml'
    
    def __init__(self) -> None:
        pass
    
    # ---------------------------------------------------------------------
    # Assessment Tasks
    # ---------------------------------------------------------------------
    def skill_assessment_task(self, agent: Agent) -> Task:
        """
        Korean skill assessment task (analyze test results, self-assessment, learning history)
        """
        return Task(
            config=self.tasks_config['skill_assessment_task'],
            agent=agent,
        )

    # ---------------------------------------------------------------------
    # Goal Analysis Task
    # ---------------------------------------------------------------------
    def goal_analysis_task(self, agent: Agent) -> Task:
        """
        Analyze and structure user goals using SMART criteria
        """
        return Task(
            config=self.tasks_config['goal_analysis_task'],
            agent=agent,
        )

    # ---------------------------------------------------------------------
    # Curriculum Planning Task
    # ---------------------------------------------------------------------
    def curriculum_planning_task(self, agent: Agent) -> Task:
        """
        Design personalized curriculum based on assessment and goals
        """
        return Task(
            config=self.tasks_config['curriculum_planning_task'],
            agent=agent,
        )

    # ---------------------------------------------------------------------
    # Schedule Optimization Task
    # ---------------------------------------------------------------------
    def schedule_optimization_task(self, agent: Agent) -> Task:
        """
        Optimize study schedule with Pomodoro and spaced repetition
        """
        return Task(
            config=self.tasks_config['schedule_optimization_task'],
            agent=agent,
        )

    # ---------------------------------------------------------------------
    # Planning Task (Comprehensive Plan)
    # ---------------------------------------------------------------------
    def planning_task(self, agent: Agent) -> Task:
        """
        Integrate all components into a comprehensive, actionable learning plan
        """
        return Task(
            config=self.tasks_config['planning_task'],
            agent=agent,
        )

    # ---------------------------------------------------------------------
    # XML Structure Task
    # ---------------------------------------------------------------------
    def xml_structure_task(self, agent: Agent) -> Task:
        """
        Convert the learning plan into a well-structured XML format
        """
        return Task(
            config=self.tasks_config['xml_structure_task'],
            agent=agent,
        )