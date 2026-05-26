from data import CITY_AVERAGES
from input_validator import normalize_city, normalize_time


def check_city_temperature(city, temp, time_of_day):

    city = normalize_city(city)
    time_of_day = normalize_time(time_of_day)

    if not city:
        return "Invalid city"

    if not time_of_day:
        return "Invalid time of day. Use morning or afternoon"

    avg = CITY_AVERAGES[city][time_of_day]

    diff = round(temp - avg, 1)

    if diff > 0:
        status = "above"
    elif diff < 0:
        status = "below"
    else:
        status = "same as"

    message = f"{temp}°C is {status} average ({avg}°C) in {city} ({time_of_day})."

    if abs(diff) > 6:
        message += f" Significant difference! ({diff:+.1f}°C)"

    return message




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