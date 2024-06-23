import argparse
import requests
import os
from jdatetime import datetime as jdatetime
from jdatetime import timedelta
from .. import set_log


def create_file_and_read_data(response, date_file):
    folder = "stage"
    file = f"MarketWatchPlus-{str(date_file)}.xlsx"
    try:
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, file), 'wb') as data:
            data.write(response.content)
        set_log.info_logger.info(f"{file} was successfully downloaded and saved in {os.path.join(os.getcwd(), folder)}")
    except Exception as e:
        set_log.error_logger.error(f"Error saving file: {str(e)}")


def read_and_write_data(start, end):
    try:
        current_date = start
        while current_date <= end:
            if current_date.weekday() < 5:
                file_url  = f"http://members.tsetmc.com/tsev2/excel/MarketWatchPlus.aspx?d={str(current_date)}"
                response = requests.get(file_url)
                if response.status_code == 200:
                    create_file_and_read_data(response, current_date)
                else:
                    set_log.error_logger.error(f"Failed to download data for {str(current_date)}")
            else:
                set_log.info_logger.info(f"{str(current_date)}: This day is weekend")
            current_date += timedelta(days=1)
    except Exception as e:
        set_log.error_logger.error(f"Error downloading files: {str(e)}")


def main():
    parser = argparse.ArgumentParser()
    try:
        parser.add_argument("start_date", type=str, help="'Start date in YYYY-MM-DD format (Shamsi)'")
        parser.add_argument("end_date", type=str, help="End date in YYYY-MM-DD format (Shamsi)")
        args = parser.parse_args()
        
        start_date_jalali = jdatetime.strptime(args.start_date, "%Y-%m-%d")
        end_date_jalali = jdatetime.strptime(args.end_date, "%Y-%m-%d")
        read_and_write_data(start_date_jalali.date(), end_date_jalali.date())
    except Exception as e:
        set_log.error_logger.error(f"Please enter the correct date: {str(e)}")


if __name__ == "__main__":
    main()
