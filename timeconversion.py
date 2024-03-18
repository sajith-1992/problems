def timeConversion(s):
    hour,minute,seconds = map(int,s[:-2].split(":"))
    timePeriod=s[-2:]   
    if timePeriod == "PM" and hour != 12 :
        hour +=12
    elif timePeriod == "AM" and hour == 12:
        hour=0
    militaryTime = "{:02d}:{:02d}:{:02d}".format(hour,minute,seconds)
    print( militaryTime)
    
    

timeConversion("04:20:30PM")
