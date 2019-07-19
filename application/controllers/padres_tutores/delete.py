import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_padre_tutor, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_padre_tutor) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_padre_tutor, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_padre_tutor) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_padre_tutor, **k):

    @staticmethod
    def POST_DELETE(id_padre_tutor, **k):
    '''

    def GET(self, id_padre_tutor, **k):
        message = None # Error message
        id_padre_tutor = config.check_secure_val(str(id_padre_tutor)) # HMAC id_padre_tutor validate
        result = config.model.get_padres_tutores(int(id_padre_tutor)) # search  id_padre_tutor
        result.id_padre_tutor = config.make_secure_val(str(result.id_padre_tutor)) # apply HMAC for id_padre_tutor
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_padre_tutor, **k):
        form = config.web.input() # get form data
        form['id_padre_tutor'] = config.check_secure_val(str(form['id_padre_tutor'])) # HMAC id_padre_tutor validate
        result = config.model.delete_padres_tutores(form['id_padre_tutor']) # get padres_tutores data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_padre_tutor = config.check_secure_val(str(id_padre_tutor))  # HMAC user validate
            id_padre_tutor = config.check_secure_val(str(id_padre_tutor))  # HMAC user validate
            result = config.model.get_padres_tutores(int(id_padre_tutor)) # get id_padre_tutor data
            result.id_padre_tutor = config.make_secure_val(str(result.id_padre_tutor)) # apply HMAC to id_padre_tutor
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/padres_tutores') # render padres_tutores delete.html 
