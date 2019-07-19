import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_trayectoria_academica, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_trayectoria_academica) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_trayectoria_academica, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_trayectoria_academica) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_trayectoria_academica, **k):

    @staticmethod
    def POST_DELETE(id_trayectoria_academica, **k):
    '''

    def GET(self, id_trayectoria_academica, **k):
        message = None # Error message
        id_trayectoria_academica = config.check_secure_val(str(id_trayectoria_academica)) # HMAC id_trayectoria_academica validate
        result = config.model.get_trayectorias_academicas(int(id_trayectoria_academica)) # search  id_trayectoria_academica
        result.id_trayectoria_academica = config.make_secure_val(str(result.id_trayectoria_academica)) # apply HMAC for id_trayectoria_academica
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_trayectoria_academica, **k):
        form = config.web.input() # get form data
        form['id_trayectoria_academica'] = config.check_secure_val(str(form['id_trayectoria_academica'])) # HMAC id_trayectoria_academica validate
        result = config.model.delete_trayectorias_academicas(form['id_trayectoria_academica']) # get trayectorias_academicas data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_trayectoria_academica = config.check_secure_val(str(id_trayectoria_academica))  # HMAC user validate
            id_trayectoria_academica = config.check_secure_val(str(id_trayectoria_academica))  # HMAC user validate
            result = config.model.get_trayectorias_academicas(int(id_trayectoria_academica)) # get id_trayectoria_academica data
            result.id_trayectoria_academica = config.make_secure_val(str(result.id_trayectoria_academica)) # apply HMAC to id_trayectoria_academica
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/trayectorias_academicas') # render trayectorias_academicas delete.html 
