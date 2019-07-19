import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    
    def GET(self, id_programa_educativo, message=None):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_programa_educativo, message) # call GET_DELETE function
            else: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_programa_educativo, message=None):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_programa_educativo, message) # call POST_DELETE function
            else: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_programa_educativo, message=None):
        id_programa_educativo = config.check_secure_val(str(id_programa_educativo)) # HMAC id_programa_educativo validate
        result = config.model.get_programas_educativos(int(id_programa_educativo)) # search  id_programa_educativo
        result.id_programa_educativo = config.make_secure_val(str(result.id_programa_educativo)) # apply HMAC for id_programa_educativo
        return config.render.delete(result, message) # render delete.html with user data




    @staticmethod
    def POST_DELETE(id_programa_educativo, message=None):
        form = config.web.input() # get form data
        form['id_programa_educativo'] = config.check_secure_val(str(form['id_programa_educativo'])) # HMAC id_programa_educativo validate
        result = config.model.delete_programas_educativos(form['id_programa_educativo']) # get programas_educativos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_programa_educativo = config.check_secure_val(str(id_programa_educativo))  # HMAC user validate
            id_programa_educativo = config.check_secure_val(str(id_programa_educativo))  # HMAC user validate
            result = config.model.get_programas_educativos(int(id_programa_educativo)) # get id_programa_educativo data
            result.id_programa_educativo = config.make_secure_val(str(result.id_programa_educativo)) # apply HMAC to id_programa_educativo
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/programas_educativos') # render programas_educativos delete.html 





 
        
