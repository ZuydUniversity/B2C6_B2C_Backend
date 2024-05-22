FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

ENV DB_USER=databaseuser
ENV DB_PASSWORD=$uperVe1ligWachtWoord
ENV DB_HOST=20.86.139.126
ENV DB_NAME=mvp

EXPOSE 80

CMD ["fastapi", "run", "app/main.py", "--port", "80"]