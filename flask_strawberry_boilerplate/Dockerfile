# We use an official Python runtime as a parent image
FROM python:3.9.7

# create root directory for our project in the container
RUN mkdir /flask_strawberry_boilerplate

# copy the contents of the repo into the directory
COPY . /flask_strawberry_boilerplate
RUN rm -rf /flask_strawberry_boilerplate/.git

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y libev-dev

# setting PYTHONUNBUFFERED to 1 ensures the python output is sent straight to terminal, so we can see it in realtime
# instead of being buffered and only seeing it later.
# https://stackoverflow.com/a/59812588/15633871
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /flask_strawberry_boilerplate/requirements.txt
RUN pip install -r /flask_strawberry_boilerplate/requirements.txt

# set the working directory to the new root directory of our project
WORKDIR /flask_strawberry_boilerplate

CMD ["python", "app.py"]