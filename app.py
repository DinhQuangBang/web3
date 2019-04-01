from flask import Flask, render_template, request, redirect
from service import bikes_collection
app = Flask(__name__)


@app.route ('/new_bike', methods = ["GET", "POST"])
def bike():
    if (request.method == "GET"):
         return render_template("bike.html")
    elif (request.method == "POST"):
        form = request.form
        new_bike = {
            "model": form["model"],
            "fee": form["fee"],
            "image": form["image"],
            "year": form["year"]
        }
        bikes_collection.insert_one (new_bike)
        return redirect ('/new_bike')

if __name__ == '__main__':
    app.run(debug=True)