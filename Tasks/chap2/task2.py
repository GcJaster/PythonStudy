import logging
import os
import datetime
import itertools
import time


class MyLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __del__(self):
        print(f"Удаление экземпляра класса: {self}")
        # self._instance = None
        # os.remove(self.logger)
        # del self

    def __init__(self) -> None:
        pass

    def writeToLogFile(self, msg):
        with open('loggerFile.txt', 'a', encoding='utf-8') as lg:
            lg.write(msg + '\n')

        lg.close()

    def terminate(self):
        self.writeToLogFile('Файл закрывается')
        if self._instance is not None:
            self._instance = None
            del self



if __name__ == "__main__":
    logger = MyLogger()
    logger.writeToLogFile('msg1')
    logger.writeToLogFile('msg2')
    time.sleep(2)

