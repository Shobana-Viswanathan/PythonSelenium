import logging
import Utilities.logCreator as logCreator
def log_generator():
    logging.basicConfig(filename="testlogReport.log",level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%Y-%M-%d %H:%M:%S %p', force= True)
    return logging.getLogger()
