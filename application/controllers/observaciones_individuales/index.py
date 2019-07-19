import config
import hashlib
import app

class Index:
    
    def __init__(self):
        pass
    
    def GET(self):
        if app.session.loggedin is True: # validate if the user is logged
            session_user = app.session.user
            session_privilege = app.session.privilege # get the session_privilege 
            if session_privilege == 0: # admin user
                return self.GET_INDEX() # call GET_INDEX() function
            elif session_privilege == 1: # guess user
                return self.GET_INDEX()
            elif session_privilege == 2: # guess user
                return self.GET_INDEX()

        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INDEX():
       
        result = config.model_alumnos_observaciones.get_all_alumnos_observaciones().list()
        for row in result:
            row.id_observacion_individual = config.make_secure_val(str(row.id_observacion_individual)) # apply HMAC to id_observacion_individual (primary key)
        return config.render.index(result) # render observaciones_individuales index.html
