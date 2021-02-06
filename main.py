from flask import Flask,jsonify
from flask_restful import Api,Resource
import schedule
from flask_apscheduler import APScheduler
from iv import pull_iv
import_iv=pull_iv('NIFTY')
app= Flask(__name__)
api=Api(app)
scheduler=APScheduler()



def geeks(): 
    print("Shaurya says Geeksforgeeks") 
    #schedule.every(1).minutes.do(geeks)

class Helloworld(Resource):
    def get(self):
        return import_iv

api.add_resource(Helloworld,"/helloworld")

if __name__ == "__main__":
    scheduler.add_job(id='schdule task',func=geeks,trigger='interval',seconds=1)
    scheduler.start()
    app.run(debug=True)
    
     