from flask import Flask,jsonify
from flask_restful import Api,Resource
import schedule
from flask_sqlalchemy import SQLAlchemy
import threading
#import market_data
import schdulejob


app= Flask(__name__)
api=Api(app)


schedule.every().day.at("09:00").do(market_status_job)









if __name__ == "__main__":
    app.run(debug=True)
    
     