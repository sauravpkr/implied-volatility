import requests
import json


def get_stock_data(securities):
    cookies=  "977E0247365692D2A9075FFCB57548AD~2Lkkb7B4CGYq4IoDwtc9YxecAplXUEilUnSDbNpOB+vHnWn7FkmjSLLCnb2Dk4UdkLfUa82KfJyPYaB5nljwoYu6Yhlhev4UrLgJHgKNA7olHYVHnHRPG1+tDI2NDPcrJUy8L2vZIJxr4TfejOTM6tRj8jr/mpztalDrlhNcRGA"
    #url_stock=  "https://www.nseindia.com/api/option-chain-equities?symbol=SBIN"
    #url_indices= "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
    api_headers= {"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36","cookie":cookies}
    
    stock_data = ["ACC","ADANIENT","ADANIPORTS","AMARAJABAT","AMBUJACEM","APOLLOHOSP","APOLLOTYRE","ASHOKLEY","ASIANPAINT","AUROPHARMA","AXISBANK","BAJAJ-AUTO","BAJAJFINSV","BAJFINANCE","BALKRISIND","BANDHANBNK","BANKBARODA","BATAINDIA","BEL","BERGEPAINT","BHARATFORG","BHARTIARTL","BHEL","BIOCON","BOSCHLTD","BPCL","BRITANNIA","CADILAHC","CANBK","CENTURYTEX","CHOLAFIN","CIPLA","COALINDIA","COLPAL","CONCOR","CUMMINSIND","DABUR","DIVISLAB","DLF","DRREDDY","EICHERMOT","EQUITAS","ESCORTS","EXIDEIND","FEDERALBNK","GAIL","GLENMARK","GMRINFRA","GODREJCP","GODREJPROP","GRASIM","HAVELLS","HCLTECH","HDFC","HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDPETRO","HINDUNILVR","IBULHSGFIN","ICICIBANK","ICICIPRULI","IDEA","IDFCFIRSTB","IGL","INDIGO","INDUSINDBK","INFRATEL","INFY","IOC","ITC","JINDALSTEL","JSWSTEEL","JUBLFOOD","JUSTDIAL","KOTAKBANK","L&TFH","LICHSGFIN","LT","LUPIN","M&M","M&MFIN","MANAPPURAM","MARICO","MARUTI","MCDOWELL-N","MFSL","MGL","MINDTREE","MOTHERSUMI","MRF","MUTHOOTFIN","NATIONALUM","NAUKRI","NCC","NESTLEIND","NIITTECH","NMDC","NTPC","ONGC","PAGEIND","PEL","PETRONET","PFC","PIDILITIND","PNB","POWERGRID","PVR","RAMCOCEM","RBLBANK","RECLTD","RELIANCE","SAIL","SBILIFE","SBIN","SHREECEM","SIEMENS","SRF","SRTRANSFIN","SUNPHARMA","SUNTV","TATACHEM","TATACONSUM","TATAMOTORS","TATAPOWER","TATASTEEL","TCS","TECHM","TITAN","TORNTPHARM","TORNTPOWER","TVSMOTOR","UBL","UJJIVAN","ULTRACEMCO","UPL","VEDL","VOLTAS","WIPRO","ZEEL"]
    indices_data = ['NIFTY', 'NIFTYIT', 'BANKNIFTY']
    data=[]
    if securities in stock_data:
        url=  "https://www.nseindia.com/api/option-chain-equities?symbol="+ securities
    elif securities in indices_data:
        url = "https://www.nseindia.com/api/option-chain-indices?symbol=" + securities
    response = requests.get(url,headers=api_headers)
    json_data=json.loads(response.text)
    filtered_data= json_data['records']['data']  # filtered_data is of type Dict
    #print(filtered_data)
    return filtered_data


def market_status_api():
    market_status_api_url='https://www.nseindia.com/api/marketStatus'
    cookies=  "977E0247365692D2A9075FFCB57548AD~2Lkkb7B4CGYq4IoDwtc9YxecAplXUEilUnSDbNpOB+vHnWn7FkmjSLLCnb2Dk4UdkLfUa82KfJyPYaB5nljwoYu6Yhlhev4UrLgJHgKNA7olHYVHnHRPG1+tDI2NDPcrJUy8L2vZIJxr4TfejOTM6tRj8jr/mpztalDrlhNcRGA"
    api_headers= {"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36","cookie":cookies}
    response = requests.get(market_status_api_url,headers=api_headers)
    json_data=json.loads(response.text)
    market_status=json_data["marketState"][0]["marketStatus"]
    #market_status= market_status[0]
    return market_status

def pull_iv(securities):
    cookies=  "977E0247365692D2A9075FFCB57548AD~2Lkkb7B4CGYq4IoDwtc9YxecAplXUEilUnSDbNpOB+vHnWn7FkmjSLLCnb2Dk4UdkLfUa82KfJyPYaB5nljwoYu6Yhlhev4UrLgJHgKNA7olHYVHnHRPG1+tDI2NDPcrJUy8L2vZIJxr4TfejOTM6tRj8jr/mpztalDrlhNcRGA"
    #url_stock=  "https://www.nseindia.com/api/option-chain-equities?symbol=SBIN"
    #url_indices= "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
    api_headers= {"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36","cookie":cookies}



    stock_data = ["ACC","ADANIENT","ADANIPORTS","AMARAJABAT","AMBUJACEM","APOLLOHOSP","APOLLOTYRE","ASHOKLEY","ASIANPAINT","AUROPHARMA","AXISBANK","BAJAJ-AUTO","BAJAJFINSV","BAJFINANCE","BALKRISIND","BANDHANBNK","BANKBARODA","BATAINDIA","BEL","BERGEPAINT","BHARATFORG","BHARTIARTL","BHEL","BIOCON","BOSCHLTD","BPCL","BRITANNIA","CADILAHC","CANBK","CENTURYTEX","CHOLAFIN","CIPLA","COALINDIA","COLPAL","CONCOR","CUMMINSIND","DABUR","DIVISLAB","DLF","DRREDDY","EICHERMOT","EQUITAS","ESCORTS","EXIDEIND","FEDERALBNK","GAIL","GLENMARK","GMRINFRA","GODREJCP","GODREJPROP","GRASIM","HAVELLS","HCLTECH","HDFC","HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDPETRO","HINDUNILVR","IBULHSGFIN","ICICIBANK","ICICIPRULI","IDEA","IDFCFIRSTB","IGL","INDIGO","INDUSINDBK","INFRATEL","INFY","IOC","ITC","JINDALSTEL","JSWSTEEL","JUBLFOOD","JUSTDIAL","KOTAKBANK","L&TFH","LICHSGFIN","LT","LUPIN","M&M","M&MFIN","MANAPPURAM","MARICO","MARUTI","MCDOWELL-N","MFSL","MGL","MINDTREE","MOTHERSUMI","MRF","MUTHOOTFIN","NATIONALUM","NAUKRI","NCC","NESTLEIND","NIITTECH","NMDC","NTPC","ONGC","PAGEIND","PEL","PETRONET","PFC","PIDILITIND","PNB","POWERGRID","PVR","RAMCOCEM","RBLBANK","RECLTD","RELIANCE","SAIL","SBILIFE","SBIN","SHREECEM","SIEMENS","SRF","SRTRANSFIN","SUNPHARMA","SUNTV","TATACHEM","TATACONSUM","TATAMOTORS","TATAPOWER","TATASTEEL","TCS","TECHM","TITAN","TORNTPHARM","TORNTPOWER","TVSMOTOR","UBL","UJJIVAN","ULTRACEMCO","UPL","VEDL","VOLTAS","WIPRO","ZEEL"]
    indices_data = ['NIFTY', 'NIFTYIT', 'BANKNIFTY']
    data=[]
    PE=[]
    CE=[]
    if securities in stock_data:
        url=  "https://www.nseindia.com/api/option-chain-equities?symbol="+ securities
    elif securities in indices_data:
        url = "https://www.nseindia.com/api/option-chain-indices?symbol=" + securities
    response = requests.get(url,headers=api_headers)
    json_data=json.loads(response.text)
    filtered_data= json_data['records']['data']  # filtered_data is of type Dict
    for first_level in filtered_data:
        for second_level,x in first_level.items():
            if(second_level == 'PE'):
                PE.append(x)
                datalist1=[]
                for y ,y_item in x.items():
                    if(y == 'underlying'):
                        datalist1.insert(1,y_item)  
                    elif(y == 'identifier'):
                        datalist1.insert(0,y_item)      
                    elif(y == 'expiryDate'):
                        datalist1.insert(2,y_item)
                    elif(y == 'strikePrice'):
                        datalist1.insert(3,y_item)
                    elif(y == 'impliedVolatility'):
                        datalist1.insert(4,y_item)
                    elif(y == 'openInterest'):
                        datalist1.insert(5,y_item)
                datalist1= tuple(datalist1)
                data.append(datalist1)
                
                    
            elif(second_level == 'CE'):
                CE.append(x)
                datalist2=[]
                for y ,y_item in x.items():
                    if(y == 'underlying'):
                        datalist2.insert(1,y_item)  
                    elif(y == 'identifier'):
                        datalist2.insert(0,y_item)      
                    elif(y == 'expiryDate'):
                        datalist2.insert(2,y_item)
                    elif(y == 'strikePrice'):
                        datalist2.insert(3,y_item)
                    elif(y == 'impliedVolatility'):
                        datalist2.insert(4,y_item)
                    elif(y == 'openInterest'):
                        datalist2.insert(5,y_item)
                datalist2= tuple(datalist2)
                data.append(datalist2)
    CE_PE=[]
    CE_PE.append(CE)
    CE_PE.append(PE)
    return data, CE_PE


if __name__ == "__main__":
    data,cepe=pull_iv('NIFTY')
    print(cepe)


    

