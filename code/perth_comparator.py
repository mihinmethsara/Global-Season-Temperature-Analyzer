from data import CITY_AVERAGES
from input_validator import normalize_city, normalize_time, is_valid_city


def compare_with_perth(city, temp, time_of_day): #parameter pass
    
    #compare citys temperature with perth    
    
    city_norm = normalize_city(city)
    if not city_norm or not is_valid_city(city_norm):
        return "Invalid city"
    
    time_norm = normalize_time(time_of_day)
    if time_norm is None:
        return "Invalid time of day. Use morning or afternoon"
    
    perth_average = CITY_AVERAGES["Perth"][time_norm]
    
    if temp > perth_average:
        return f"{city_norm} is warmer than Perth"
    elif temp < perth_average:
        return f"{city_norm} is cooler than Perth"
    else:
        return f"{city_norm} is the same as Perth"


