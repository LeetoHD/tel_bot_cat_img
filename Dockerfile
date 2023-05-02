FROM python:3.8
WORKDIR /bot1
COPY . .
RUN pip install -r requirement.txt
CMD python3 /bot1/main.py