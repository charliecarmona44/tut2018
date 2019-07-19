import config
import hashlib
import app

class Index:
    
    def __init__(self):
        pass
    
    def GET(self):
        if app.session.loggedin is True: # validate if the user is logged
            user = app.session.user
            privilege = app.session.privilege
            picture = app.session.picture
            email = app.session.user
            params={}
            params['user']=user
            params['privilege']=privilege
            params['picture']=picture
            message = None
            if privilege == 4: # admin user
                return self.GET_INDEX(email,params,message) # call GET_INDEX() function
            elif privilege == 1: # guess user
                return self.GET_INDEX(email,params,message)
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INDEX(email,params,message): 
        message = None   
        resul = config.model.validar_trayectorias_academicas(email) # get trayectorias_academicas table list
        result = resul
             
        return config.render.index(result['id_trayectoria_academica'],params,message) # render trayectorias_academicas index.html
