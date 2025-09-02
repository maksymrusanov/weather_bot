FROM python:3.13-slim
WORKDIR /app
COPY req.txt .
RUN pip install -r req.txt
COPY . .
CMD [ "python","bot_main.py" ]