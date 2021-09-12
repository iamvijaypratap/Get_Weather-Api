from flask import Flask,redirect,url_for,render_template,request
import requests

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def Get_WeatherInfo():
    if request.method=="POST":
        url ='http://api.openweathermap.org/data/2.5/weather?q={},in&APPID=49f26b78235a96eed41bba96e732d27e' 
        city = request.form.get("Data")
        r = requests.get(url.format(city)).json()
        if r["cod"]=="404":
            return "city not found"
        else:
            weather= {
                    "city": r["name"],
                    "temprature" :round(r["main"]["temp"]-273.15),
                    "description":r["weather"][0]["description"],
                    "icon":r["weather"] [0]["icon"],
                    "code" :r["cod"],
                    "country":r["sys"]["country"], }
            return render_template("weather.html",weather=weather)
    return render_template("weather.html")


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)