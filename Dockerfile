FROM ubuntu:20.04


RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install flask gunicorn && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt 

WORKDIR /opt/app

COPY ./dash_app /opt/app

ENV FLASK_ENV=development

EXPOSE 3457

CMD ["python3", "app.py", "--bind", "0.0.0.0:3457"]
