import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    
    def GET(self, user):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(user) # call GET_VIEW() function
            else: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(user):
        id_tutor_grupo = config.check_secure_val(str(user)) # HMAC id_tutor_grupo validate
        result = config.model_users.get_users(user) # search for the id_tutor_grupo data
        return config.render.view(result) # render view.html with id_tutor_grupo data
