# Global Season & Temperature Analyzer


## Overview

A Python command line application for analyzing seasons and temperatures across different countries and cities. The system compares meteorological seasons, Indigenous Australian (Noongar) seasons, and city temperature data, with menu based analysis and file output features for users and testers.

## Features

| **Category**                     | **Description**                                        |
| --------------------------------- | ------------------------------------------------------- |
| **Meteorological season lookup**  | Find the season for a country and month.                |
| **Traditional season lookup**     | Find the Noongar season for Australia.                  |
| **Compare seasons**               | Compare seasons of two countries for a month.            |
| **Save comparison to File**       | Save the season comparison result to a text file.        |
| **City temperature Check**        | Check a city's temperature with average temperatures.    |
| **Compare with Perth**            | Compare a city's temperature with Perth's average.       |
| **Data storage**                  | Store season and temperature data in a data module.      |

## Class Structure

**Global Season & Temperature Analyzer**

```
├── 📄 main.py                 - Main program and menu
├── 📄 data.py                 - Season, city, and temperature data
├── 📄 input_validator.py      - Input checking and validation
├── 📄 season_finder.py        - Finds meteorological and traditional seasons
├── 📄 season_comparator.py    - Compares seasons and saves results
├── 📄 temperature_analyzer.py - Checks city temperatures against averages
└── 📄 perth_comparator.py     - Compares temperatures with Perth
```

## Compilation and Execution

### Prerequisites
- Python 3.10 or newer
- `pytest` (for running the tests)

### Steps to Run

1. **Clone or download the repository**:
   
2. **Navigate to the code directory**:
```bash
cd code
```

3. **Run the Application**:
```bash
python main.py 
```

4. **Use the menu: Choose an option from 1–7 and follow the instructions.**

5. **Run the tests** (if not install test framework first install it and test):
```bash
pip install pytest
```
```bash
pytest -v
```

## Data Validation

The application checks and validates user input before processing to avoid incorrect results.

The application uses input validation for:

- **Country**: Must be one of the supported countries (Australia, Sri Lanka, Japan, Mauritius, Malaysia, Spain)
- **Month**: Accepts full month name or numeric value (1–12), it case insensitive
- **City**: Must be one of the supported cities (Perth, Adelaide, Brisbane)
- **Time of Day**: Must be `"morning"` or `"afternoon"` (case insensitive)
- **Temperature**: Must be a valid number within each city's historical min/max range


## Checklist of Completed Functionalities

**All the features and functionalities of the Global Season & Temperature Analyzer are working**

- Design Requirements

- Program Functionalities

    - [x] Find Meteorological Season

    - [x] Find Traditional Season (Australia only)

    - [x] Compare Seasons of Two Countries

    - [x] Compare Seasons and Save to File

    - [x] Check City Temperature

    - [x] Compare Temperature with Perth

    - [x] Exit the Program

- File Handling

    - [x] Writing comparison results to output text file 

- Error Handling and Data Validation

- Menu and User interface

- Unit Testing

    - [x] Equivalence Partitioning tests

    - [x] Boundary Value Analysis tests

    - [x] White-box path/branch tests

## Technical Specifications

- **Programming Language**: Python
- **Paradigm**: Modular design
- **Data Structures**: Dictionary and list use for store data
- **Testing Framework**: `pytest` (65 tests done)
- **Input Validation**: Input checking and error handling

## Error Handling

- **Input Mismatch**: Handles incorrect data types such as non-numeric temperatures.
- **Invalid Country / City / Month**: Shows clear error messages for invalid inputs.
- **Out-of-Range Temperature**: Checks temperatures outside the expected range and report it.
- **File Operations**: Safely saves comparison results to a file.

## Testing Approach

This project uses a structured approach to software testing:

- **Equivalence Partitioning** — testing values from valid and invalid groups.
- **Boundary Value Analysis** — testing edge values 
- **White-Box Testing** — Checking  program's internal branches, loops, and exception paths

All test cases are documented and traceable in the project report(inside document folder).

## Project Compliance

- [x] Modular design with clear separation of concerns

- [x] Comprehensive input validation

- [x] File I/O for result output

- [x] Full unit test coverage (EP, BVA, WB)

- [x] Git version control with feature branching workflow

## Development Notes

- Developed using a feature branch git workflow (`feature/season`, `feature/temperature`, `feature/refactoring`, `feature/testing`, `feature/documentation`)
- Merged into `develop`, then finalized into `main`
- Traceability matrix included in project documentation(it inside document folder)

## Author

- Mihin Methsara Prathapasinghe

