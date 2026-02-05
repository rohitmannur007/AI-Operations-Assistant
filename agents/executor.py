from tools.github_tool import GitHubTool
from tools.weather_tool import WeatherTool
from tools.summarize_tool import SummarizeTool
from llm.llm_client import LLMClient

class ExecutorAgent:
    def __init__(self, llm):
        self.llm = llm
        self.github = GitHubTool()
        self.weather = WeatherTool()
        self.summarizer = SummarizeTool()

    def execute(self, plan):
        results = []
        steps = plan.get("steps", [])

        for step in steps:
            tool = step.get("tool")
            action = step.get("action")

            if tool == "github":
                results.append(self.github.run(action))
            elif tool == "weather":
                results.append(self.weather.run(action))
            elif tool == "summarize":
                results.append(self.summarizer.run(action))
            else:
                results.append({"error": f"Unknown tool: {tool}"})

        return results
