from flask import Flask,jsonify
from flask_restful import Api,Resource
import schedule
import threading
from schdulejob import *
from apscheduler.schedulers.background import BackgroundScheduler


sched = BackgroundScheduler(daemon=True)
sched.add_job(market_status_job,'interval',seconds=300)
sched.add_job(market_data_job,'interval',seconds=300)
sched.start()

app = Flask(__name__)

@app.route("/home")
def home():
    """ Function for test purposes. """
    return "Welcome Home :) !"

if __name__ == "__main__":
    app.run()