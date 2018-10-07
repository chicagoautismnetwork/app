FROM python:3.6.1-alpine
MAINTAINER David Matsumura "davidkunio@gmail.com"

WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

RUN apk update && apk add build-base postgresql-dev libffi-dev python3-dev

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80
EXPOSE 443

# Define environment variable
ENV NAME ChiAutNet

# Run app.py when the container launches
CMD ["python", "app.py"]
