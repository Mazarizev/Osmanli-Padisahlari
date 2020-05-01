from flask import Flask, request, url_for, make_response
from flask_pymongo import PyMongo
import os

Program = Flask (__name__)
Program.config ["MONGO_URI"] = "mongodb://127.0.0.1:27017/Ottoman"
Mongo = PyMongo (Program)

@Program.route ("/")
def Index ():
    Response = make_response ({ "Sultans" : [{ "ID": I ["ID"], "Name": I ["Name"], "Number": I ["Number"], "Reign": I ["Reign"], "Image": I ["Image"], "Tughra": I ["Tughra"] } \
    for I in Mongo.db.Sultans.find ()] })
    Response.headers ["Access-Control-Allow-Origin"] = "*"
    return Response

@Program.before_first_request
def Before ():
    with open ("Flag/Flag.png", "rb") as Image: Mongo.save_file ("Flag.png", Image)
    for File in os.listdir ("Tughras"): 
        with open ("Tughras/" + File, "rb") as Image:
            Mongo.save_file (File, Image)
    for File in os.listdir ("Sultans"): 
        with open ("Sultans/" + File, "rb") as Image:
            Mongo.save_file (File, Image) 
      
@Program.route ("/File/<Name>")
def File (Name):
    return Mongo.send_file (Name)

@Program.route ("/Sultan/<int:ID>")
def Sultan (ID):
    Object = Mongo.db.Sultans.find_one_or_404 ({ "ID": ID })
    return f"""
            <h1 style = "font-family: sans-serif">{Object ["Name"]} {Object ["Number"]}</h1>
              <img src = "{url_for ("File", Name = Object ["Image"])}">
            """

if __name__ == "__main__": Program.run ()