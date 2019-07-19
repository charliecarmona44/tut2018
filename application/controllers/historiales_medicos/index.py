import config
import hashlib
import app

class Index:
    
    def __init__(self):
        pass
    
    def GET(self):
        if app.session.loggedin is True: # validate if the user is logged
            email = app.session.user
            privilege = app.session.privilege
            picture = app.session.picture
            params = {}
            params['privilege'] = privilege
            params['user'] = email
            params['picture'] = picture
            privilege = app.session.privilege # get the session_privilege 
            if privilege == 4: # admin user
                return self.GET_INDEX(params) # call GET_INDEX() function
            elif privilege == 0: # guess user
                return self.GET_INDEX(params) # rendner guess.html
        else: # the user dont have logged
            raise config.web.seeother('/') # render login.html

    @staticmethod
    def GET_INDEX(params):
        email = app.session.user
        privilege = app.session.user
    
        resul = config.model.validar_historial_medico(email) # get historiales_medicos table list
        result = resul
             
        return config.render.index(result['id_historial_medico'],params) # render historiales_medicos index.html
