# Use official Python image
FROM python:3.11-slim

# Set working directory in the container
WORKDIR cd ~/IT/ChatGPT-Memory-Automation/

# Copy local files into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Run the app (adjust if your main file is not app.py)
CMD ["streamlit", "run", "app.py"]
