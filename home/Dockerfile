FROM python:3.7.7-slim-buster
ENV DB_HOST ${DB_HOST}
ENV DB_PORT ${DB_PORT}
ENV DB_NAME ${DB_NAME}
ENV DB_USER ${DB_USER}
ENV DB_PASSWORD ${DB_PASSWORD}
WORKDIR /home
COPY . /home
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python","home.py"]
