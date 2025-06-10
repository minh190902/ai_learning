import os, sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from dotenv import load_dotenv
load_dotenv(".env", override=True)

from kor_learning.crew import AILearningCrew

crew = AILearningCrew()
inputs = {
    "model_provider": "openai",
    "model_id": "gpt-4o-mini",
    "temperature": 0.5,
    "self_assessment": "Beginner",
    "user_goals": "Topik 6",
    "period": "1 year",
    "weekly_study_hours": 10
}

# Run the planning kickoff
goal = crew.planning_kickoff(inputs)
print(goal)
    