
FROM public.ecr.aws/docker/library/python:3.9-slim

RUN apt-get update && apt-get install -y curl && apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip show newrelic

COPY . .

COPY newrelic.ini .  

EXPOSE 5000

ENV FLASK_APP=application.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV NEW_RELIC_CONFIG_FILE=newrelic.ini
CMD ["newrelic-admin", "run-program", "python", "application.py"]