# Submission Notes for TrulyMadly GenAI Intern Assignment

## Test Commands Used Locally
- Install: `pip install -r requirements.txt`
- Run app: `make run` (or `streamlit run main.py`)
- Docker build & run: `make docker-build && make docker-run`
- Tests: `make test` (or `pytest tests/`)
- Pre-commit: `pre-commit run --all-files` (after `pip install pre-commit && pre-commit install`)

## Actual Sample Outputs (From My Local Runs)
1. Prompt: "Find the top 3 Python repos on GitHub and get their star counts."
   Output: [{"name": "TheAlgorithms/Python", "stars": 177714, "description": "All Algorithms implemented in Python"}, {"name": "public-apis/public-apis", "stars": 299053, "description": "A collective list of free APIs"}, {"name": "django/django", "stars": 77315, "description": "The Web framework for perfectionists with deadlines."}]
2. Prompt: "What's the weather in Mumbai right now?"
   Output: {"city": "Mumbai", "temperature": 27.99, "description": "haze"}
3. Prompt: "Search for AI repos on GitHub and check the weather in San Francisco."
   Output: GitHub: [{"name": "Significant-Gravitas/AutoGPT", "stars": 163355, "description": "AutoGPT is the vision of accessible AI for everyone, using GPT-4 to drive its actions."}, ...] Weather: {"city": "San Francisco", "temperature": 13.05, "description": "overcast clouds"}
4. Prompt: "Get details for the 'tensorflow/tensorflow' repo on GitHub."
   Output: {"name": "tensorflow/tensorflow", "stars": 183198, "description": "An Open Source Machine Learning Framework for Everyone"}
5. Prompt: "Plan a trip: Weather in New York and popular ML repos."
   Output: Weather: {"city": "New York", "temperature": 3.89, "description": "clear sky"} ML Repos: [{"name": "huggingface/transformers", "stars": 126948, "description": "🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX."}, ...]
(Note: Outputs vary based on real-time API data; these are from a test run on [your date].)

## Known Flaky Test Details
- None; all tests are deterministic with mocks. If APIs are called in tests (shouldn't be), rate limits could affect, but mocks prevent that.