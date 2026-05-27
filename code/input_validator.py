from data import (VALID_COUNTRIES, VALID_MONTHS, VALID_CITIES, VALID_TIMES,
 MONTH_NUMBER_TO_NAME, CITY_RANGES
)


def normalize_country(country):
    #format and stadarize country name

    if country is None:
        return None
    if isinstance(country, str):
        result = country.strip().title()
        return result if result else None
    return None


def is_valid_country(country):
    #Check if country exists data

    norm = normalize_country(country)
    return norm in VALID_COUNTRIES if norm else False


def normalize_month(month):
  
    #convert month input to standardized month name
    

    if month is None:
        return None
    
    #handle integer and float

    if isinstance(month, (int, float)):
        month_num = int(month)
        if 1 <= month_num <= 12:
            return MONTH_NUMBER_TO_NAME.get(str(month_num))
        return None
    


     #handle string
    if isinstance(month, str):
        month_str = month.strip().title()
        if not month_str:
            return None
        
       
        if month_str in VALID_MONTHS:
            return month_str
        
        #number of month to name
        if month_str in MONTH_NUMBER_TO_NAME:
            return MONTH_NUMBER_TO_NAME[month_str]
        
        
        return None
    
    return None



def is_valid_month(month): #check month valid
    return normalize_month(month) is not None


def normalize_city(city): #format and stadarize cityname

    if city is None:
        return None
    if isinstance(city, str):
        result = city.strip().title()
        return result if result else None
    return None


def is_valid_city(city):
    #check city exists  data
    norm = normalize_city(city)
    return norm in VALID_CITIES if norm else False


def normalize_time(time): #standardize time of day"
    if time is None:
        return None
    if isinstance(time, str):
        result = time.strip().lower()
        return result if result in VALID_TIMES else None #check time is morning or afternoon
    return None




def is_temperature_in_range(city, temp):
    #check temperature is within valid range city

    norm_city = normalize_city(city)
    if norm_city not in CITY_RANGES:
        return False
    range_data = CITY_RANGES[norm_city]
    return range_data["min"] <= temp <= range_data["max"]


def get_temperature_range_message(city, temp): #if temperature out of range message give
    norm_city = normalize_city(city)
    if norm_city not in CITY_RANGES:
        return None
    range_data = CITY_RANGES[norm_city]
    if temp < range_data["min"]:
        return f"Temperature {temp}°C is below minimum ({range_data['min']}°C) for {norm_city}"
    if temp > range_data["max"]:
        return f"Temperature {temp}°C is above maximum ({range_data['max']}°C) for {norm_city}"
    return None



def validate_month_strict(month):
 
    try:
       
        month_int = int(month)
        
        if 1 <= month_int <= 12:
            return month_int
        else:
            raise ValueError(f"Month {month_int} is out of range (1-12)") #if not range 
            
    except TypeError:
       
        raise TypeError(f"Month must be a number, got {type(month).__name__}")
        
    except ValueError:
        raise ValueError(f"Invalid month value: {month}")