FROM python:3.8-alpine
COPY ./requirements.txt /receiver/requirements.txt
WORKDIR /receiver
RUN pip install -r requirements.txt
COPY . /receiver
RUN sleep 40s 
CMD ["python", "receiver.py"]
