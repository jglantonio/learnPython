FROM python:3
WORKDIR /usr/src/app
COPY scripts .
CMD [ "python", "./scripts/file.py" ]