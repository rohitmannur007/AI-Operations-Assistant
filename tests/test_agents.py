import pytest
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.verifier import VerifierAgent
import requests_mock
from llm.llm_client import LLMClient

class MockLLMClient(LLMClient):
    def chat_json(self, prompt, model=None):
        if "Planner" in prompt:
            return {"steps": [{"description": "Search python", "tool": "github_search"}]}
        elif "Verifier" in prompt:
            return {"final_answer": "Test output", "issues": []}

@pytest.fixture
def mock_apis():
    with requests_mock.Mocker() as m:
        m.get("https://api.github.com/search/repositories?q=python&sort=stars&order=desc", json={"items": [{"full_name": "test/repo", "stargazers_count": 100, "description": "test"}]})
        m.get("http://api.openweathermap.org/data/2.5/weather?q=Mumbai&appid=key&units=metric", json={"name": "Mumbai", "main": {"temp": 25}, "weather": [{"description": "clear"}]})
        yield m

@pytest.fixture
def mock_llm():
    return MockLLMClient()

def test_full_flow(mock_apis, mock_llm):
    planner = PlannerAgent(mock_llm)
    plan = planner.plan("Test")
    executor = ExecutorAgent(mock_llm)
    results = executor.execute(plan)
    verifier = VerifierAgent(mock_llm)
    output = verifier.verify(results, "Test")
    assert "Test output" in output