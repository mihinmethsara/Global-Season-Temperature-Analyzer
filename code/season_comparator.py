from season_finder import get_meteorological_season


def check_seasons_same(country1, country2, month):
     #check if two countries have the same season
   
    season1 = get_meteorological_season(country1, month)
    season2 = get_meteorological_season(country2, month)
    
    print(f"\n--- Season comparison result ---")
    print(f"{country1} in {month}: {season1}")
    print(f"{country2} in {month}: {season2}")
    
    if "Invalid" in season1 or "Invalid" in season2:
        print("Cannot compare invalid country or month entered.")
        return False
    
    if season1 == season2:
        print(f"Result: same season → Both countries have {season1}")
        return True
    else:
        print(f"Result: different seasons → {country1} has {season1}, {country2} has {season2}")
        return False



def compare_seasons_with_output_file(country1, country2, month, output_file):
    
    #samecheck seasons_same with writes output to file test
    
    season1 = get_meteorological_season(country1, month)
    season2 = get_meteorological_season(country2, month)

    
    with open(output_file, 'w') as f:
        f.write(f"Season Comparison Result\n")
        f.write(f"{country1} in {month}: {season1}\n")
        f.write(f"{country2} in {month}: {season2}\n")
        
        if "Invalid" in season1 or "Invalid" in season2:
            f.write("Cannot compare invalid country or month entered.\n")
            return False
        
        if season1 == season2:
            f.write(f"Result: same season -Both countries have {season1}\n")
            return True
        else:
            f.write(f"Result: different seasons - {country1} has {season1}, {country2} has {season2}\n")
            return False