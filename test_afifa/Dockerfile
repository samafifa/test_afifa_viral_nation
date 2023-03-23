FROM python:3.9.9-buster

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

# Install wait-for-it
COPY wait-for-it.sh /usr/local/bin/
RUN chmod u+x /usr/local/bin/wait-for-it.sh

# install postgresql client
RUN apt-get update
RUN apt-get install -y postgresql-client

# Configure custom entrypoint to wait for postgres and run webserver
COPY custom-entrypoint /usr/local/bin/
RUN chmod u+x /usr/local/bin/custom-entrypoint
ENTRYPOINT ["custom-entrypoint"]

EXPOSE 8000
