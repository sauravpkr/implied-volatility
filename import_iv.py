import requests
import json


stock_data = ["ACC","ADANIENT","ADANIPORTS","AMARAJABAT","AMBUJACEM","APOLLOHOSP","APOLLOTYRE","ASHOKLEY","ASIANPAINT","AUROPHARMA","AXISBANK","BAJAJ-AUTO","BAJAJFINSV","BAJFINANCE","BALKRISIND","BANDHANBNK","BANKBARODA","BATAINDIA","BEL","BERGEPAINT","BHARATFORG","BHARTIARTL","BHEL","BIOCON","BOSCHLTD","BPCL","BRITANNIA","CADILAHC","CANBK","CENTURYTEX","CHOLAFIN","CIPLA","COALINDIA","COLPAL","CONCOR","CUMMINSIND","DABUR","DIVISLAB","DLF","DRREDDY","EICHERMOT","EQUITAS","ESCORTS","EXIDEIND","FEDERALBNK","GAIL","GLENMARK","GMRINFRA","GODREJCP","GODREJPROP","GRASIM","HAVELLS","HCLTECH","HDFC","HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDPETRO","HINDUNILVR","IBULHSGFIN","ICICIBANK","ICICIPRULI","IDEA","IDFCFIRSTB","IGL","INDIGO","INDUSINDBK","INFRATEL","INFY","IOC","ITC","JINDALSTEL","JSWSTEEL","JUBLFOOD","JUSTDIAL","KOTAKBANK","L&TFH","LICHSGFIN","LT","LUPIN","M&M","M&MFIN","MANAPPURAM","MARICO","MARUTI","MCDOWELL-N","MFSL","MGL","MINDTREE","MOTHERSUMI","MRF","MUTHOOTFIN","NATIONALUM","NAUKRI","NCC","NESTLEIND","NIITTECH","NMDC","NTPC","ONGC","PAGEIND","PEL","PETRONET","PFC","PIDILITIND","PNB","POWERGRID","PVR","RAMCOCEM","RBLBANK","RECLTD","RELIANCE","SAIL","SBILIFE","SBIN","SHREECEM","SIEMENS","SRF","SRTRANSFIN","SUNPHARMA","SUNTV","TATACHEM","TATACONSUM","TATAMOTORS","TATAPOWER","TATASTEEL","TCS","TECHM","TITAN","TORNTPHARM","TORNTPOWER","TVSMOTOR","UBL","UJJIVAN","ULTRACEMCO","UPL","VEDL","VOLTAS","WIPRO","ZEEL"]
indices_data = ['NIFTY', 'NIFTYIT', 'BANKNIFTY']
cookies=  "977E0247365692D2A9075FFCB57548AD~2Lkkb7B4CGYq4IoDwtc9YxecAplXUEilUnSDbNpOB+vHnWn7FkmjSLLCnb2Dk4UdkLfUa82KfJyPYaB5nljwoYu6Yhlhev4UrLgJHgKNA7olHYVHnHRPG1+tDI2NDPcrJUy8L2vZIJxr4TfejOTM6tRj8jr/mpztalDrlhNcRGA"
url_stock=  "https://www.nseindia.com/api/option-chain-equities?symbol=SBIN"
url_indices= "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
api_headers= {"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36","cookie":cookies}

def pull_iv(securities):
    response = requests.get(url,headers=api_headers)
    json_data=json.loads(response.text)
    filtered_data= json_data['filtered']['data']
    
    if securities in stock_data:
        url=  "https://www.nseindia.com/api/option-chain-equities?symbol="+ securities
    elif securities in indices_data:
        url = "https://www.nseindia.com/api/option-chain-indices?symbol=" + securities
    
    for x in filtered_data:
        print(x)
    

if __name__ == "__main__":
    pull_iv('NIFTY')