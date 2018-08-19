# Use an official Python runtime as a parent image
FROM python:3.6

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Ports Exposed for Masonite
EXPOSE 80 443 5432

# Run app.py when the container launches
CMD ["gunicorn", "-w", "3", "wsgi:application"]