import requests
import json



def market_status_api():
    market_status_api_url='https://www.nseindia.com/api/marketStatus'
    cookies=  "977E0247365692D2A9075FFCB57548AD~2Lkkb7B4CGYq4IoDwtc9YxecAplXUEilUnSDbNpOB+vHnWn7FkmjSLLCnb2Dk4UdkLfUa82KfJyPYaB5nljwoYu6Yhlhev4UrLgJHgKNA7olHYVHnHRPG1+tDI2NDPcrJUy8L2vZIJxr4TfejOTM6tRj8jr/mpztalDrlhNcRGA"
    api_headers= {"Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9","User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36","cookie":cookies}
    response = requests.get(market_status_api_url,headers=api_headers)
    json_data=json.loads(response.text)
    market_status=json_data["marketState"][0]["marketStatus"]
    #market_status= market_status[0]
    return market_status

if __name__ == "__main__":
    if(market_status_api()=='Close'):
        print("Market is closed")