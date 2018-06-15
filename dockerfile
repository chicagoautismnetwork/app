FROM ubuntu:latest
MAINTAINER David Matsumura "davidkunio@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME ChiAutNet

# Run app.py when the container launches
CMD ["python", "app.py"]
