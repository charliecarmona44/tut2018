import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, id_programa_educativo, message=None):
        if app.session.loggedin is True: # validate if the user is logged
            session_username = app.session.user
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_programa_educativo, message) # call GET_EDIT function
            else: # guess user
                raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_programa_educativo, message=None):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_programa_educativo) # call POST_EDIT function
            else: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_programa_educativo, message=None):
        message = None # Error message
        id_programa_educativo = config.check_secure_val(str(id_programa_educativo)) # HMAC id_programa_educativo validate
        result = config.model.get_programas_educativos(int(id_programa_educativo)) # search for the id_programa_educativo
        result.id_programa_educativo = config.make_secure_val(str(result.id_programa_educativo)) # apply HMAC for id_programa_educativo
        return config.render.edit(result, message) # render programas_educativos edit.html





    @staticmethod
    def POST_EDIT(id_programa_educativo, message=None):
        form = config.web.input()  # get form data
        form['id_programa_educativo'] = config.check_secure_val(str(form['id_programa_educativo'])) # HMAC id_programa_educativo validate
        # edit user with new data
        result = config.model.edit_programas_educativos(
            form['id_programa_educativo'],form['programa'],
        )
        if result == None: # Error on udpate data
            id_programa_educativo = config.check_secure_val(str(id_programa_educativo)) # validate HMAC id_programa_educativo
            result = config.model.get_programas_educativos(int(id_programa_educativo)) # search for id_programa_educativo data
            result.id_programa_educativo = config.make_secure_val(str(result.id_programa_educativo)) # apply HMAC to id_programa_educativo
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/programas_educativos') # render programas_educativos index.html
    

    
        

            
