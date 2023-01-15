FROM python

COPY ./requiriments.txt /home/requiriments.txt
RUN pip install -r /home/requiriments.txt

COPY ./src /home/code
WORKDIR /home/code

CMD [ "python", "main.py" ]