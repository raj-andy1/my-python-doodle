import datetime
import dateutil.parser
import json



with open('/Users/arajagopalan/Downloads/x_ace_history.json', 'r') as f:
    contents = json.load(f)

    for content in contents:
        date = content.get('time')
        print(date)
        try:
            print(datetime.datetime.strptime(date, "%m/%d/%Y, %H:%M:%S").strftime("%m/%d/%y"))
        except TypeError:
            print(f'invalid date: {date}')
            continue
        except ValueError:
            print(dateutil.parser.parse(date).strftime("%m/%d/%y"))
            continue


