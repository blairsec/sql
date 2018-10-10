FROM python:slim

COPY . /sequel
WORKDIR /sequel

RUN pip3 install -r requirements.txt
RUN python db.py

EXPOSE 3000

CMD ["gunicorn", "-c", "gunicorn.conf", "sequel:app"]