import logging ,sys
import logging.config
import inspect

# DEBUG, INFO, WARNING(default level), ERROR, CRITICAL


#logging.basicConfig(filename="test_log.txt", level=logging.DEBUG)
#logging.basicConfig(format="%(asctime)s: %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.DEBUG)
# logging.warning("loggging.warning message")
# logging.info("logging.info message")
# logging.error("logging.error error message")
# logging.critical("logging.critical critical message")

class LoggerConsole():
    def testLog(self):
        logger = logging.getLogger("test_log")
        logger.setLevel(logging.INFO)
        #console handler
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s: -%(name)s -%(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        chandler.setFormatter(formatter)

        logger.addHandler(chandler)

        logger.warning("loggging.warning message")
        logger.info("logging.info message")
        logger.error("logging.error error message")
        logger.critical("logging.critical critical message")

    def customLogger(logLevel):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        logger.setLevel(logging.DEBUG)

        fileHandler = logging.FileHandler("{0}.log".format(loggerName), mode="w")
        fileHandler.setLevel(logLevel)

        formatter = logging.Formatter("%(asctime)s: -%(name)s -%(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        return logger
    
test = LoggerConsole()
test.testLog()
