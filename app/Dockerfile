FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /code/
RUN chmod +x /code/entrypoint.sh

COPY . /code/

ENTRYPOINT ["/code/entrypoint.sh"]