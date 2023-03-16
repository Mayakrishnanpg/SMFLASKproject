from flask import Flask
from flask import*
from public import public
from merchant import merchant
from farmer import farmer
app=Flask(__name__)
app.secret_key="sm"
app.register_blueprint(public)
app.register_blueprint(merchant,url_prefix="/merchant")
app.register_blueprint(farmer,url_prefix="/farmer")
app.run(debug=True,port=5012)