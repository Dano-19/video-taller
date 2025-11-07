FROM python:3.10-slim

LABEL maintainer="daniela-cardenas"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY daniela.py .

EXPOSE 8080

CMD ["python", "daniela.py"]