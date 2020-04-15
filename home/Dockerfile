FROM python:3.7-alpine
WORKDIR /home
COPY . /home
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python","home.py"]
