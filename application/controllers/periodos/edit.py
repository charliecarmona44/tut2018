import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_periodo, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_periodo) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_periodo, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_periodo) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_periodo, **k):

    @staticmethod
    def POST_EDIT(id_periodo, **k):
        
    '''

    def GET(self, id_periodo, **k):
        message = None # Error message
        id_periodo = config.check_secure_val(str(id_periodo)) # HMAC id_periodo validate
        result = config.model.get_periodos(int(id_periodo)) # search for the id_periodo
        result.id_periodo = config.make_secure_val(str(result.id_periodo)) # apply HMAC for id_periodo
        return config.render.edit(result, message) # render periodos edit.html

    def POST(self, id_periodo, **k):
        form = config.web.input()  # get form data
        form['id_periodo'] = config.check_secure_val(str(form['id_periodo'])) # HMAC id_periodo validate
        # edit user with new data
        result = config.model.edit_periodos(
            form['id_periodo'],form['periodo'],
        )
        if result == None: # Error on udpate data
            id_periodo = config.check_secure_val(str(id_periodo)) # validate HMAC id_periodo
            result = config.model.get_periodos(int(id_periodo)) # search for id_periodo data
            result.id_periodo = config.make_secure_val(str(result.id_periodo)) # apply HMAC to id_periodo
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/periodos') # render periodos index.html
