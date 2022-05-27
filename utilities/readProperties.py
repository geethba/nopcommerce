import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
       url= config.get('common data','baseurl')
       return url
    @staticmethod
    def getuseremail():
        username=config.get('common data','useremail')
        return username
    @staticmethod
    def getpasword():
        password=config.get('common data','Password')
        return password
