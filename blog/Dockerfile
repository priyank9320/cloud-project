FROM python:3.7-alpine
WORKDIR /blog
COPY . /blog
RUN pip install -r requirements.txt
EXPOSE 8081
CMD [ "python","blog.py"]
