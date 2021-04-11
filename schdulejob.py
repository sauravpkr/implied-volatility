from market_data import *
import datetime
import time
import database_operation

def market_status_job():
    market_status_api()
    print(marketStatus)

def market_data_job():
    if marketStatus == 'Open':
        data = get_stock_data('NIFTY')
        insert_data_into_database(data)
    else:
        time.sleep(10)
        print("not open")

    







if __name__ == "__main__":
    market_data_job()
    