# season data from figure1

FOUR_SEASONS = {
    "Winter": ["December", "January", "February"],
    "Spring": ["March", "April", "May"],
    "Summer": ["June", "July", "August"],
    "Autumn": ["September", "October", "November"]
}


AUSTRALIAN_SEASONS = {
    "Summer": ["December", "January", "February"],
    "Autumn": ["March", "April", "May"],
    "Winter": ["June", "July", "August"],
    "Spring": ["September", "October", "November"]
}


MAURITIUS_SEASONS = {
    "Summer": ["November", "December", "January",
               "February", "March", "April"],
    "Autumn": ["May"],
    "Winter": ["June", "July", "August", "September"],
    "Spring": ["October"]
}


MONSOON_SEASONS = {
    "Northeast Monsoon": ["December", "January", "February"],
    "Inter-monsoon": ["March", "April", "October", "November"],
    "Southeast Monsoon": [
        "May", "June", "July",
        "August", "September"
    ]
}


# country season data

SEASON_DATA = {

    "Australia": AUSTRALIAN_SEASONS,

    "Sri Lanka": MONSOON_SEASONS,

    "Japan": FOUR_SEASONS,  # reused same seasons no duplicate

    "Mauritius": MAURITIUS_SEASONS,

    "Malaysia": MONSOON_SEASONS,

    "Spain": FOUR_SEASONS
}


NOONGAR_SEASONS = {

    "Birak": ["December", "January"],
    "Bunuru": ["February", "March"],
    "Djeran": ["April", "May"],
    "Makuru": ["June", "July"],
    "Djilba": ["August", "September"],
     "Kambarang": ["October", "November"]
}


# temperature data from figure2

CITY_AVERAGES = {
    "Perth": {"morning": 18.2, "afternoon": 23.0},
    "Adelaide": {"morning": 16.5, "afternoon": 21.0},
    "Brisbane": {"morning": 21.8, "afternoon": 24.8}
}


CITY_RANGES = {
    "Perth": {"min": 0.7, "max": 46.0},
    "Adelaide": {"min": -1.0, "max": 49.0},
    "Brisbane": {"min": 2.6, "max": 41.7}
}


VALID_COUNTRIES = list(SEASON_DATA.keys())
VALID_CITIES = list(CITY_AVERAGES.keys())
VALID_TIMES = ["morning", "afternoon"]


VALID_MONTHS = {
    "January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December"
}


MONTH_NUMBER_TO_NAME = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}