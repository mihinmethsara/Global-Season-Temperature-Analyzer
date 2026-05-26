from data import CITY_AVERAGES
from input_validator import normalize_city, normalize_time

def compare_with_perth(city, temp, time_of_day):

    city = normalize_city(city)
    time_of_day = normalize_time(time_of_day)

    if not city:
        return "Invalid city"

    if not time_of_day:
        return "Invalid time of day"

    perth_average = CITY_AVERAGES["Perth"][time_of_day]

    if temp > perth_average:
        return f"{city} is warmer than Perth"
    elif temp < perth_average:
        return f"{city} is cooler than Perth"
    else:
        return f"{city} is the same as Perth"