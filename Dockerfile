FROM python:3.9-slim

COPY requirements.txt requirements.txt

RUN apt-get update -y && apt-get install imagemagick ffmpeg -y

RUN pip3 install -r requirements.txt

RUN sed -i 's/none/read,write/g' /etc/ImageMagick-6/policy.xml 

COPY . .

CMD ["python3", "main.py"]