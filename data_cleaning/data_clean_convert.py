import pandas as pd
import os
import argparse
from .. import set_log


def create_data_file(file_name, df):
    csv_file = file_name.replace(".xlsx", ".csv")
    folder = "datalake"
    os.makedirs(folder, exist_ok=True)
    csv_path = os.path.join(folder, csv_file)
    df.columns = ["نماد", "نام", "تعداد", "حجم", "ارزش", "دیروز", "اولین", "آخرین معامله - مقدار",
                "آخرین معامله - تغییر", "آخرین معامله - درصد", "قیمت پایانی - مقدار", "قیمت پایانی - تغییر",
                "قیمت پایانی - درصد", "کمترین", "بیشترین"]
    df.drop([0, 1], axis=0, inplace=True)
    df.to_csv(csv_path, index=False)
    set_log.info_logger.info(f"{file_name} converted to {csv_file} and saved in {os.path.join(os.getcwd(), folder)}")


def clean_convert_file(stage_path, save_excel):
    try:
        for file_name in os.listdir(stage_path):
            if file_name.endswith(".xlsx"):
                file_path = os.path.join(stage_path, file_name)
                df = pd.read_excel(file_path)
                if df.shape[0] <= 2:
                    os.remove(file_path)
                    set_log.info_logger.info(f"This file {file_name} is empty and was removed")
                else:
                    create_data_file(file_name, df)
                    if not save_excel:
                        os.remove(file_path)
                        set_log.info_logger.info(f"{file_name} removed after CSV conversion")
    except Exception as e:
        set_log.error_logger.error(f"Error cleaning and converting files: {str(e)}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("stage_path", type=str, help="Path to the stage folder")
    parser.add_argument("save_excel", type=int, help="Keep the initial Excel files (1: save, 0: remove)")
    args = parser.parse_args()
    clean_convert_file(args.stage_path, args.save_excel)


if __name__ == "__main__":
    main()
