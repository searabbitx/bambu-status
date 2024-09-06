FROM python:3

WORKDIR /usr/src/app

COPY src .
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]
