#################################################
# Dockerfile for TwitterTalk 
# Base : python-3.6.2
#################################################

FROM python:3.6.2
MAINTAINER darthvaldr

# add application files to image
ADD app /app

# add requirements file
ADD requirements.txt /requirements.txt 

# install requirements
RUN pip install -r /requirements.txt

# set PYTHONPATH to find twitter_settings module
ENV PYTHONPATH /app

# default entrypoint
ENTRYPOINT ["/usr/local/bin/python", "/app/twittertalk.py"]
CMD ["/bin/bash"]
