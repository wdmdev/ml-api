FROM python:3.9

COPY api.py . 
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "api.py"]