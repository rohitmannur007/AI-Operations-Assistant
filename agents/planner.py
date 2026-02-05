class PlannerAgent:
    def __init__(self, llm):
        self.llm = llm

    def plan(self, task: str):
        # Dummy plan for now
        return {
            "steps": [
                {"tool": "github", "action": task}
            ]
        }
