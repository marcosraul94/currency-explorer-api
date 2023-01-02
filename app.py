from src.common.app import app, db
from src.common.models import *  # needed for running migrations


@app.route('/ping')
def ping():
    return 'OK'
