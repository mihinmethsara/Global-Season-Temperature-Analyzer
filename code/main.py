from season_utils import get_meteorological_season, get_traditional_season, check_seasons_same
from temperature_utils import check_city_temperature, compare_with_perth


def main():
    print("\n-------------------------------------------")
    print("      Educational Software Tool- Menu")
    print("-------------------------------------------")
    
    while True:

        print("1. Find Meteorological Season")
        print("2. Find Traditional Season (Australia only)")
        print("3. Compare Seasons of Two Countries")
        print("4. Check City Temperature")
        print("5. Compare Temperature with Perth")
        print("6. Exit")
        print("-------------------------------------------")
        
        choice = input("Enter your choice (1-6): ").strip()
        
       

        if choice == "1":
            print("\n--- Find Meteorological Season ---")
            country = input("Enter country name: ").strip()
            month = input("Enter month (name or number): ").strip()
            
            season = get_meteorological_season(country, month)
            
            print("\n"+"-----------------------------------")
            print(f"Country: {country}")
            print(f"Month: {month}")
            print(f"Meteorological Season: {season}")
            print("-----------------------------------")
        
    

        elif choice == "2":
            print("\n--- Find Traditional Season ---")
            print("-----------------------------------\n")
            country = input("Enter country name: ").strip()
            month = input("Enter month (name or number): ").strip()
            
            season = get_traditional_season(country, month)   
            
            print("------------------------------------------")
            print(f"Country: {country}")
            print(f"Month: {month}")
            print(f"Traditional Season: {season}")
         



        elif choice == "3":
                print("\n--- Compare Seasons of Two Countries ---")
                country1 = input("Enter first country: ").strip()
                country2 = input("Enter second country: ").strip()
                month = input("Enter month: ").strip()

                print("------------------------------------------")
                check_seasons_same(country1, country2, month)
        
        
        elif choice == "4":
            print("\n--- Check City Temperature ---")
            city = input("Enter city (Perth/Adelaide/Brisbane): ").strip()
            
            try:
                temp = float(input("Enter temperature (°C): "))
                time = input("Enter time (morning/afternoon): ").strip().lower()
                
                result = check_city_temperature(city, temp, time)
                
                print("------------------------------------------")
                print(result)
                
                
            except ValueError:
                print("------------------------------------------")
                print("\nError: Please enter a valid number for temperature.")
        


        elif choice == "5":
            print("\n--- Compare Temperature with Perth ---")
            city = input("Enter city (Perth/Adelaide/Brisbane): ").strip()
            
            try:
                temp = float(input("Enter temperature (°C): "))
                time = input("Enter time (morning/afternoon): ").strip().lower()
                
                result = compare_with_perth(city, temp, time)
                
                print("------------------------------------------")
                print(result)
                
                
            except ValueError:
                print("------------------------------------------")
                print("\nError: Please enter a valid number for temperature.")
        
       

        elif choice == "6":
            print("-------------------------------------------")
            print("Thank you for using the Educational Software Tool!")
            print("Goodbye!")
            break
        else:
            print("\nError: Invalid choice. Please enter 1-6.")

        
        input("\nPress Enter to continue...")



if __name__ == "__main__":
    main()