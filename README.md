# Automatas-Gramaticas

## Project Description

This repository contains Python scripts developed as part of the final exam for the "Automata and Grammars" course. The scripts are designed to analyze session time data of users within a specified date range from a given Excel file.

## Contents

- **FileControl.py**: This script provides functions for opening and exporting Excel files.
- **UserManager.py**: This script includes functions related to managing user data, such as searching for users based on input criteria.
- **SessionTime.py**: Here, functions are implemented to calculate session times based on specified date ranges.

## Usage

### Requirements
- Python 3.x
- Pandas library
- tkinter library (for GUI interaction)

### Running the Scripts

1. **FileControl.py**: Handles file operations.
   - `open_file(filename, sheetname)`: Opens the specified Excel file and returns its data.
   - `export_file(username, start_date, end_date, session_time)`: Exports the search results to a new Excel file.

2. **UserManager.py**: Manages user data.
   - `search_usuario(username, data)`: Searches for the specified username in the provided data.

3. **SessionTime.py**: Computes session times.
   - `RegexFecha(date)`: Validates the input date format.
   - `sum_session_time(data, start_date, end_date)`: Calculates the total session time for a user within the specified date range.

### Workflow

1. Run the main script `main.py`.
2. Enter the filename and sheetname of the Excel file you want to analyze.
3. Choose a user from the displayed list.
4. Input the start and end dates for the analysis.
5. View the total session time for the selected user within the specified date range.
6. Optionally, export the search results to an Excel file.
7. Choose whether to perform another search or exit the program.

## Contributors

- Luca Terranova


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
