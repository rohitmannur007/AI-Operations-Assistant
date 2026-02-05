class VerifierAgent:
    def __init__(self, llm):
        self.llm = llm

    def verify(self, result, task):
        return f"Task '{task}' completed successfully.\n\nResult:\n{result}"
