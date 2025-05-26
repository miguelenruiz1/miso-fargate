FROM public.ecr.aws/docker/library/python:3.9-slim

RUN apt-get update && apt-get install -y curl && apt-get clean

WORKDIR /app

COPY requirements.txt .
# Aquí pip instalará Flask, SQLAlchemy, New Relic, etc.
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos tu configuración completa de New Relic 


# Indicamos al agente dónde está el config (no necesitarás ENV extra)
ENV NEW_RELIC_CONFIG_FILE=newrelic.ini

# Copiamos el resto de tu aplicación
COPY . .

EXPOSE 5000

# Arrancamos la app instrumentada con New Relic
CMD ["python", "application.py"]
