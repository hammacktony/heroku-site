# Use an official Python runtime as a parent image
FROM python:3.6

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install pipenv
RUN pipenv install

# Declare environment variables
ENV APP_NAME=Masonite
ENV APP_ENV=local
ENV APP_DEBUG=True
ENV KEY=aAprSG7FIFEBjHs_04hnROedzyvLpQeqYn-MOhoYwgA=

ENV DB_DRIVER=postgres
ENV DB_HOST=ec2-54-235-244-185.compute-1.amazonaws.com
ENV DB_PORT=5432
ENV DB_DATABASE=dfqefn9gk5dgnj
ENV DB_USERNAME=pmnkiouizlkvpb
ENV DB_PASSWORD=e42ed49071fb7526e39693d62def04878ae1ae68058a1b3c6526eca0be120c64

ENV STORAGE_DRIVER=disk

# Ports Exposed for Masonite
EXPOSE 80 443 5432

# Run app.py when the container launches
CMD ["pipenv", "run", "gunicorn", "-w", "3", "wsgi:application"]