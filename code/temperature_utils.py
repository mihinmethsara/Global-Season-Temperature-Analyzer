 #average temperatures from figure2

CITY_AVERAGES = {
    "Perth": {"morning": 18.2, "afternoon": 23.0},
    "Adelaide": {"morning": 16.5, "afternoon": 21.0},
     "Brisbane": {"morning": 21.8, "afternoon": 24.8}
}

  #temperature min and max ranges from figure2

CITY_RANGES = {
    "Perth": {"min": 0.7, "max": 46.0},
    "Adelaide": {"min": -1.0, "max": 49.0},
     "Brisbane": {"min": 2.6, "max": 41.7}
}



 #check city temperature with average given

def check_city_temperature(city, temp, time_of_day):

    city = city.strip().title()  
    time_of_day = time_of_day.lower()

    
    if city not in CITY_AVERAGES:  #check if city valid
        return "Invalid city"
        

     
    if time_of_day not in ["morning", "afternoon"]:  #check if time valid
       return "Invalid time of day. Use morning or afternoon"
        


    min_temp = CITY_RANGES[city]["min"]
    max_temp = CITY_RANGES[city]["max"]

     
     #check temperature range for city

    if temp < min_temp:
        return f"Temperature {temp}°C is below minimum ({min_temp}°C) for {city}"
        
    if temp > max_temp:
        return f"Temperature {temp}°C is above maximum ({max_temp}°C) for {city}"
        
    


    avg = CITY_AVERAGES[city][time_of_day]
    diff = round(temp - avg, 1) #get differece of tempreture with average


     #check difference above below or same

    if diff > 0:
        status = "above"
    elif diff < 0:
        status = "below"
    else:
        status = "same as"


    message = f"{temp}°C is {status} average ({avg}°C) in {city} ({time_of_day})."  #result message


     #add warning if difference  large

    if abs(diff) > 6:
       message += f" Significant difference! ({diff:+.1f}°C)" #shows  how much above or below


    return message


