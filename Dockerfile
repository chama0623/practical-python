FROM python:3.12-slim

# set timezone
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update

RUN pip install --upgrade pip
RUN pip install poetry jupyterlab
RUN poetry config virtualenvs.create false