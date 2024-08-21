# Use an official Python runtime as a parent image
FROM python:3.9

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ARG username
ENV username=${username}

ARG pat
ENV pat=${pat}

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /app
COPY ./app /code

# Install Python packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

VOLUME /var/run/docker.sock /var/run/docker.sock

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the Flask app
CMD ["python", "-m", "main"]