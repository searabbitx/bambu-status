FROM python:3

RUN apt-get update && apt-get install -y \
    software-properties-common \
    npm \
	nginx

RUN npm install npm@latest -g

ADD entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod 777 /usr/local/bin/entrypoint.sh

ADD nginx/default /etc/nginx/sites-available/default

WORKDIR /usr/src/frontend

COPY frontend .
RUN npm run build

WORKDIR /usr/src/app

COPY flask .

RUN pip install --disable-pip-version-check --no-cache-dir -r requirements.txt

CMD /usr/local/bin/entrypoint.sh
