run:
	streamlit run main.py

docker-build:
	docker build -t ai_ops_assistant .

docker-run:
	docker run -p 8501:8501 --env-file .env ai_ops_assistant

test:
	pytest tests/