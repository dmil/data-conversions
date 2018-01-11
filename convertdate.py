from datetime import datetime

raw_date = "2017-01-11"


parsed_date = datetime.strptime(raw_date, "%Y-%m-%d")

print parsed_date.strftime("%d/%m/%y") # 01/11/17
