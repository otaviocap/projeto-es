FROM python:3.9
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends python-dev librocksdb-dev build-essential libsnappy-dev zlib1g-dev libbz2-dev libgflags-dev liblz4-dev

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app
RUN pip install -r requirements.txt

CMD [ "python3", "manage.py", "runserver" ]