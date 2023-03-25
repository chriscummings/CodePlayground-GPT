FROM python:3.11-slim

WORKDIR /code

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./pygen-gpt.py ./

CMD ["tail", "-f", "/dev/nul"]