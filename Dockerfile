FROM python:3

WORKDIR /usr/src/app

COPY flask .
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py

CMD [ "python", "-m", "gunicorn", "-b", "0.0.0.0:5000", "app:app" ]
