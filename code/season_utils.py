from data import SEASON_DATA,NOONGAR_SEASONS,VALID_MONTHS
from input_validator import normalize_country, normalize_month


def get_meteorological_season(country, month):

    country = normalize_country(country)
    month = normalize_month(month)

    if not country or not month:
        return "Invalid country or month"

    if country not in SEASON_DATA:
        return "Invalid country"

    for season_name, month_list in SEASON_DATA[country].items():
        if month in month_list:
            return season_name

    return "Invalid month"




def get_traditional_season(country, month):
     #module 2 find traditional noongar season for australia from figure1

    if month_str in month_numbers:
       month_str = month_numbers[month_str]


     #check if country is australia becauce  australia only have traditional seasons
    if country != "Australia":
        return "No traditional season for this country"
    

       #find matching season and return

    for season_name, valid_months in noongar_seasons.items():
        if month_str in valid_months:
            return season_name


     #if month not match any season
    return "No traditional season for this month" 





def check_seasons_same(country1, country2, month):
    #module 3 check if two countries have same season for given month

      #get seasons for both countries using module1
    season1 = get_meteorological_season(country1, month)
    season2 = get_meteorological_season(country2, month)

     
    print(f"\n---Season Comparison Result---") #show comparison result screen
    print(f"{country1} in {month}: {season1}")
    print(f"{country2} in {month}: {season2}")


       #check if any country or month  invalid

    if "Invalid" in season1 or "Invalid" in season2:
        print("Cannot compare invalid country or month entered.")
        return False
    

    #check if seasons are same or different
    if season1 == season2:
        print(f"Result: same season → Both countries have {season1}")
        return True
    
    else:
        print(f"Result: different seasons → {country1} has {season1}, {country2} has {season2}")
        return False
    