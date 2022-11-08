FROM python:3.10

WORKDIR /app/src/

COPY ./requirements.txt .
# RUN pip install --upgrade pip  && pip install -r ./requirements.txt && rm ./requirements.tx
RUN apt-get update && apt-get install python3-tk -y

COPY ./src .

COPY ./run_loop.py /app/run_loop.py