import logging

class LogGen:
    @staticmethod
    def loggen():
        # logger = logging.getLogger()
        # logging.basicConfig(filename='.\\Logss\\automationlog.log')
        #                     #format='%(asctime)s: %(levelname)s:%(message)s',datefmt = '%Y-%m-%d %H:%M:%S')
        #
        # logger.setLevel(logging.INFO)
        # return logger

        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='.\\Logss\\automation.log', mode='w')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger