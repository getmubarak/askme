FROM python:3.11-buster 

RUN apt-get update && apt-get install -y git

ENV HOST=0.0.0.0
ENV LISTEN_PORT 8080
EXPOSE 8080

WORKDIR /app

COPY ./AskMe ./AskMe
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

CMD ["streamlit", "run", "AskMe/index.py", "--server.port", "8080"]
