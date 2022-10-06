FROM python:3.8-alpine
COPY ./requirements.txt /receiver/requirements.txt
WORKDIR /receiver
RUN pip install -r requirements.txt
COPY . /receiver
CMD ["python", "receiver.py"]
