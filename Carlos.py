import datetime

dateFormat = '%Y-%m-%d %H:%M:%S.%f'
currentTime = datetime.datetime.now().strftime(dateFormat)
print "The date is: " + currentTime
