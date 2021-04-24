from flask import Flask,jsonify,render_template
from flask_restful import Api,Resource
import schedule
import threading
from schdulejob import *
from apscheduler.schedulers.background import BackgroundScheduler
import os


sched = BackgroundScheduler(daemon=True)
sched.add_job(market_status_job,'interval',max_instances=10, seconds=300)
sched.add_job(market_data_job,'interval',max_instances=10,seconds=300)
sched.start()

app = Flask(__name__)
PORT= os.environ.get('PORT')
@app.route("/")
@app.route("/home")
def home():
    """ Function for test purposes. """
    return render_template('./Template/Acctav.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=PORT)