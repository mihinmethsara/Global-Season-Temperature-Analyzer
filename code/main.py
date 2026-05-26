import season_finder
import season_comparator
import temperature_analyzer
import perth_comparator



def main():

    print("\n-------------------------------------------")
    print("      Educational Software Tool - Menu")
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
            # Module 1: Find meteorological season
            print("\n--- Find Meteorological Season ---")
            country = input("Enter country name: ").strip()
            month = input("Enter month (name or number): ").strip()
            season = season_finder.get_meteorological_season(country, month)

            print("\n-----------------------------------")
            print(f"Country: {country}")
            print(f"Month: {month}")
            print(f"Meteorological Season: {season}")
            print("-----------------------------------")




        elif choice == "2":
            #find traditional season for australia

            print("\n--- Find traditional season ---")
            country = input("Enter country name: ").strip()
            month = input("Enter month (name or number): ").strip()
            season = season_finder.get_traditional_season(country, month)


            print("\n-----------------------------------")
            print(f"Country: {country}")
            print(f"Month: {month}")
            print(f"Traditional Season: {season}")
            print("-----------------------------------")




        elif choice == "3":
            #compare seasons between countrie

            print("\n--- Compare seasons of two countries ---")
            country1 = input("Enter first country: ").strip()
            country2 = input("Enter second country: ").strip()
            month = input("Enter month: ").strip()
            print("------------------------------------------")
            season_comparator.check_seasons_same(country1, country2, month)



        elif choice == "4":
             #check city temperature against averages

            print("\n--- Check city temperature ---")
            city = input("Enter city (Perth/Adelaide/Brisbane): ").strip()

            try:
                temp = float(input("Enter temperature (°C): "))
                time = input("Enter time (morning/afternoon): ").strip().lower()
                result = temperature_analyzer.check_city_temperature(city, temp, time)
                print("------------------------------------------")
                print(result)

            except ValueError:
                print("------------------------------------------")
                print("Error: Please enter a valid number for temperature.")


        elif choice == "5":
             #compare temperature with Perth

            print("\n--- Compare temperature with Perth ---")
            city = input("Enter city (Perth/Adelaide/Brisbane): ").strip()

            try:
                temp = float(input("Enter temperature (°C): "))
                time = input("Enter time (morning/afternoon): ").strip().lower()
                result = perth_comparator.compare_with_perth(city, temp, time)
                print("------------------------------------------")
                print(result)
                
            except ValueError:
                print("------------------------------------------")
                print("Error: Please enter a valid number for temperature.")


        elif choice == "6":
             #exit program

            print("-------------------------------------------")
            print("Thank you for using the educational softwar!")
            print("Goodbye!")
            break

        else:
            print("\nError: Invalid choice. Please enter 1-6.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()