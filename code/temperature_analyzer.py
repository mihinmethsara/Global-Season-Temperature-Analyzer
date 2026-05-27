from data import CITY_AVERAGES
from input_validator import ( normalize_city, normalize_time, is_valid_city, is_valid_time,
                             get_temperature_range_message)



def check_city_temperature(city, temp, time_of_day):  #use parameter pass
    
    #check temperature against city average
   
    city_norm = normalize_city(city)
    if not city_norm or not is_valid_city(city_norm):
        return "Invalid city"
    
    time_norm = normalize_time(time_of_day)
    if time_norm is None:
        return "Invalid time of day. Use morning or afternoon"
    
    # Check temperature range
    range_msg = get_temperature_range_message(city_norm, temp)
    if range_msg:
        return range_msg
    
    avg = CITY_AVERAGES[city_norm][time_norm]
    diff = round(temp - avg, 1)
    
    if diff > 0:
        status = "above"
    elif diff < 0:
        status = "below"
    else:
        status = "same as"
    
    message = f"{temp}°C is {status} average ({avg}°C) in {city_norm} ({time_norm})."
    
    if abs(diff) > 6:
        message += f" Significant difference! ({diff:+.1f}°C)"
    
    return message



def print_city_temperature(city, temp, time_of_day): #Print  for console output testing
    result = check_city_temperature(city, temp, time_of_day)
    print(result)
    return result