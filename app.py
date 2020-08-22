import os
from flask import Flask
from views.items import item_blueprint
from views.alerts import alert_blueprint
from common.database import Database

_author_ = 'Dezhong Shen'

app = Flask(__name__)

app.config.update(
    ADMIN=os.environ.get('ADMIN')
)


#@app.before_first_request
#def init_db():
#    Database.initialize()

# app.register_blueprint(item_blueprint, url_prefix="/items")
app.register_blueprint(alert_blueprint, url_prefix="/alerts")

if __name__ == '__main__':
    app.run(debug=True)