from market_data import *
import datetime
import time
import database_operation

def market_status_job():
    market_status_api()
    print(marketStatus)

def market_data_job():
    data = get_stock_data('NIFTY')
    insert_data_into_database(data)







if __name__ == "__main__":
    market_data_job()
    