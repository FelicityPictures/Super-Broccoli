import urllib2
import json

error='DEFAULT'
client_id='PLACEHOLDER'

superemails=['ywang7','sbao1','sfang2','fng','mgedrich']

def authenticate(id_token):
    r=urllib2.urlopen('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=%s' % id_token)
    resp=json.load(r)
    global error
    if r.getcode()==200:
        if resp['aud']==client_id:
            if 'hd' in resp.keys():
                if resp['hd']=='stuy.edu':
                    return True
            else:
                error='Invalid domain.'
        else:
            error='Invalid client ID.'
    else:
        error='Invalid user token ID.'
    return False

def auth_super(id_token):
    r=urllib2.urlopen('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=%s' % id_token)
    resp=json.load(r)
    global error
    if r.getcode()==200:
        if resp['aud']==client_id:
            if 'hd' in resp.keys():
                if resp['hd']=='stuy.edu':
                    global superemails
                    if resp['email'].split('@')[0] in superemails:
                        return True
                    else:
                        error='You do not have the permissions for this.'
                else:
                    error='Invalid domain.'
            else:
                error='Invalid client ID.'
        else:
            error='Invalid user token ID.'
    return False

def getName(id_token):
    r=urllib2.urlopen('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=%s' % id_token)
    resp=json.load(r)
    return resp['email'].split('@')[0]

def authSuper(name):
    if name in superemails:
        return True
    return False

def getError():
    global error
    return error
