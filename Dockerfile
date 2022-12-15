# 1. Base image
FROM python:3.8

# 2. Create app directory
RUN mkdir -p /app/

# 3. Copy files
COPY python_app.py /app

# 4. define entrypoint to launch python_app.py
ENTRYPOINT ["python", "/app/python_app.py"]
