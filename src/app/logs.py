import datetime
import logging


class Logs:

    def __init__(self):
        self.timestamp = datetime.datetime.now()

    def info(self, data: str):
        message = "{}: File loading {}".format(self.timestamp, data)
        logging.info(message)

    def error(self, data_error: str):
        message = "{}: Error data: {}".format(self.timestamp, data_error)
        logging.error(message)
