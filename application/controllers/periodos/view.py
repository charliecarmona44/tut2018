import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    '''
    def GET(self, id_periodo):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_periodo) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_periodo):
    '''

    def GET(self, id_periodo):
        id_periodo = config.check_secure_val(str(id_periodo)) # HMAC id_periodo validate
        result = config.model.get_periodos(id_periodo) # search for the id_periodo data
        return config.render.view(result) # render view.html with id_periodo data
