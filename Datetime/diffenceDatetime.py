from datetime import datetime
datetime_ist = datetime.now(IST) 
print("Date & Time in IST : ",  
      datetime_ist.strftime('%Y:%m:%d %H:%M:%S %Z %z')) 

start = datetime.strptime("10:41:00", "%H:%M:%S") 
end = datetime.strptime("19:18:00", "%H:%M:%S") 
  
difference = end - start 
  
seconds = difference.total_seconds() 
print('difference in seconds is:', seconds) 
  
minutes = seconds / 60
print('difference in minutes is:', minutes) 
  
hours = seconds / (60 * 60) 
print('difference in hours is:', hours)





# def addtwo(a, b):
#     pass

# @squar
# @percent
# @route
# @addtwo
# def nums(2, 6):
#     print('it is adding')


# print(nums())
# output:
# it is adding


# squar -> percent -> route -> addtwo -> nums

# squar(percent(route(addtwo(nums))))
