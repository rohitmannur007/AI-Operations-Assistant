import pytest
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.verifier import VerifierAgent
from llm.llm_client import LLMClient

class MockLLMClient(LLMClient):
    def chat_json(self, prompt, model=None):
        if "Planner" in prompt:
            return {"steps": [{"description": "Test step", "tool": "none"}]}
        elif "Verifier" in prompt:
            return {"final_answer": "Verified", "issues": []}

@pytest.fixture
def mock_llm():
    return MockLLMClient()

def test_smoke_flow(mock_llm):
    planner = PlannerAgent(mock_llm)
    plan = planner.plan("Test task")
    assert len(plan.steps) == 1
    executor = ExecutorAgent(mock_llm)
    results = executor.execute(plan)
    assert len(results) == 1
    verifier = VerifierAgent(mock_llm)
    output = verifier.verify(results, "Test task")
    assert "Verified" in output