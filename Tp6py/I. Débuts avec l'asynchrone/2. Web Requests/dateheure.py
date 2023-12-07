import datetime

def get_date():
    return f"{datetime.date.today().day}-{datetime.date.today().month}-{datetime.date.today().year}"

def get_time():
    return f"{datetime.datetime.now().time().hour}:{datetime.datetime.now().time().minute}"