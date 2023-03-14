from requests import Response

from utils.api import RestfulBookerAPI
from utils.checking import Checking

""" Tests for restful-booker API """

bookingid = None
first_name = ""
last_name = ""


class TestRestfulBookerAPI:

    """ Health Check """

    def test_get_ping(self):
        print("\nGET - Health Check")
        result_get: Response = RestfulBookerAPI.get_ping()
        Checking.check_status_code(result_get, 201)

    """ Auth User & Create Token """

    def test_auth_user(self):
        print("\nPOST - Auth User & Create Token")
        result_post: Response = RestfulBookerAPI.auth_user()
        Checking.check_status_code(result_post, 200)
        Checking.check_response_json(result_post, ["token"])

    """ Create Booking """

    def test_create_booking(self):
        print("\nPOST - Create Booking")
        global bookingid
        result_post: Response = RestfulBookerAPI.create_booking()
        check_post = result_post.json()
        get_id = check_post.get("bookingid")
        bookingid = get_id
        Checking.check_status_code(result_post, 200)
        Checking.check_response_json(result_post, ["bookingid", "booking"])
        Checking.check_json_value(result_post, "bookingid", bookingid)

    """ Get Booking """

    def test_get_booking(self):
        print("\nGET - Get Booking")
        global bookingid
        result_get: Response = RestfulBookerAPI.get_booking(str(bookingid))
        Checking.check_status_code(result_get, 200)
        Checking.check_response_json(result_get, ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates",
                                                  "additionalneeds"])

    """ Update Booking """

    def test_update_booking(self):
        print("\nPUT - Update Booking")
        global first_name, last_name
        result_put: Response = RestfulBookerAPI.update_booking(str(bookingid))
        check_put = result_put.json()
        get_first_name = check_put.get("firstname")
        get_last_name = check_put.get("lastname")
        first_name = get_first_name
        last_name = get_last_name
        Checking.check_status_code(result_put, 200)
        Checking.check_response_json(result_put, ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates",
                                                  "additionalneeds"])

    """ Partial Update Booking """

    def test_partial_update_booking(self):
        print("\nPATCH - Partial Update Booking")
        global first_name, last_name
        result_patch: Response = RestfulBookerAPI.partial_update_booking(str(bookingid))
        check_patch = result_patch.json()
        get_first_name = check_patch.get("firstname")
        get_last_name = check_patch.get("lastname")
        first_name = get_first_name
        last_name = get_last_name
        Checking.check_status_code(result_patch, 200)
        Checking.check_response_json(result_patch,
                                     ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates",
                                      "additionalneeds"])

    """ Get Booking Ids """

    def test_get_bookingids(self):
        print("\nGET - Get Booking Ids")
        result_get: Response = RestfulBookerAPI.get_bookingids(first_name, last_name)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_value(result_get, "bookingid", bookingid)

    """ Delete Booking """

    def test_delete_booking(self):
        print("\nDELETE - Delete Booking")
        result_delete: Response = RestfulBookerAPI.delete_booking(str(bookingid))
        Checking.check_status_code(result_delete, 201)

    """ Get Booking After Delete """

    def test_get_booking_after_delete(self):
        print("\nGET - Get Booking")
        result_get: Response = RestfulBookerAPI.get_booking(str(bookingid))
        Checking.check_status_code(result_get, 404)
