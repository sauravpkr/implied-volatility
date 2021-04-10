from flask import Flask,jsonify
from flask_restful import Api,Resource
import schedule
from flask_apscheduler import APScheduler
from iv import pull_iv
from flask_sqlalchemy import SQLAlchemy
import threading
import market_data


app= Flask(__name__)
api=Api(app)
scheduler=APScheduler()

stock_data = ["ACC","ADANIENT","ADANIPORTS","AMARAJABAT","AMBUJACEM","APOLLOHOSP","APOLLOTYRE","ASHOKLEY","ASIANPAINT","AUROPHARMA","AXISBANK","BAJAJ-AUTO","BAJAJFINSV","BAJFINANCE","BALKRISIND","BANDHANBNK","BANKBARODA","BATAINDIA","BEL","BERGEPAINT","BHARATFORG","BHARTIARTL","BHEL","BIOCON","BOSCHLTD","BPCL","BRITANNIA","CADILAHC","CANBK","CENTURYTEX","CHOLAFIN","CIPLA","COALINDIA","COLPAL","CONCOR","CUMMINSIND","DABUR","DIVISLAB","DLF","DRREDDY","EICHERMOT","EQUITAS","ESCORTS","EXIDEIND","FEDERALBNK","GAIL","GLENMARK","GMRINFRA","GODREJCP","GODREJPROP","GRASIM","HAVELLS","HCLTECH","HDFC","HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDPETRO","HINDUNILVR","IBULHSGFIN","ICICIBANK","ICICIPRULI","IDEA","IDFCFIRSTB","IGL","INDIGO","INDUSINDBK","INFRATEL","INFY","IOC","ITC","JINDALSTEL","JSWSTEEL","JUBLFOOD","JUSTDIAL","KOTAKBANK","L&TFH","LICHSGFIN","LT","LUPIN","M&M","M&MFIN","MANAPPURAM","MARICO","MARUTI","MCDOWELL-N","MFSL","MGL","MINDTREE","MOTHERSUMI","MRF","MUTHOOTFIN","NATIONALUM","NAUKRI","NCC","NESTLEIND","NIITTECH","NMDC","NTPC","ONGC","PAGEIND","PEL","PETRONET","PFC","PIDILITIND","PNB","POWERGRID","PVR","RAMCOCEM","RBLBANK","RECLTD","RELIANCE","SAIL","SBILIFE","SBIN","SHREECEM","SIEMENS","SRF","SRTRANSFIN","SUNPHARMA","SUNTV","TATACHEM","TATACONSUM","TATAMOTORS","TATAPOWER","TATASTEEL","TCS","TECHM","TITAN","TORNTPHARM","TORNTPOWER","TVSMOTOR","UBL","UJJIVAN","ULTRACEMCO","UPL","VEDL","VOLTAS","WIPRO","ZEEL"]
indices_data = ['NIFTY', 'NIFTYIT', 'BANKNIFTY']

thread_list=[]
for securities in indices_data:
    
    try:
        thread_obj= threading.Thread(target=pull_iv,args=(securities,))
        thread_list.append(thread_obj)
    except:
        print("error in creating thread")

for thread_list_item in thread_list:
    thread_list_item.join()








if __name__ == "__main__":
    app.run(debug=True)
    
     