import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_tutoria_especial, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_tutoria_especial) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_tutoria_especial, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_tutoria_especial) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_tutoria_especial, **k):

    @staticmethod
    def POST_DELETE(id_tutoria_especial, **k):
    '''

    def GET(self, id_tutoria_especial, **k):
        message = None # Error message
        id_tutoria_especial = config.check_secure_val(str(id_tutoria_especial)) # HMAC id_tutoria_especial validate
        result = config.model.get_tutoria_especial(int(id_tutoria_especial)) # search  id_tutoria_especial
        result.id_tutoria_especial = config.make_secure_val(str(result.id_tutoria_especial)) # apply HMAC for id_tutoria_especial
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_tutoria_especial, **k):
        form = config.web.input() # get form data
        form['id_tutoria_especial'] = config.check_secure_val(str(form['id_tutoria_especial'])) # HMAC id_tutoria_especial validate
        result = config.model.delete_tutoria_especial(form['id_tutoria_especial']) # get tutoria_especial data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_tutoria_especial = config.check_secure_val(str(id_tutoria_especial))  # HMAC user validate
            id_tutoria_especial = config.check_secure_val(str(id_tutoria_especial))  # HMAC user validate
            result = config.model.get_tutoria_especial(int(id_tutoria_especial)) # get id_tutoria_especial data
            result.id_tutoria_especial = config.make_secure_val(str(result.id_tutoria_especial)) # apply HMAC to id_tutoria_especial
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/tutoria_especial') # render tutoria_especial delete.html 
