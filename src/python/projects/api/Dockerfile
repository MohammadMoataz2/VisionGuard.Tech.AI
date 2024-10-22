FROM python:3.11

EXPOSE 8011
WORKDIR /app

COPY src.python.projects.api.api/main.pex .

ENV PEX_SCRIPT=uvicorn
CMD ["./main.pex", "api.main:app", "--host", "0.0.0.0", "--port", "8011", "--reload"]
