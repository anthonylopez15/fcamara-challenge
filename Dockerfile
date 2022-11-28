FROM python:3.8-slim

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /home/app/

COPY Pipfile Pipfile.lock /home/app/

RUN apt-get update -qq && \
    apt-get clean && \
    rm -rf /var/cache/apk/* && \
    pip install --upgrade pip==20.2.3 --no-cache-dir

RUN pip install pipenv --no-cache-dir && \
    pipenv install --system --ignore-pipfile --deploy


COPY ./ /home/app/

CMD [ "uvicorn", "main:app", "--reload", "--workers", "1",  "--host",  "0.0.0.0", "--port", "8000"  ]

EXPOSE 8000