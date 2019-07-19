import config
import app
import auth
import json
import web

class Logout:
    def __init__(self):
        pass

    @staticmethod
    def GET():


        app.session.loggedin = False
        web.setcookie('_id', '', 0)
        app.session.user = 'anonymous'
        app.session.privilege = -1 #asignar privilegio solo para pagina de introduccion
        app.session.kill()#destruir la session de kuorra
        #raise config.web.seeother('/')
        raise config.web.seeother('https://accounts.google.com/Logout')
       #redireccion al index

#ServiceLogin?elo=1

#/CheckCookie?hl=es-419&checkedDomains=youtube&checkConnection=youtube%3A4868%3A1&pstMsg=1&chtml=LoginDoneHt