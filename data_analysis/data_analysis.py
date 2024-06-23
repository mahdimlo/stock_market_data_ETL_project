import pandas as pd
import os
from .. import set_log


class Analyze:
    def __init__(self):
        self.df_list = []
        self.path = "datalake"
        self.df_merged = pd.DataFrame()

    def set_read_data(self):
        try:
            for file_name in os.listdir(self.path):
                if file_name.endswith(".csv"):
                    file_path = os.path.join(self.path, file_name)
                    df = pd.read_csv(file_path)
                    self.df_list.append(df)
                    set_log.info_logger.info(f"This {file_name} was read and added to the list")
        except Exception as e:
            set_log.error_logger.error(f"We encountered a problem reading the files: {str(e)}")

    def set_merge_data(self):
        try:
            self.df_merged = pd.concat([df for df in self.df_list], ignore_index=True)
            set_log.info_logger.info("All the data in the list are merged together")
        except Exception as e:
            set_log.error_logger.error(f"We encountered a problem while merging the data: {str(e)}")

    def get_largest_valume_of_transactions(self):
        try:
            largest_valume = {}
            volum_of_transactions = self.df_merged.groupby("نماد")["حجم"].sum()
            largest_valume = volum_of_transactions.nlargest(10)
            set_log.info_logger.info(f"Ten of the best stocks in terms of trading volume:\n {pd.DataFrame(largest_valume)}")
        except Exception as e:
            set_log.error_logger.error(f"We encountered a problem in calculating the volume of transactions: {str(e)}")

    def get_highest_average_price(self):
        try:
            average_price = self.df_merged.groupby("نماد")["قیمت پایانی - تغییر"].mean()
            set_log.info_logger.info(f"The highest average price change in this period:\n symbol: {average_price.idxmax()} | average price change: {average_price.max()}")
        except Exception as e:
            set_log.error_logger.error(f"We encountered a problem in calculating the average price change: {str(e)}")
    
    def get_lowest_average_price(self):
        try:
            average_price = self.df_merged.groupby("نماد")["قیمت پایانی - تغییر"].mean()
            set_log.info_logger.info(f"The lowest average price change in this period:\n symbol: {average_price.idxmin()} | average price change: {average_price.min()}")
        except Exception as e:
            set_log.error_logger.error(f"We encountered a problem in calculating the average price change: {str(e)}")

    def get_highest_price(self):
        try:
            highest_price = self.df_merged.groupby("نماد")["بیشترین"].max()
            set_log.info_logger.info(f"The highest price in this range:\n symbol: {highest_price.idxmax()} | highest price: {highest_price.max()}")
        except Exception as e:
            set_log.error_logger.error(f"We have a problem in calculating the highest price: {str(e)}")
    
    def get_lowest_price(self):
        try:
            lowest_price = self.df_merged.groupby("نماد")["کمترین"].min()
            set_log.info_logger.info(f"The highest price in this range:\n symbol: {lowest_price.idxmin()} | lowest price: {lowest_price.min()}")
        except Exception as e:
            set_log.error_logger.error(f"We have a problem in calculating the lowest price: {str(e)}")



def main():
    analyze = Analyze()
    analyze.set_read_data()
    analyze.set_merge_data()
    analyze.get_largest_valume_of_transactions()
    analyze.get_highest_average_price()
    analyze.get_lowest_average_price()
    analyze.get_highest_price()
    analyze.get_lowest_price()


if __name__ == "__main__":
    main()
