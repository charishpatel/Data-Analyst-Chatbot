# Use Python 3.11.5 as the base image
FROM python:3.11.5-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port your app will run on (changing it to 8080)
EXPOSE 8080

# Set the entrypoint to run your app
CMD ["python", "main.py"]
