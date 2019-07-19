import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, id_padre_tutor, message=None):
        if app.session.loggedin is True: # validate if the user is logged
            user = app.session.user
            privilege = app.session.privilege # get the session_privilege
            params = {}
            params['user'] = user
            params['privilege'] = privilege
            if privilege == 4: # admin user
                return self.GET_EDIT(id_padre_tutor,params,message) # call GET_EDIT function
            elif privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_padre_tutor, message=None):
        if app.session.loggedin is True: # validate if the user is logged
            user = app.session.user
            privilege = app.session.privilege
            params = {}
            params['user'] = user
            params['privilege'] = privilege
             # get the session_privilege
            if privilege == 4: # admin user
                return self.POST_EDIT(id_padre_tutor,params,message) # call POST_EDIT function
            elif privilege == 0: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    
   
        
    @staticmethod
    def GET_EDIT(id_padre_tutor, params, message):
        message = None # Error message
        
        result = config.model.get_padres_tutores(id_padre_tutor) # search for the id_padre_tutor
    
        return config.render.edit(result,params,message) # render padres_tutores edit.html



    @staticmethod
    def POST_EDIT(id_padre_tutor, params, message):
    
        form = config.web.input()  # get form data
         # HMAC id_padre_tutor validate
        # edit user with new data
        result = config.model.edit_padres_tutores(
            form['id_padre_tutor'],
            form['email'],
            form['nombre'],
            form['ap_paterno'],
            form['ap_materno'],
            form['parentesco'],
            form['telefono_celular'],
            form['telefono_casa'],
            form['telefono_trabajo'],
            form['email_tutor'],
            form['calle'],
            form['colonia'],
            form['cp'],
            form['no_exterior'],
            form['no_interior'],
            form['municipio'],
            form['referencias'],
        )
        
        raise config.web.seeother('/alumnos/index_alumno')
