# coding: UTF-8
import tweepy
import schedule
import time

import config
import weather

CK  = config.CONSUMER_KEY
CS  = config.CONSUMER_SECRET_KEY
AT  = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)

faceData=['😊','🙂','😟','😩','😖','😎','🤔','🤮','😇']
weatherData=['☀️','⛅️','☁️','🌂','☂️','☔️','🌪','🤷‍♂️']

data = weather.getInfo(0)

def decide():
    if data['weather'][0]['main'] == 'Clear':
        if data['main']['humidity'] > 80:
            return weatherData[0],faceData[6]
        elif data['wind']['speed'] >10:
            return weatherData[0],faceData[5]
        elif data['wind']['speed'] >5:
            return weatherData[0],faceData[0]
        elif data['wind']['speed'] <=5:
            return weatherData[0],faceData[1]
    elif data['weather'][0]['main'] == 'Clouds':
        if data['clouds']['all'] >=85:
            if data['main']['humidity'] >=80:
                return weatherData[2],faceData[8]
            elif data['main']['humidity'] <80:
                return weatherData[2],faceData[1]
        if data['clouds']['all'] <85:
            if data['wind']['speed'] >10:
                return weatherData[1],faceData[4]
            elif data['wind']['speed'] >5:
                return weatherData[1],faceData[5]
            elif data['wind']['speed'] <=5:
                return weatherData[1],faceData[2]
    elif data['weather'][0]['main'] == 'Rain':
        if data['rain']:
            if data['rain']['3h'] >20:
                if data['wind']['speed'] >10:
                    return weatherData[6],faceData[8]
                elif data['wind']['speed'] >3:
                    return weatherData[5],faceData[7]
                elif data['wind']['speed'] <=3:
                    return weatherData[5],faceData[7]
            if data['rain']['3h'] >3:
                if data['wind']['speed'] >10:
                    return weatherData[4],faceData[8]
                elif data['wind']['speed'] >5:
                    return weatherData[4],faceData[7]
                elif data['wind']['speed'] <=5:
                    return weatherData[4],faceData[7]
            if data['rain']['3h'] <=3:
                if data['wind']['speed'] >10:
                    return weatherData[3],faceData[4]
                elif data['wind']['speed'] >5:
                    return weatherData[3],faceData[4]
                elif data['wind']['speed'] <=5:
                    return weatherData[3],faceData[4]
    else:
        return weatherData[7],faceData[6]

def change():
    nameStr = "もぎ%s%s" % (decide())
    print(nameStr)
    api.update_profile(name=nameStr)   

schedule.every(1).hours.do(change)
while True:
    schedule.run_pending()
    time.sleep(1)
