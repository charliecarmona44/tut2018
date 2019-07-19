"""
    Class for update users
"""
from . import config
import hashlib
import app


class Edit:

    def __init__(self):
        pass

    def GET(self, user, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(user) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, user, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(user) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(user, **k):
        message = None # Error message
        user = config.check_secure_val(str(user)) # HMAC user validate
        result = config.model.get_users(user) # search for the user
        result.user = config.make_secure_val(str(result.user)) # apply HMAC for username
        return config.render.edit(result, message) # render edit.html
    
    @staticmethod
    def POST_EDIT(user, **k):
        form = config.web.input() # get form data
        user = config.check_secure_val(str(user)) # HMAC user validate
        user = config.model.get_users(user)  # search for the user
    

        

        user_hash = hashlib.md5(form.user + config.secret_key).hexdigest() # create a new user_hash

        form.user = config.check_secure_val(str(form.user)) # validate HMAC username

        # edit user with new data
        result = config.model.edit_users(
            form['user'],
            form['privilege'],
            form['status'],
            form['name'],
            form['email'],
            form['other_data'],
            user_hash
            
        )
        if result == None: # Error on udpate values
            user = config.check_secure_val(str(user)) # validate HMAC username
            result = config.model.get_users(user) # search for username data
            result.user = config.make_secure_val(str(result.user)) # apply HMAC to username
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/users') # render users index.html