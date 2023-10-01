# takes one python image called 3.8...
FROM python:3.8-slim-buster

EXPOSE 8501

#This line is like adding additional LEGO pieces or tools that are needed, which in this case is the AWS command line interface.
RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*
# creates one app directory
WORKDIR /app

# it copies all the source code and puts it inside it
COPY . /app
# installs requirements
RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]