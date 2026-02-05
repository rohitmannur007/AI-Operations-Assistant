AI Operations Assistant

This project is a multi-agent AI system that takes natural-language tasks, plans steps, executes them using tools (external APIs), and verifies the results.
Built for the GenAI Intern Assignment (TrulyMadly).

⚠️ Important:
This project uses paid / rate-limited external APIs (xAI Grok, OpenWeather, GitHub).
The included code is correct, but you must use your own API keys to run it.
The author’s keys are NOT included.

⸻

Setup Instructions (Run Locally)
	1.	Clone the repository:

git clone <your-repo-url>
cd AI-Operations-Assistant

	2.	Create a virtual environment:

python3 -m venv venv
source venv/bin/activate

	3.	Install dependencies:

pip install -r requirements.txt

	4.	Create environment file:

cp .env.example .env

	5.	Add your API keys to .env.
	6.	Run the app:

make run

or

streamlit run main.py

	7.	Open in browser:

http://localhost:8501


⸻

Environment Variables (.env.example)

GROK_API_KEY=your_xai_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
GITHUB_TOKEN=your_github_token   # optional


⸻

Architecture Explanation

Agents
	•	Planner Agent
Converts the user task into a structured JSON plan.
	•	Executor Agent
Executes each step using tools (GitHub, Weather, or reasoning).
	•	Verifier Agent
Validates the execution results and produces a clean final answer.

Tools
	•	GitHubTool – Fetches repositories, stars, descriptions.
	•	WeatherTool – Fetches live weather by city.

Flow

User → Planner → Executor → Verifier → UI


⸻

Integrated APIs
	•	xAI Grok API – LLM reasoning & planning
	•	GitHub REST API – Repository search
	•	OpenWeatherMap API – Weather data

⸻

Example Prompts
	1.	Find the top 3 Python repos on GitHub and get their star counts.
	2.	What’s the weather in Mumbai right now?
	3.	Search for AI repos on GitHub and check the weather in San Francisco.
	4.	Get details for the ‘tensorflow/tensorflow’ repo on GitHub.
	5.	Plan a trip: Weather in New York and popular ML repos.

⸻

Known Limitations / Tradeoffs
	•	Requires external API keys
	•	Grok API requires paid credits
	•	Sequential tool execution (no parallelism)
	•	Basic UI (no auth, no persistence)
	•	API rate limits

⸻

Smoke Tests

make test


⸻

License

MIT License
Author: Rohit Mannur

