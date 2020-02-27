from flask import Flask, render_template, redirect, request, make_response, url_for, jsonify
from flask_pymongo import PyMongo
from bson import json_util
import json
from flask_cors import CORS, cross_origin
import base64
import requests
import random, string
import dns
import hashlib
from pathlib import Path
from shutil import unpack_archive
import urllib.parse
import datetime
keys = {}
keyPath = Path('./').glob('keys.json')
keyList = [x for x in keyPath if x.is_file()]
with keyList[0].open("r") as f:
    keys = json.loads(f.read())
    f.close()
CLIENT_SECRET = keys['CLIENT_SECRET']
CLIENT_ID = keys['CLIENT_ID']
RIOT_API_KEY = keys['RIOT_API_KEY']
TWITCH_CLIENT_ID = keys['TWITCH_CLIENT_ID']
TWITCH_CLIENT_SECRET = keys['TWITCH_CLIENT_SECRET']
PATCH = keys['PATCH']
SEASON = keys['SEASON']

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
CORS(app)
#only need cors when local

app.config["MONGO_URI"] = "mongodb+srv://admin2:etnl4OefU7uuTh00@lom-wlgkz.gcp.mongodb.net/lom?retryWrites=true&w=majority"
port = "5000"
prodOrLocal = "http://localhost:" + port + "/"
#prodOrLocal = "https://lom-website-253818.appspot.com/"
mongo = PyMongo(app)
mongo.db.users.create_index([('did', 'text')])  

#Need to send user along with request to ensure the request is not changing another user
#IMPORTANT

@app.route('/')
def index():
    #search by did, find user, make sure hashed id = cookie id
    if request.cookies.get('user') and request.cookies.get('duser'):
        loggedIn = True
    elif request.cookies.get('rememberMe') and request.cookies.get('duser'):
        response = make_response(render_template('index.html'))
        user = mongo.db.users.find_one({"did": request.cookies.get("duser")})
        h = hashlib.sha3_512((str(user['_id']).encode())).hexdigest()
        response.set_cookie('duser', user.did, max_age=60*60*24*31)
        response.set_cookie('user', h, max_age=60*60*24*31)
        response.set_cookie('rememberMe', h, max_age=60*60*24*31)
        loggedIn = True
        return response
    else:
        loggedIn = False
    return render_template("index.html")

@app.route('/login')
def login():
    r = request.args.get('r')
    mcode = request.args.get('mcode')
    if not request.cookies.get('user') and not request.cookies.get('rememberMe') and r != "1":
        #return redirect('https://discordapp.com/api/oauth2/authorize?client_id=628252746365140999&redirect_uri=https%3A%2F%2Flom-website-253818.appspot.com%2Fcallback%3Fr%3D0%26m%3D0&response_type=code&scope=identify%20email%20guilds.join')
        return redirect("https://discordapp.com/api/oauth2/authorize?client_id=628252746365140999&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Fcallback%3Fr%3D0%26m%3D0&response_type=code&scope=identify%20email%20guilds.join")
    elif not request.cookies.get('user') and not request.cookies.get('rememberMe') and r == "1":
        if mcode:
            mongo.db.codes.update({'code': mcode},{'$set':{"used" : True, "usedBy": ''}})
            #return redirect("https://discordapp.com/api/oauth2/authorize?client_id=628252746365140999&redirect_uri=https%3A%2F%2Flom-website-253818.appspot.com%2Fcallback%3Fr%3D1%26m%3D1&response_type=code&scope=identify%20guilds.join%20email")
            return redirect('https://discordapp.com/api/oauth2/authorize?client_id=628252746365140999&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Fcallback%3Fr%3D1%26m%3D1&response_type=code&scope=identify%20email%20guilds.join')
        else:
            #return redirect('https://discordapp.com/api/oauth2/authorize?client_id=628252746365140999&redirect_uri=https%3A%2F%2Flom-website-253818.appspot.com%2Fcallback%3Fr%3D1%26m%3D0&response_type=code&scope=identify%20email%20guilds.join')
            return redirect('https://discordapp.com/api/oauth2/authorize?client_id=628252746365140999&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Fcallback%3Fr%3D1%26m%3D0&response_type=code&scope=identify%20email%20guilds.join')
    else:
        user = mongo.db.users.find_one({"did": request.cookies.get("duser")})
        response = make_response(redirect('/#/profile/' + user['name']))
        h = hashlib.sha3_512((str(user['_id']).encode())).hexdigest()
        response.set_cookie('duser', user['did'], max_age=60*60*24*31)
        response.set_cookie('user', h, max_age=60*60*24*31)
        response.set_cookie('rememberMe', h, max_age=60*60*24*31)
        return response

@app.route('/logout')
def logout():
    response = make_response(redirect('/#/login'))
    #logged out confirm
    response.set_cookie('duser', '', max_age=0)
    response.set_cookie('user', '', max_age=0)
    response.set_cookie('rememberMe', '', max_age=0)
    return response

@app.route('/callback')
def callback():
    code = request.args.get('code')
    r = request.args.get('r')
    m = request.args.get('m')
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
    params = {
        "client_id" : CLIENT_ID,
        "client_secret" : CLIENT_SECRET,
        "redirect_uri" : prodOrLocal + "callback?r=" + r + "&m=" + m,
        "grant_type":"authorization_code",
        "code" : code,
        "scope": "identify email guilds.join"
        }
    print(prodOrLocal + "?r=" + r + "&m=" + m)
    try:
        access_token = requests.post('https://discordapp.com/api/oauth2/token', data=params, headers=headers).json()
        print(access_token)
        infoHeaders = {'Authorization': 'Bearer ' + access_token['access_token']}
        info = requests.get('https://discordapp.com/api/users/@me', headers=infoHeaders).json()
        user = mongo.db.users.find_one({"did": info['id']})
        if r != "1":
            #regular login
            if user:
                response = make_response(redirect('/#/profile/' + user['did']))
            else:
                response = make_response(redirect('/#/signup'))
                #error about needing to register first
        if r == "1":
            #sign them up then redirect to fill in profile
            if m == "1":
                t = "mentor"
            else:
                t = "student"
            u = {
            "did":info['id'],
            "champs":[],
            "type":t,
            "achievements":[],
            "bio":"",
            "requirements":{},
            "name":info['username'],
            "score":0,
            "socials":{},
            "rank":"default",
            "main":"",
            "region":[],
            "languages":[],
            "reviewType":[],
            "moneyType":[],
            "roles":[],
            "email":info['email'],
            "bg": "Heimerdinger_0"
            }
            if not user:
                mongo.db.users.insert(u)
                response = make_response(redirect('/#/editProfile?new=1')) 
                user = mongo.db.users.find_one({"did": info['id']})
            else:
                #already registered error
                response = make_response(redirect('/#/login'))  
        h = hashlib.sha3_512((str(user['_id']).encode())).hexdigest()
        oneMonth = 60*60*24*31
        oneDay = 60*60*24*1
        response.set_cookie('duser', user['did'], max_age=oneMonth)
        response.set_cookie('user', h, max_age=oneMonth)
        response.set_cookie('rememberMe', h, max_age=oneMonth)
        return response
    except:
        #unknown error try again
        return make_response(redirect('/#/login'))
#Here lies the API
@app.route('/api/profileInfo/<user>', methods=['GET', 'POST'])
def profileInfo(user):
    if request.method == 'GET':
        if user == "MENTORS":
            prep = mongo.db.users.find({"type": "mentor"}, { 'ip': 0, 'type': 0 })
            response = json.dumps([mentor for mentor in prep], default=json_util.default)
        else:
            response = json.dumps(mongo.db.users.find_one({ "$text": { "$search": user } },  { 'ip': 0, 'password': 0 }), default=json_util.default)
        return response
    else:
        data = request.get_json()
        newData = data.copy()
        newData.pop('did', None)
        try:
            print(newData)
            print(data['did'])
            mongo.db.users.update({'did': data['did']},{'$set':newData})
            return "true"
        except:
            return "false"
@app.route('/api/checkCode/<code>')
def checkCode(code):
    prep = mongo.db.codes.find_one({"code": code})
    response = json.dumps(prep, default=json_util.default)
    return response

@app.route('/api/checkUser')
def checkUser():
    #we want to send back user info so we don't have to make another req
    id = request.cookies.get('user')
    did = request.cookies.get('duser')
    user = mongo.db.users.find_one({"did": did})
    try:
        compare = hashlib.sha3_512((str(user['_id']).encode())).hexdigest()
        if compare == id:
            return json.dumps(user, default=json_util.default)
        else:
            return json.dumps(False)
    except:
        return json.dumps(False)
@app.route('/api/getStreams')
def getStreams():
    prep = mongo.db.users.find({"type": "mentor"}, { 'ip': 0, 'type': 0 })
    logins = ""
    streamList = {}
    for document in prep:
        print(document['socials'])
        try:
            if document['socials']['twitch']:
                logins = logins + "user_login=" + document['socials']['twitch'] + "&"
                streamList[document['socials']['twitch'].lower()] = document['did']
                print(streamList)
        except:
            pass
    headers = {'Client-ID': TWITCH_CLIENT_ID}
    info = requests.get('https://api.twitch.tv/helix/streams?&game_id=21779&first=100&' + logins, headers=headers).json() 
    try:
        for stream in info['data']:
            stream['did'] = streamList[stream['user_name'].lower()]
        print(info)
        return json.dumps(info['data'])
    except:
        return json.dumps([])

@app.route('/api/getCoaching/<user>', methods=['GET'])
def getCoaching(user):
    if request.args.get('complete'):
        if(request.args.get('complete') == '1'):
            prep = mongo.db.coaching.find({"mentor": user, "complete": True, "reviewTitle":  {"$exists" : True, "$ne" : ""}})
    else:
        prep = mongo.db.coaching.find({"mentor": user})
    return json.dumps([c for c in prep], default=json_util.default)

@app.route('/api/getNews')
def getNews():
    prep = mongo.db.news.find().sort([("date", -1)])
    return json.dumps([c for c in prep], default=json_util.default)

@app.route('/api/riotApi', methods=['POST'])
def riotAPI():
    data = request.get_json()
    region = data['region']
    user = data['accountName']
    timeInMs = str(int(datetime.datetime.now().timestamp()*1000-604800000)) 
    print(timeInMs)
    accountInfoURL = "https://" + region + "1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + user + "?api_key=" + RIOT_API_KEY
    accountInfo = requests.get(accountInfoURL).json()
    accountId = accountInfo['accountId']
    summonerId = accountInfo['id']
    #Games from x time ago
    weeklyMatchlistURL = "https://" + region + "1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountId + "?beginTime=" + timeInMs + "&api_key=" + RIOT_API_KEY
    weeklyMatchlist = requests.get(weeklyMatchlistURL).json()
    print(weeklyMatchlist)
    totalChamps = len(set([c['champion'] for c in weeklyMatchlist['matches']]))
    totalGames = weeklyMatchlist['totalGames']
    print(totalChamps)
    #Season games
    url3 = "https://" + region + "1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountId + "?season=" + SEASON + "&api_key=" + RIOT_API_KEY
    #Rank
    rankedStatsURL = "https://" + region + "1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + summonerId + "?api_key=" + RIOT_API_KEY
    rankedStats = requests.get(rankedStatsURL).json()
    soloq = next((x for x in rankedStats if x['queueType'] == "RANKED_SOLO_5x5"), None)
    convertedNumber = None
    if soloq['rank'] == "I":
        convertedNumber = "1" 
    elif soloq['rank'] == "II": 
        convertedNumber = "2"
    elif soloq['rank'] == "III":
        convertedNumber = "3"
    else:
        convertedNumber = "4"
    if soloq['tier']:
        finalRank = soloq['tier'].lower() + "_" + convertedNumber
    else: 
        finalRank = "default"
    goals =  {"gamesPlayed": totalGames, "champsPlayed": totalChamps, "lastUpdate": datetime.datetime.now().timestamp()}
    final = {"rank": finalRank, "goalProgress": goals}
    mongo.db.users.update({'did': data['did']},{'$set':final, '$push': { "rankTimeline": {"rank": finalRank, "time": datetime.datetime.now().timestamp() }}})
    return {"rank": finalRank, "time": datetime.datetime.now().timestamp(), "goalProgress": goals}

@app.route('/api/getSkinList', methods=['POST'])
def getSkinList():
#This will update skin/champion lists -> still need to manually update splashes + add new champs to square_icons via community dragon + .ddragon in riot disc
    user = request.get_json()
    adminCheck = mongo.db.users.find_one({"did": user['did'], "admin": True})
    if adminCheck:
        try:
            skinList = {}
            championList = requests.get('http://ddragon.leagueoflegends.com/cdn/' + PATCH + '/data/en_US/champion.json').json()
            for champ in championList['data']:
                c = requests.get('http://ddragon.leagueoflegends.com/cdn/' + PATCH + '/data/en_US/champion/' + champ + '.json').json()
                skinList[champ] = []
                print(champ)
                for skin in c['data'][champ]['skins']:
                    skinList[champ].append({"name": skin['name'], "id": skin['num']})
            #Also we should just update Champion List while we pull it       
            p1 = Path('./static').glob('champions.json')
            file1 = [x for x in p1 if x.is_file()]
            with file1[0].open("w+") as f:
                json.dump(championList, f)
            #Update Skins
            p = Path('./static').glob('skinList.json')
            file = [x for x in p if x.is_file()]
            with file[0].open("w+") as f:
                json.dump(skinList, f)
            splashes = "https://ddragon.leagueoflegends.com/cdn/dragontail-" + PATCH + ".tgz"
            return "true"
        except:
            return "false"

@app.route('/api/changeAPIKeys', methods=['POST'])
def changeAPIKeys():
    data = request.get_json()
    adminCheck = mongo.db.users.find_one({"did": data['did'], "admin": True})
    if adminCheck:
        if not data['keyType']:
            print({'keys': list(keys.keys()), 'patch': keys['PATCH']})
            return {'keys': list(keys.keys()), 'patch': keys['PATCH']}
        else:
            try:
                keys[data['keyType']] = data['new_key']
                print(keys)
                with keyList[0].open("w+") as f:
                    json.dump(keys, f)
                return "true"
            except:
                return "false"
@app.route('/api/generateCode', methods=['POST'])
def generateCode():
    data = request.get_json()
    adminCheck = mongo.db.users.find_one({"did": data['did'], "admin": True})
    if adminCheck:
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        codeType = data['codeType']
        genBy = adminCheck['name']
        d = {
            'code': x,
            'type': codeType,
            'used': False,
            'usedBy': '',
            'generatedBy': genBy
        }
        mongo.db.codes.insert(d)
        return x
    return "false"