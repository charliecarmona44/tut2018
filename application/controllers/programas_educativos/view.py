import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    
    def GET(self, id_programa_educativo):
        if app.session.loggedin is True: # validate if the user is logged
            session_username = app.session.user
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_programa_educativo) # call GET_VIEW() function
            else: # guess user
                raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_programa_educativo):
        id_programa_educativo = config.check_secure_val(str(id_programa_educativo)) # HMAC id_programa_educativo validate
        result = config.model.get_programas_educativos(id_programa_educativo) # search for the id_programa_educativo data
        return config.render.view(result) # render view.html with id_programa_educativo data
