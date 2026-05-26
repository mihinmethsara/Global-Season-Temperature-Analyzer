from data import SEASON_DATA, NOONGAR_SEASONS
from input_validator import normalize_country, normalize_month, is_valid_country


def get_meteorological_season(country, month):  #get meteorological or monsoon season for  country
    
    
    country_norm = normalize_country(country) #validate inputs
    if not country_norm or not is_valid_country(country_norm):
        return "Invalid country"
    
    
    month_norm = normalize_month(month)
    if month_norm is None:
        return "Invalid month"
    

     #find season
    if country_norm not in SEASON_DATA:
        return "Invalid country"
    
    for season_name, month_list in SEASON_DATA[country_norm].items():
        if month_norm in month_list:
            return season_name
    
    return "Invalid month"



def get_traditional_season(country, month):
    #get  traditional Noongar season only for australia

    country_norm = normalize_country(country)
    
    if country_norm != "Australia":  #check country is only ausralia
        return "No traditional season for this country"
    
    
    
    month_norm = normalize_month(month)
    if month_norm is None:
        return "No traditional season for this month"
    
    for season_name, month_list in NOONGAR_SEASONS.items():
        if month_norm in month_list:
            return season_name
    
    return "No traditional season for this month"