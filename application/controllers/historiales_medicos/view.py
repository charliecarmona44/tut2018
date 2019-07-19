import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    '''
    def GET(self, id_historial_medico):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_historial_medico) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_historial_medico):
    '''

    def GET(self, id_historial_medico):
        id_historial_medico = config.check_secure_val(str(id_historial_medico)) # HMAC id_historial_medico validate
        result = config.model.get_historiales_medicos(id_historial_medico) # search for the id_historial_medico data
        return config.render.view(result) # render view.html with id_historial_medico data
