import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    
    def GET(self, id_tutor_grupo, message=None):
        if app.session.loggedin is True: # validate if the user is logged
            session_user = app.session.user
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_tutor_grupo) # call GET_DELETE function
            else: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_tutor_grupo, message=None):
        if app.session.loggedin is True: # validate if the user is logged
            session_user = app.session.user
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_tutor_grupo) # call POST_DELETE function
            else: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_tutor_grupo, message=None):
        id_tutor_grupo = config.check_secure_val(str(id_tutor_grupo)) # HMAC id_tutor_grupo validate
        result = config.model.get_tutores_grupos(int(id_tutor_grupo)) # search  id_tutor_grupo
        result.id_tutor_grupo = config.make_secure_val(str(result.id_tutor_grupo)) # apply HMAC for id_tutor_grupo
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_tutor_grupo, message=None):
        form = config.web.input() # get form data
        form['id_tutor_grupo'] = config.check_secure_val(str(form['id_tutor_grupo'])) # HMAC id_tutor_grupo validate
        result = config.model.delete_tutores_grupos(form['id_tutor_grupo']) # get tutores_grupos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_tutor_grupo = config.check_secure_val(str(id_tutor_grupo))  # HMAC user validate
            id_tutor_grupo = config.check_secure_val(str(id_tutor_grupo))  # HMAC user validate
            result = config.model.get_tutores_grupos(int(id_tutor_grupo)) # get id_tutor_grupo data
            result.id_tutor_grupo = config.make_secure_val(str(result.id_tutor_grupo)) # apply HMAC to id_tutor_grupo
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/tutores_grupos') # render tutores_grupos delete.html 
