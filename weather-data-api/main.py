from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations_file = "../data_small/stations.txt"
stations = pd.read_csv(stations_file, skiprows=17)
@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/about/")
def about():
    return render_template("tutorial.html")


@app.route("/api/v1/<station>")
def all_data_for_station(station):
    filename = "../data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df[0:10].to_dict(orient="records")
    return result


@app.route("/api/v1/<station>/<date>/")
def data_for_date(station, date):
    filename = "../data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }

@app.route("/api/v1/yearly/<station>/<year>")
def data_for_year(station, year):
    filename = "../data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))][0:10].to_dict(orient="records")
    return result

if __name__ == "__main__":
    app.run(debug=True, port=5000)
