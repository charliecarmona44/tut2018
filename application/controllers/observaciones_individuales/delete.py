import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_observacion_individual, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_observacion_individual) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_observacion_individual, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_observacion_individual) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_observacion_individual, **k):

    @staticmethod
    def POST_DELETE(id_observacion_individual, **k):
    '''

    def GET(self, id_observacion_individual, **k):
        message = None # Error message
        id_observacion_individual = config.check_secure_val(str(id_observacion_individual)) # HMAC id_observacion_individual validate
        result = config.model.get_observaciones_individuales(int(id_observacion_individual)) # search  id_observacion_individual
        result.id_observacion_individual = config.make_secure_val(str(result.id_observacion_individual)) # apply HMAC for id_observacion_individual
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_observacion_individual, **k):
        form = config.web.input() # get form data
        form['id_observacion_individual'] = config.check_secure_val(str(form['id_observacion_individual'])) # HMAC id_observacion_individual validate
        result = config.model.delete_observaciones_individuales(form['id_observacion_individual']) # get observaciones_individuales data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_observacion_individual = config.check_secure_val(str(id_observacion_individual))  # HMAC user validate
            id_observacion_individual = config.check_secure_val(str(id_observacion_individual))  # HMAC user validate
            result = config.model.get_observaciones_individuales(int(id_observacion_individual)) # get id_observacion_individual data
            result.id_observacion_individual = config.make_secure_val(str(result.id_observacion_individual)) # apply HMAC to id_observacion_individual
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/observaciones_individuales') # render observaciones_individuales delete.html 
