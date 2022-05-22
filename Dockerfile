FROM python:3.9


RUN apt-get update

# RUN apt install python3-pip -y

# RUN apt-get install python3-flask -y


COPY ./src/requirements.txt /source/requirements.txt

RUN pip3 install --no-cache-dir -r /source/requirements.txt

COPY ./src /source

ENV FLASK_APP=/source/app.py
# ENV FLASK_DEBUG=True

# RUN export FLASK_ENV=development

EXPOSE 5000




CMD ["/usr/local/bin/flask", "run", "-h", "0.0.0.0"]
# CMD ["python3","/source/app.py"]
# RUN ./entrypoint.sh



