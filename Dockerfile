# Linux OS with Python
FROM python:alpine3.20

# Copy new files/directories to image filesystem
COPY . /app

# Change working directory
WORKDIR /app

# Install the required Python dependencies
RUN pip install -r requirements.txt

# Expose the port that Flask runs on (5000 by default)
EXPOSE 5000

# Command to run the Flask app
CMD ["python3", "app.py"]

# BUILD: docker build -t flask_api_exercise .
# RUN: docker run -it -p 5001:5000 flask_api_exercise   (-it allow for terminal access)