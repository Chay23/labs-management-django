FROM python:3.8.3-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /code

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip

COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /code/
RUN chmod +x /code/entrypoint.sh

COPY . /code/

ENTRYPOINT ["/code/entrypoint.sh"]