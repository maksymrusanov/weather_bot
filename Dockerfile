FROM PYTHON:alpine
WORKDIR /app
COPY req.txt .
RUN pip install -r req.text
COPY . .
CMD [ "python","bot_main" ]