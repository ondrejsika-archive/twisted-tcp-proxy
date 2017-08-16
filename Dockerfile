FROM python:2.7
MAINTAINER Ondrej Sika <ondrej@ondrejsika.com>
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY proxy.py /app/proxy.py
WORKDIR /app
ENTRYPOINT ["python", "proxy.py"]
