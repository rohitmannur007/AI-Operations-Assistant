from tools.github_tool import GitHubTool
from tools.weather_tool import WeatherTool
from llm.llm_client import LLMClient

class ExecutorAgent:
    def __init__(self, llm: LLMClient):
        self.llm = llm
        self.tools = {
            "github_search": GitHubTool(),
            "weather": WeatherTool()
        }

    def execute(self, plan):
        results = []
        for step in plan.steps:
            if step.tool == "none":
                result = {"step": step.description, "result": "Reasoned step (no tool)"}
            else:
                tool = self.tools.get(step.tool)
                if tool:
                    try:
                        result = {"step": step.description, "result": tool.run(step.description)}
                    except Exception as e:
                        result = {"step": step.description, "result": f"Error: {str(e)}"}
                else:
                    result = {"step": step.description, "result": "Unknown tool"}
            results.append(result)
        return results