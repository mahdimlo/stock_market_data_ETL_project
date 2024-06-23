from data_extraction.data_download import read_and_write_data
from data_cleaning.data_clean_convert import clean_convert_file
from data_analysis.data_analysis import Analyze
import set_log
import argparse
from jdatetime import datetime as jdatetime


def main():
    parser = argparse.ArgumentParser()
    try:
        parser.add_argument("start_date", type=str, help="'Start date in YYYY-MM-DD format (Shamsi)'")
        parser.add_argument("end_date", type=str, help="End date in YYYY-MM-DD format (Shamsi)")
    
        parser.add_argument("stage_path", type=str, help="Path to the stage folder")
        parser.add_argument("save_excel", type=int, help="Keep the initial Excel files (1: save, 0: remove)")
        args = parser.parse_args()
        
        start_date_jalali = jdatetime.strptime(args.start_date, "%Y-%m-%d")
        end_date_jalali = jdatetime.strptime(args.end_date, "%Y-%m-%d")

    except Exception as e:
        set_log.error_logger.error(f"Please enter the correct date: {str(e)}")

    
    try:
        read_and_write_data(start_date_jalali.date(), end_date_jalali.date())
        set_log.info_logger.info("The data was downloaded and saved correctly")
    except Exception as e:
        set_log.error_logger.error(f"There is a problem in downloading and saving data: {str(e)}")

    try:
        clean_convert_file(args.stage_path, args.save_excel)
        set_log.info_logger.info("Data conversion and cleaning was done correctly")
    except Exception as e:
        set_log.error_logger.error(f"Data conversion and cleaning were done correctly: {str(e)}")
    
    try:
        analyze = Analyze()
        analyze.set_read_data()
        analyze.set_merge_data()
        analyze.get_largest_valume_of_transactions()
        analyze.get_highest_average_price()
        analyze.get_lowest_average_price()
        analyze.get_highest_price()
        analyze.get_lowest_price()
        set_log.info_logger.info("The analyzes were performed correctly")
    except Exception as e:
        set_log.error_logger.error(f"The analysis process went wrong: {str(e)}")


if __name__ == "__main__":
    main()
