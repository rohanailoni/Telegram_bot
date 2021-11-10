FROM python:3

WORKDIR /app


COPY . /app/
COPY req.txt /app/


RUN pip install -r req.txt


CMD ["python","server.py"]