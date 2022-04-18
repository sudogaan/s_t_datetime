gvr = datetime(1956, 1, 31)
print(gvr.month)
print(gvr.year)
print(gvr.day)

#datetime has a module in it called as timedelta which allows the addition or substraction of dates

mill =datetime.date(2000, 1, 1)

dt = datetime.timedelta(100)

print(mill+dt) # the output is 2000-04-10, addition of 100 to the existing date

#to get Day-name, Month-name Day-#, Year
#there are two ways that we can use to do it:
#1st one:
print(gvr.strftime("%A, %B %d, %Y))
#2nd one:
message = "GVR was born on {:%A, %B %d, %Y}."
print(message.format(gvr))

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime(2017, 3, 30, 22, 27, 0)

print(launch_date)
print(launch_time)
print(launch_datetime)


#accessing the current datetime

now = datetime.datetime.today()
print(now) #we get the exact date and time you run your code
#but there is a fractional value after the second, this module can store time down to the microseconds.

#converting string to a datetime object

moon_landing = 7/20/1969
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y)
print(moon_landing_datetime) 
print(type(moon_landing_datetime)
