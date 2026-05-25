## Module Descriptions

I identified three main modules for the season functionality following good modularity principles taught high cohesion and low coupling. Each module has a single, well-defined responsibility.

### Module1:

**Module Name:** `get_meteorological_season`

**Purpose:** Returns the meteorological season for a given country and month based on figure1.

**Imports:** 
- country(string taken to module with keyboard input)
- month(string or integer take directly whe function called with parameter passing)

**Exports:**
- Season name as string return value

**Behaviour:**  Finds the meteorological season for a given country and month based on Figure 1 and returns the season name. It uses a dictionary containing data(add to same code ) from figure 1 for six countries.Returns "Invalid country" or "Invalid month" for error cases.

**Dependencies:** None

**Exceptions:** Handles invalid inputs by returning error messages as strings instead of raising exceptions.This approach keeps the modules simple and easy to test.


### Module 2:

**Module name**: `get_traditional_season`

**Purpose:** Returns the traditional Noongar season for Australia based on figure1.

**Imports:** 
- country (string using parameter passing)
- month (string or integer using parameter passing)

**Exports:**
- Season name return string  or  retun message "no traditional season for this country" or "no traditional season for this month"

**Behaviour:** Finds the traditional Noongar season for Australia based on figure1 and returns the season name.

**Dependencies:** None

**Exceptions:** Handled by returning error messages.

### Module 3:

**Module Name:** `check_seasons_same`

**Purpose:** Compares meteorological seasons of two countries for a given month.

**Imports:** use parameter prassing with function 
- country1 and country2(string)
- month (string or integer)

**Exports:** 
- Boolean value return,true if same season,false if different or invalid 
- Prints comparison result 

**Behaviour:**  Uses module 1 to get meteorological seasons for both countries, compares them, and returns true if same season, false if different or invalid.

**Dependencies:** Module 1: get_meteorological_season

**Exceptions:** Handles invalid inputs by returning false and printing error messages instead of raising exceptions. This approach keeps the module simple and easy to test.

