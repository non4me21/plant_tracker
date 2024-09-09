FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /project
COPY requirements.txt /project/
RUN pip install -r requirements.txt
RUN pip install pillow
COPY . /project/
