import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_periodo, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_periodo) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_periodo, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_periodo) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_periodo, **k):

    @staticmethod
    def POST_DELETE(id_periodo, **k):
    '''

    def GET(self, id_periodo, **k):
        message = None # Error message
        id_periodo = config.check_secure_val(str(id_periodo)) # HMAC id_periodo validate
        result = config.model.get_periodos(int(id_periodo)) # search  id_periodo
        result.id_periodo = config.make_secure_val(str(result.id_periodo)) # apply HMAC for id_periodo
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_periodo, **k):
        form = config.web.input() # get form data
        form['id_periodo'] = config.check_secure_val(str(form['id_periodo'])) # HMAC id_periodo validate
        result = config.model.delete_periodos(form['id_periodo']) # get periodos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_periodo = config.check_secure_val(str(id_periodo))  # HMAC user validate
            id_periodo = config.check_secure_val(str(id_periodo))  # HMAC user validate
            result = config.model.get_periodos(int(id_periodo)) # get id_periodo data
            result.id_periodo = config.make_secure_val(str(result.id_periodo)) # apply HMAC to id_periodo
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/periodos') # render periodos delete.html 
