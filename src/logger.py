import logging

class Log:
    def __init__(self) -> None:
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
    
    @staticmethod
    def log(msg):
        logging.info(msg)