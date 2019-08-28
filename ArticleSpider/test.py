import datetime
try:
    create_date = datetime.datetime.strptime("2019/07/05", "%Y/%m/%d").date()
except Exception as e:
    create_date = datetime.datetime.now().date()

print(create_date)