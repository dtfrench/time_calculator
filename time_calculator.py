def add_time(start, duration, day=None):

  #Separte the hours and numbers from the start argument so they can be converted to integers and make AM/PM lowercase
  start = start.split()
  start_digits = start[0].split(":")
  start_tod = start[1].lower()

  #Convert the provided time to 24 hours standard instead of 12 hour standard. Convert the hours and minutes to integers. 
  if (start_tod == "am"):
    start_hours = int(start_digits[0])
  elif (start_tod == "pm"):
    start_hours = int(start_digits[0]) + 12

  start_minutes = int(start_digits[1])

  #Separate the hours and numbers from the duration argument so they can be converted to integers.
  duration = duration.split()
  duration_digits = duration[0].split(":") 

  duration_hours = int(duration_digits[0])
  duration_minutes = int(duration_digits[1])

  #Add the hours from the start parameter and the hours from the duration parameter to calculate the number of days that have passed.
  final_hours = start_hours + duration_hours
  final_minutes = start_minutes + duration_minutes

  if (final_hours / 24 < 1):
    final_days = 0
  else:
    final_days = round(final_hours / 24)
  
  #A list of all the days of the week to iterate through
  days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

  #If the day is provided in the optional day variable, convert it to all lowercase. 
  if (day != None):
    day = day.lower()

  #If the string provided in the optional day paremeter is in the days list return the appropriate day after the calculated number of days has passed. 
  if (day in days and final_days == 0):
    day_of_week = f", {day.title()}"
  
  elif (day in days and final_days > 0):
    start_index = days.index(day)
    index_total = final_days
    while (index_total > 0):
      index_total -=  1
      if (start_index < len(days) -1):
        start_index += 1
      else:
        start_index = 0
      day_of_week = f", {days[start_index].title()}"
  
  else:
    day_of_week = ''
  
  #Calculate the hours and minutes of the time after the duration and format the resulting minutes in a string. 
  final_hours = (start_hours + duration_hours) - (final_days * 24)

  if (final_minutes >= 60):
    final_hours += 1
    final_minutes -= 60
  
  if (final_minutes < 10):
    final_minutes = "0" + str(final_minutes)
  else:
    final_minutes = str(final_minutes)
  
  #Convert the final hours back to 12 hour format and the appropriate time of day (AM/PM).
  if (final_hours > 12):
    final_tod = "PM"
    final_string_hours = str(final_hours - 12)
  
  elif (final_hours == 12):
    final_tod = "PM"
    final_string_hours = str(final_hours)
  
  elif (final_hours < 12 and final_hours > 0):
    final_tod = "AM"
    final_string_hours = str(final_hours)
  
  elif(final_hours == 0):
    final_tod = "AM"
    final_string_hours = "12"

  #If the ending time is the next day then "(next day)"" should be added to the return string, otherwise "N days later" should be added. N is the number of days that have passed. 
  if (final_days == 1):
    final_string = f" (next day)"
  
  elif(final_days > 1):
    final_string = f" ({final_days} days later)"
  
  else:
    final_string = ''
  
  #Construct the properly formatted string with hours, minutes, time of day (AM/PM), the optional day of the week, and next day/n days later string as appropriate. Return it. 
  final_time = final_string_hours + ":" + final_minutes + f" {final_tod}" + day_of_week + final_string

  return final_time


    
