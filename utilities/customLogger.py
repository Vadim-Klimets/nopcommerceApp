import logging



#class LogGen:
#    @staticmethod
#    def loggen():
#      logging.basicConfig(filename='.\\Logs\\automation.log',
#                           format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y/ %I:%M:%S %p')
#      logger = logging.getLogger()
#      logger.setLevel(logging.INFO)
#      return logger

class LogGen:
    @staticmethod
    def loggen():

#      for handler in logging.root.handlers[:]:
#            logging.root.removeHandler(handler)
      logging.basicConfig(filename='.\\Logs\\automation.log',
                        format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y/ %I:%M:%S %p')
      logger = logging.getLogger()
      handler = logging.FileHandler(filename='.\\Logs\\automation.log', mode='a')
      formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
      handler.setFormatter(formatter)
      logger.addHandler(handler)
      logger.setLevel(logging.INFO)
      return logger

#class LogGen:
#    @staticmethod
#    def loggen():
#        logger = logging.getLogger()
#        handler = logging.FileHandler(filename='.\\Logs\\automation.log', mode='a')
#        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#        handler.setFormatter(formatter)
#        logger.addHandler(handler)
#       logger.setLevel(logging.INFO)
#        return logger
