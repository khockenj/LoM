from flask import Flask, render_template, redirect, request, make_response, url_for
from flask_pymongo import PyMongo
from bson import json_util
import json
from flask_cors import CORS, cross_origin
import base64
import requests
import random, string
CLIENT_SECRET ="hx984-Qq67PLmssoCtcUBhLEHrXP74gG"
CLIENT_ID = "628252746365140999"
app = Flask(__name__,
            static_folder = "../dist/static",
            template_folder = "../dist")
CORS(app)
#app.config["MONGO_URI"] = "mongodb://localhost:27017/lom"  
app.config["MONGO_URI"] = "mongodb+srv://admin:KjhKrK2017<3@lom-wlgkz.gcp.mongodb.net/admin?retryWrites=true&w=majority")

mongo = PyMongo(app)     
mongo.db.users.create_index([('name', 'text')])   
@app.route('/')
def index():
    if request.cookies.get('user') and request.cookies.get('duser'):
        loggedIn = True
    elif request.cookies.get('rememberMe') and request.cookies.get('duser'):
        response = make_response(render_template('index.html'))
        user = mongo.db.users.findOne({"did": request.cookies.get("duser")})
        h = hash(user._id)
        response.set_cookie('duser', user.did, max_age=60*60*24*31)
        response.set_cookie('user', h, max_age=60*60*24*1)
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
        return redirect("https://discordapp.com/api/oauth2/authorize?client_id=628252746365140999&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Fcallback%3Fr%3D0&response_type=code&scope=identify%20email%20guilds.join")
    elif not request.cookies.get('user') and not request.cookies.get('rememberMe') and r == "1":
        if mcode:
            mongo.db.codes.update({'code': mcode},{'$set':{"used" : True, "usedBy": ''}})
            return redirect('https://discordapp.com/api/oauth2/authorize?client_id=628252746365140999&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Fcallback%3Fr%3D1%26m%3D1&response_type=code&scope=identify%20email%20guilds.join')
        else:
            return redirect('https://discordapp.com/api/oauth2/authorize?client_id=628252746365140999&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Fcallback%3Fr%3D1%26m%3D0&response_type=code&scope=identify%20email%20guilds.join')
    else:
        user = mongo.db.users.find_one({"did": request.cookies.get("duser")})
        response = make_response(redirect('/#/profile/' + user['name']))
        h = str(hash(user['_id']))
        response.set_cookie('duser', user['did'], max_age=60*60*24*31)
        response.set_cookie('user', h, max_age=60*60*24*1)
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
        "redirect_uri" : "http://localhost:5000/callback?r=" + r + "&m=" + m,
        "grant_type":"authorization_code",
        "code" : code,
        "scope": "identify email guilds.join"
        }
    try:
        access_token = requests.post('https://discordapp.com/api/oauth2/token', data=params, headers=headers).json()
        infoHeaders = {'Authorization': 'Bearer ' + access_token['access_token']}
        info = requests.get('https://discordapp.com/api/users/@me', headers=infoHeaders).json()
        user = mongo.db.users.find_one({"did": info['id']})
        if r != "1":
            #regular login
            if user:
                response = make_response(redirect('/#/profile/' + user['name']))
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
            "rank":"",
            "main":"",
            "region":[],
            "languages":[],
            "reviewType":[],
            "moneyType":[],
            "roles":[],
            "email":info['email']
            }
            if not user:
                mongo.db.users.insert(u)
                response = make_response(redirect('/#/editProfile?new=1')) 
                user = mongo.db.users.find_one({"did": info['id']})
            else:
                #already registered error
                response = make_response(redirect('/#/login'))  
        h = str(hash(user['_id']))
        oneMonth = 60*60*24*31
        oneDay = 60*60*24*1
        response.set_cookie('duser', user['did'], max_age=oneMonth)
        response.set_cookie('user', h, max_age=oneDay)
        response.set_cookie('rememberMe', h, max_age=oneMonth)
        return response
    except:
        #unknown error try again
        return make_response(redirect('/#/login'))
#Here lies the API
@app.route('/api/profileInfo/<user>')
def profileInfo(user):
    if user == "MENTORS":
        prep = mongo.db.users.find({"type": "mentor"}, { 'ip': 0, 'password': 0, 'type': 0 })
        response = json.dumps([mentor for mentor in prep], default=json_util.default)
    else:
        response = json.dumps(mongo.db.users.find_one({ "$text": { "$search": user } },  { 'ip': 0, 'password': 0 }), default=json_util.default)
    return response

@app.route('/api/checkCode/<code>')
def checkCode(code):
    prep = mongo.db.codes.find_one({"code": code})
    response = json.dumps(prep, default=json_util.default)
    return response

def generateCode():
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    codeType = "mentor"
    genBy = "K3Vx"
    d = {
        'code': x,
        'type': codeType,
        'used': False,
        'usedBy': '',
        'generatedBy': genBy
    }
    mongo.db.codes.insert(d)