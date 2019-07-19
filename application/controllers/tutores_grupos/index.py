import config
import hashlib
import app

class Index:
    
    def __init__(self):
        pass
    
    def GET(self):
        if app.session.loggedin is True: # validate if the user is logged
            session_user = app.session.user
            session_privilege = app.session.privilege # get the session_privilege 
            if session_privilege == 0: # admin user
                return self.GET_INDEX() # call GET_INDEX() function
            else: # guess user
                raise config.web.seeother('/guess') # rendner guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INDEX():
        result = config.model_grupos_tutores_users.get_all_grupos_tutores_users().list() # get tutores_grupos table list
        for row in result:
            row.user = config.make_secure_val(str(row.user))
            row.id_tutor_grupo = config.make_secure_val(str(row.id_tutor_grupo)) # apply HMAC to id_tutor_grupo (primary key)
        return config.render.index(result) # render tutores_grupos index.html
