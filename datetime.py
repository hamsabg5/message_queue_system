import datetime

class Datetime():

    def get_current_datetime(self):
        return datetime.datetime.today()

    def get_next_day(self):
        return datetime.datetime.today() + datetime.timedelta(days=1)

    def get_datetime_as_string(self,datetime_value):
        return datetime_value.strftime('%d%m%Y')

    def get_convert_to_datetime(self,datetime_string):
        return datetime.datetime.strptime(datetime_string,'%d%m%Y')

    def get_current_date(self):
        return datetime.datetime.date()

    def get_time_stamp(self):
        return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d::%H:%M:%S - ')