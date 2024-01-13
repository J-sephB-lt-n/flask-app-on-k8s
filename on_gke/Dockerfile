
# Use the official lightweight Python image # 
# https://hub.docker.com/_/python
FROM python:3.12-slim

# Copy local code to the container image #
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install python dependencies #
RUN pip install -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
