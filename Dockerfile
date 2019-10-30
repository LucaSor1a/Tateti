FROM python:3

RUN git clone https://github.com/LucaSor1a/Tateti
WORKDIR /Tateti

RUN pip install parameterized

CMD ["python3", "./test_tateti.py"]
