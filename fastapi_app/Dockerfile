#use offcial python image
FROM python:3.11-slim

#set working directory inside container
WORKDIR /app

#Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy FastAPI code
COPY . .

# Expose port 8000
EXPOSE 8000

#Run FastAPI when container starts
CMD ["uvicorn","fastapi_app.main:app","--host","0.0.0.0","--port","8000"]

