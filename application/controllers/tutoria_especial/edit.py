import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_tutoria_especial, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_tutoria_especial) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_tutoria_especial, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_tutoria_especial) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_tutoria_especial, **k):

    @staticmethod
    def POST_EDIT(id_tutoria_especial, **k):
        
    '''

    def GET(self, id_tutoria_especial, **k):
        message = None # Error message
        id_tutoria_especial = config.check_secure_val(str(id_tutoria_especial)) # HMAC id_tutoria_especial validate
        result = config.model.get_tutoria_especial(int(id_tutoria_especial)) # search for the id_tutoria_especial
        result.id_tutoria_especial = config.make_secure_val(str(result.id_tutoria_especial)) # apply HMAC for id_tutoria_especial
        return config.render.edit(result, message) # render tutoria_especial edit.html

    def POST(self, id_tutoria_especial, **k):
        form = config.web.input()  # get form data
        form['id_tutoria_especial'] = config.check_secure_val(str(form['id_tutoria_especial'])) # HMAC id_tutoria_especial validate
        # edit user with new data
        result = config.model.edit_tutoria_especial(
            form['id_tutoria_especial'],form['id_area_atencion'],form['email'],form['user'],form['id_grupo'],form['id_programa_educativo'],form['fecha'],form['motivo_tutoria'],form['acciones'],form['resolucion_tutoria'],form['nota'],
        )
        if result == None: # Error on udpate data
            id_tutoria_especial = config.check_secure_val(str(id_tutoria_especial)) # validate HMAC id_tutoria_especial
            result = config.model.get_tutoria_especial(int(id_tutoria_especial)) # search for id_tutoria_especial data
            result.id_tutoria_especial = config.make_secure_val(str(result.id_tutoria_especial)) # apply HMAC to id_tutoria_especial
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/tutoria_especial') # render tutoria_especial index.html
