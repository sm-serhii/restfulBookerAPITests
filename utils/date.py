from datetime import datetime, timedelta

""" Generate Checkin and Checkout Date """


class Date:

    @staticmethod
    def get_date():
        checkin = str(datetime.now().date())
        parse = datetime.strptime(checkin, '%Y-%m-%d')
        checkout = parse + timedelta(days=10)
        date = [checkin, checkout.strftime('%Y-%m-%d')]
        return date

    get_date = get_date()
    checkin = get_date[0]
    checkout = get_date[1]
