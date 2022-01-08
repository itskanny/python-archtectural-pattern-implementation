FROM python:3.10-alpine

WORKDIR /patterns

#COPY . .

CMD [ "python", "./information_handler.py" ]