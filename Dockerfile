# Linux OS with Python
FROM python:alpine3.17

# Copy new files/directories to image filesystem
COPY . /app

# Change working directory
WORKDIR /app

# Install the required Python dependencies
RUN pip install -r requirements.txt

# Set Flask port
EXPOSE 5000

# Define the default command to run the Flask app
CMD ["python3", "app.py"]