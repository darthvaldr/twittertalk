#################################################
# Dockerfile to build Python ebooks twitter app
# Base : python-2.7.13
#################################################

FROM python:2.7.13
MAINTAINER darthvaldr

# setup where ebooks lives
RUN mkdir /ebooks

# add requirements from pwd to image
# ADD ./requirements.txt /requirements.txt
ADD ../ebooks /ebooks

# install requirements
RUN pip install -r /ebooks/requirements.txt

# default entrypoint
ENTRYPOINT ["/usr/local/bin/python", "/ebooks/ebooks.py"]
