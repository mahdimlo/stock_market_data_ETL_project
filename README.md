# Stock Market Data ETL Project
## Introduction
The Stock Market Data ETL (Extract, Transform, Load) Project automates the process of downloading, cleaning, converting, and analyzing stock market data. It fetches data from the TSETMC website, processes it to remove empty files and convert Excel files to CSV format, and then performs various analyses on the cleaned data to extract valuable insights about market transactions.
## Tools Used
- __Python:__ The primary programming language used for the project.
- __pandas:__ Used for data manipulation and analysis.
- __argparse:__ Handles command-line arguments.
- __requests:__ Fetches data from the web.
- __jdatetime:__ Manages and converts Jalali (Shamsi) dates.
- __logging:__ Logs information and errors for debugging and tracking.
- __openpyxl:__ Reads and writes Excel files.

## Code Explanation
### data_download.py
This script downloads stock market data files from the TSETMC website based on a given date range.
- __create_file_and_read_data(response, date_file):__ Saves the downloaded data to the 'stage' folder.
- __download_data(start, end):__ Iterates through the given date range, downloading and saving data for weekdays.
- __main():__ Parses command-line arguments for start and end dates, and initiates the data download process.

### data_clean_convert.py
This script cleans and converts the downloaded Excel files to CSV format.
- __create_data_file(file_name, df):__ Converts an Excel file to CSV format and saves it to the 'datalake' folder.
- __clean_convert_files(stage_path, save_excel):__ Cleans the data by removing empty files and converts the remaining files to CSV format.
- __main():__ Parses command-line arguments for the stage folder path and whether to keep the original Excel files, then initiates the cleaning and conversion process.

### data_analysis.py
This script analyzes the cleaned data to extract insights such as the largest volume of transactions, highest and lowest average price changes, and highest and lowest prices.
- __Analyze class:__ Contains methods for reading, merging, and analyzing the data.
    - __set_read_data():__ Reads all CSV files from the 'datalake' folder.
    - __set_merge_data():__ Merges the read data into a single DataFrame.
    - __get_largest_volume_of_transactions():__ Finds the top 10 stocks with the highest trading volume.
    - __get_highest_average_price():__ Finds the stock with the highest average price change.
    - __get_lowest_average_price():__ Finds the stock with the lowest average price change.
    - __get_highest_price():__ Finds the stock with the highest price.
    - __get_lowest_price():__ Finds the stock with the lowest price.
- __main():__ Initiates the analysis process.

### set_log.py
This script sets up logging for the project.
- __error_logger:__ Logs error messages.
- __info_logger:__ Logs informational messages.

### main.py
This script orchestrates the entire process, from data extraction to cleaning, conversion, and analysis.
- __main():__ Parses command-line arguments for date range, stage folder path, and Excel file retention, then executes the data extraction, cleaning, conversion, and analysis processes in sequence.

## Command Line Arguments
### main.py
The main script takes the following command-line arguments:
- __start_date:__ The start date for data extraction in Jalali (Shamsi) calendar format (e.g., 1402-01-01).
- __end_date:__ The end date for data extraction in Jalali (Shamsi) calendar format (e.g., 1402-01-10).
- __stage_path:__ The directory path where the downloaded Excel files will be saved before conversion (e.g., 'stage').
- __save_excel:__ An integer flag indicating whether to keep the original Excel files after conversion (1 to keep, 0 to remove).

Example:
```
python main.py 1402-01-01 1402-01-10 stage 1
```
This command will:
1. Download stock market data from the TSETMC website for the date range from 1402-01-01 to 1402-01-10.
2. Save the downloaded data to the 'stage' folder.
3. Clean and convert the data to CSV format, saving the converted files to the 'datalake' folder.
4. Perform various analyses on the cleaned data and log the results.

## Project Setup and Execution
1. __Set Up Environment:__ Ensure you have Python installed and set up a virtual environment.
2. __Install Dependencies:__ Run the following command to install the necessary packages:
  ```
  pip install -r requirements.txt
  ```
3. __Download Data, Clean, Convert, and Analyze:__ Execute the main script with the necessary arguments to download data, clean and convert it, and perform the analysis. For example:
  ```
  python main.py 1402-01-01 1402-01-10 stage 1
  ```
4. __Check Logs:__ Review info.log and error.log for detailed logs and any errors encountered during execution.

This documentation provides a clear and comprehensive guide to understanding, running, and maintaining the Stock Market Data ETL Project.
