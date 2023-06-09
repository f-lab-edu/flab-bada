FROM python:3.11
RUN mkdir /usr/local/flab-bada
COPY . /usr/local/flab-bada
WORKDIR /usr/local/flab-bada

RUN apt-get update && apt-get -y upgrade
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN curl -sSL https://install.python-poetry.org | python3 - && poetry install --no-root
CMD poetry run uvicorn main:app --host 0.0.0.0 --port 80