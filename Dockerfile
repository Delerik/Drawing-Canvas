FROM python:3.8.2
RUN apt-get update && apt-get install postgresql libpq-dev -y

RUN mkdir /opt/canvas_drawer

COPY run-test.sh /opt/canvas_drawer/run-test.sh
COPY check.py /opt/canvas_drawer/check.py
COPY utils /opt/canvas_drawer/utils
COPY main.py /opt/canvas_drawer
COPY requirements.txt /opt/canvas_drawer
COPY domain /opt/canvas_drawer/domain
COPY consumer /opt/canvas_drawer/consumer
COPY data_connect /opt/canvas_drawer/data_connect
COPY scripts /opt/canvas_drawer/scripts
RUN chmod +x /opt/canvas_drawer/run-test.sh

WORKDIR /opt/canvas_drawer
ENV PYTHONPATH /opt/canvas_drawer

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3", "main.py"]


