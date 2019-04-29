import logging
"""
# add filemode="w" to overwrite
logging.basicConfig(filename="sample.log", level=logging.INFO)

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")
"""
"""
logging.basicConfig(filename="sample.log", level=logging.INFO)
log = logging.getLogger("ex")

try:
    raise RuntimeError
except Exception:
    log.exception("Error!")
"""
import logging
from log_parse import otherMod2
import os


# ----------------------------------------------------------------------
def main():
    """
    The main entry point of the application
    """
    #print(os.getcwd())
    logger = logging.getLogger("exampleApp")
    logger.setLevel(logging.INFO)

    # create the logging file handler
    fh = logging.FileHandler("logging_1.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)

    logger.info("Program started")
    result = otherMod2.add(7, 8)
    logger.info("Done!")

    x=10
    y = 100
    logger = logging.getLogger("example")
    logger.info("added %s and %s to get %s" % (x, y, x + y))


if __name__ == "__main__":
    main()