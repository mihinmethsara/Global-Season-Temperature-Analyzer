def get_meteorological_season(country, month):

   #module 1 find season for country and month with given figure1 png

     #remove extra spaces and fix capital letters first letter change
    country = str(country).strip().title()
    
     
      #check if month number or text
    if isinstance(month, (int, float)):
        month_str = str(int(month)).strip()

    else:
         month_str = str(month).strip().title()


       #change month number to month name

    month_numbers = {
        "1": "January", "2": "February", "3": "March", "4": "April",
        "5": "May", "6": "June", "7": "July", "8": "August",
        "9": "September", "10": "October", "11": "November", "12": "December",
        "01": "January", "02": "February", "03": "March", "04": "April",
         "05": "May", "06": "June", "07": "July", "08": "August", "09": "September"
    }

    if month_str in month_numbers:
       month_str = month_numbers[month_str]

      #store season details for countries

    season_data = {
        
        "Australia": {
            "Summer": ["December", "January", "February"],
            "Autumn": ["March", "April", "May"],
            "Winter": ["June", "July", "August"],
             "Spring": ["September", "October", "November"]
        },



        "Sri Lanka": {
            "Northeast Monsoon": ["December","January","February"],
            "Inter-monsoon": ["March","April","October","November"],
             "Southeast Monsoon": ["May","June","July","August","September"]
        },


        "Japan": {
            "Winter": ["December", "January", "February"],
            "Spring": ["March", "April", "May"],
            "Summer": ["June", "July", "August"],
             "Autumn": ["September", "October", "November"]
        },


        "Mauritius": {
            "Summer": ["November","December","January","February","March","April"],
            "Autumn": ["May"],
            "Winter": ["June","July","August","September"],
            "Spring": ["October"]
        },


        "Malaysia": {
            "Northeast Monsoon": ["December","January","February"],
             "Inter-monsoon": ["March","April","October","November"],
            "Southeast Monsoon": ["May","June","July","August","September"]
        },
        
        
        "Spain": {
            "Winter": ["December", "January", "February"],
            "Spring": ["March", "April", "May"],
            "Summer": ["June", "July", "August"],
            "Autumn": ["September", "October", "November"]
        }, 
    }


    if country not in season_data:  #check country valid
        return "Invalid country"


    for season_name, month_list in season_data[country].items(): #find matching season and give
        if month_str in month_list:
          return season_name

    return "Invalid month" 



def get_traditional_season(country, month):
     #module 2 find traditional noongar season for australia from figure1


    country = str(country).strip().title() 
    
     

    if isinstance(month, (int, float)):
        month_str = str(int(month)).strip()
    else:
        month_str = str(month).strip().title()


    month_numbers = {
        
        "1": "January", "2": "February", "3": "March", "4": "April",
        "5": "May", "6": "June", "7": "July", "8": "August",
        "9": "September", "10": "October", "11": "November", "12": "December",
         "01": "January", "02": "February", "03": "March", "04": "April",
        "05": "May", "06": "June", "07": "July", "08": "August", "09": "September"
    }

    if month_str in month_numbers:
       month_str = month_numbers[month_str]


       #store noongar traditional seasons from figure1
    noongar_seasons = {

        "Birak": ["December", "January"],
        "Bunuru": ["February", "March"],
        "Djeran": ["April", "May"],
        "Makuru": ["June", "July"],
        "Djilba": ["August", "September"],
         "Kambarang": ["October", "November" ]
    }


      #check if country is australia becauce  australia only have traditional seasons
    if country != "Australia":
        return "No traditional season for this country"
    

       #find matching season and return

    for season_name, valid_months in noongar_seasons.items():
        if month_str in valid_months:
            return season_name


     #if month not match any season
    return "No traditional season for this month" 