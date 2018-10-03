FROM python:slim

COPY . /sql
WORKDIR /sql

RUN pip3 install -r requirements.txt
RUN python db.py

EXPOSE 3000

CMD ["gunicorn", "-c", "gunicorn.conf", "sql:app"]