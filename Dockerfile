FROM python:3.8.10

COPY ./backend /backend/src
COPY ./requirements.txt /backend

WORKDIR /backend

RUN pip install -r requirements.txt

WORKDIR /backend/src
RUN snips-nlu download en

EXPOSE 8000


CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]