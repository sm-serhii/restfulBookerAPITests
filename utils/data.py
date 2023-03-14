import random

from utils.generator import DataGenerator

""" Generate Test Data """


class TestData:

    @staticmethod
    def gen_first_name():
        generator = DataGenerator()
        first_name = generator.first_name()
        return first_name

    @staticmethod
    def gen_last_name():
        generator = DataGenerator()
        last_name = generator.last_name()
        return last_name

    BASE_URL = "https://restful-booker.herokuapp.com"
    USERNAME = "admin"
    PASSWORD = "password123"

    FIRSTNAME = gen_first_name()
    LASTNAME = gen_last_name()
    DEPOSITPAID = True
    TOTALPRICE = random.randint(1000, 2000)
    ADDITIONALNEEDS = "Breakfast"

    FIRSTNAME_FOR_UPDATE = gen_first_name()
    LASTNAME_FOR_UPDATE = gen_last_name()
    DEPOSITPAID_FOR_UPDATE = False
    TOTALPRICE_FOR_UPDATE = TOTALPRICE + 50
    ADDITIONALNEEDS_FOR_UPDATE = "Breakfast, WiFi"
