FROM alpine:latest

RUN apk add --no-cache python3
RUN rm -rf /var/cache/apk/*
WORKDIR /home
RUN mkdir /home/data
RUN mkdir /home/output
COPY ./*.py .
CMD ["python3", "PythonScript.py"]