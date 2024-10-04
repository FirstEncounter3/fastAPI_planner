FROM python:3.11

WORKDIR /backend

COPY requirements-dev.txt .

RUN pip install --no-cache-dir --upgrade && pip install -r requirements-dev.txt

EXPOSE 8000

COPY . .

CMD ["python3" , "main.py"]