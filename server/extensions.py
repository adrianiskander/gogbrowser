from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from flask_cors import CORS


app = Flask(__name__)
cors = CORS()
sched = BackgroundScheduler()
