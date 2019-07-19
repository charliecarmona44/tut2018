import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_observacion_individual, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_observacion_individual) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_observacion_individual, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_observacion_individual) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_observacion_individual, **k):

    @staticmethod
    def POST_EDIT(id_observacion_individual, **k):
        
    '''

    def GET(self, id_observacion_individual, **k):
        message = None # Error message
        id_observacion_individual = config.check_secure_val(str(id_observacion_individual)) # HMAC id_observacion_individual validate
        result = config.model.get_observaciones_individuales(int(id_observacion_individual)) # search for the id_observacion_individual
        result.id_observacion_individual = config.make_secure_val(str(result.id_observacion_individual)) # apply HMAC for id_observacion_individual
        return config.render.edit(result, message) # render observaciones_individuales edit.html

    def POST(self, id_observacion_individual, **k):
        form = config.web.input()  # get form data
        form['id_observacion_individual'] = config.check_secure_val(str(form['id_observacion_individual'])) # HMAC id_observacion_individual validate
        # edit user with new data
        result = config.model.edit_observaciones_individuales(
            form['id_observacion_individual'],form['email'],form['user'],form['fecha_observaciones'],form['observaciones'],form['fecha_atencion'],form['acciones'],form['resultados'],form['semaforo'],
        )
        if result == None: # Error on udpate data
            id_observacion_individual = config.check_secure_val(str(id_observacion_individual)) # validate HMAC id_observacion_individual
            result = config.model.get_observaciones_individuales(int(id_observacion_individual)) # search for id_observacion_individual data
            result.id_observacion_individual = config.make_secure_val(str(result.id_observacion_individual)) # apply HMAC to id_observacion_individual
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/observaciones_individuales') # render observaciones_individuales index.html
