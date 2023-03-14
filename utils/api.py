from utils.date import Date

from utils.http_methods import Http_method
from utils.data import TestData

""" Requests for restfulBookerAPI """

base_url = TestData.BASE_URL
cookie = ""  # User Token
headers = {
    'Content-type': 'application/json',
    'Accept': 'application/json',
    'Cookie': cookie
}


class RestfulBookerAPI:

    """ Auth User & Create Token """

    @staticmethod
    def auth_user():
        json_for_create_user = {
            "username": TestData.USERNAME,
            "password": TestData.PASSWORD
        }
        global headers, cookie
        post_resource = "auth"  # POST resourse
        post_url = f"{base_url}/{post_resource}"
        print(post_url)
        result_post = Http_method.post(post_url, json_for_create_user)
        check_post = result_post.json()
        token = str(check_post.get("token"))
        cookie = "token=" + token
        headers['Cookie'] = cookie
        print(result_post.text)
        return result_post

    """ Create Booking """

    @staticmethod
    def create_booking():
        json_for_create_booking = {
            "firstname": TestData.FIRSTNAME,
            "lastname": TestData.LASTNAME,
            "totalprice": TestData.TOTALPRICE,
            "depositpaid": TestData.DEPOSITPAID,
            "bookingdates": {
                "checkin": Date.checkin,
                "checkout": Date.checkout
            },
            "additionalneeds": TestData.ADDITIONALNEEDS
        }

        post_resource = "booking"  # POST resourse
        post_url = f"{base_url}/{post_resource}"
        print(post_url)
        result_post = Http_method.post(post_url, json_for_create_booking)
        print(result_post.text)
        return result_post

    """ Get Booking """

    @staticmethod
    def get_booking(bookingid):
        get_resource = "booking"  # GET resourse
        get_url = f"{base_url}/{get_resource}/{bookingid}"
        print(get_url)
        result_get = Http_method.get(get_url)
        print(result_get.text)
        return result_get

    """ Update Booking """

    @staticmethod
    def update_booking(bookingid):
        json_for_update_booking = {
            "firstname": TestData.FIRSTNAME_FOR_UPDATE,
            "lastname": TestData.LASTNAME_FOR_UPDATE,
            "totalprice": TestData.TOTALPRICE_FOR_UPDATE,
            "depositpaid": TestData.DEPOSITPAID_FOR_UPDATE,
            "bookingdates": {
                "checkin": Date.checkin,
                "checkout": Date.checkout
            },
            "additionalneeds": TestData.ADDITIONALNEEDS_FOR_UPDATE
        }

        put_resource = "booking"  # PUT resourse
        put_url = f"{base_url}/{put_resource}/{bookingid}"
        print(put_url)
        result_put = Http_method.put(put_url, json_for_update_booking, headers)
        print(result_put.text)
        return result_put

    """ Partial Update Booking """

    @staticmethod
    def partial_update_booking(bookingid):
        json_for_partial_update_booking = {
            "firstname": TestData.FIRSTNAME_FOR_UPDATE,
            "lastname": TestData.LASTNAME_FOR_UPDATE
        }

        patch_resource = "booking"  # PATCH resourse
        patch_url = f"{base_url}/{patch_resource}/{bookingid}"
        print(patch_url)
        result_patch = Http_method.patch(patch_url, json_for_partial_update_booking, headers)
        print(result_patch.text)
        return result_patch

    """ Delete Booking """

    @staticmethod
    def delete_booking(bookingid):
        delete_resource = "booking"  # DELETE resourse
        delete_url = f"{base_url}/{delete_resource}/{bookingid}"
        print(delete_url)
        result_delete = Http_method.delete(delete_url, headers)
        print(result_delete.text)
        return result_delete

    """ Get Booking Ids """

    @staticmethod
    def get_bookingids(first_name, last_name):
        get_resource = "booking"  # GET resourse
        firstname = f"firstname={first_name}"
        lastname = f"lastname={last_name}"
        checkin_date = f"checkin={Date.checkin}"
        checkout_date = f"checkout={Date.checkout}"
        get_url = f"{base_url}/{get_resource}?{firstname}&{lastname}&{checkin_date}&{checkout_date}"
        print(get_url)
        result_get = Http_method.get(get_url)
        print(result_get.text)
        return result_get

    """ Health Check """

    @staticmethod
    def get_ping():
        get_resource = "ping"  # GET resourse
        get_url = f"{base_url}/{get_resource}/"
        print(get_url)
        result_get = Http_method.get(get_url)
        print(result_get.text)
        return result_get
