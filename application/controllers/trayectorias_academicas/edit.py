import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, id_trayectoria_academica, message=None):
        if app.session.loggedin is True: # validate if the user is logged
            user = app.session.user
            privilege = app.session.privilege # get the session_privilege
            picture = app.session.picture
            params = {}
            params['user']=user
            params['privilege']=privilege
            params['picture']=picture
            if privilege == 4: # admin user
                return self.GET_EDIT(id_trayectoria_academica,params,message) # call GET_EDIT function
            elif privilege == 0: # guess user
                raise self.GET_EDIT(id_trayectoria_academica,params,message) # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/') # render login.html

    def POST(self, id_trayectoria_academica, message=None):
        if app.session.loggedin is True: # validate if the user is logged
            user = app.session.user
            privilege = app.session.privilege # get the session_privilege
            picture = app.session.picture
            params = {}
            params['user']=user
            params['privilege']=privilege
            params['picture']=picture # get the session_privilege
            if privilege == 4: # admin user
                return self.POST_EDIT(id_trayectoria_academica,params,message) # call POST_EDIT function
            elif privilege == 1: # guess user
                return self.POST_EDIT(id_trayectoria_academica,params,message) # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/') # render login.html

    

   
        
    @staticmethod
    def GET_EDIT(id_trayectoria_academica,params,message):
        message = None # Error message
         # HMAC id_trayectoria_academica validate
        result = config.model.get_trayectorias_academicas(id_trayectoria_academica) # search for the id_trayectoria_academica
         
        return config.render.edit(result,params,message) # render trayectorias_academicas edit.html

    @staticmethod
    def POST_EDIT(id_trayectoria_academica,params,message):
        form = config.web.input()  # get form data
         # HMAC id_trayectoria_academica validate
        # edit user with new data
        result = config.model.edit_trayectorias_academicas(
            form['id_trayectoria_academica'],
            form['email'],
            form['primaria_institucion'],
            form['primaria_promedio'],
            form['secundaria_institucion'],
            form['secundadria_promedio'],
            form['bachillerato_institucion'],
            form['bachillerato_promedio'],
            form['tsu_institucion'],
            form['tsu_promedio'],
            form['cuatrimestre_promedio01'],
            form['cuatrimestre_promedio02'],
            form['cuatrimestre_promedio03'],
            form['cuatrimestre_promedio04'],
            form['cuatrimestre_promedio05'],
            form['cuatrimestre_promedio06'],
            form['cuatrimestre_promedio07'],
            form['cuatrimestre_promedio08'],
            form['cuatrimestre_promedio09'],
            form['cuatrimestre_promedio10'],
        )
        
        raise config.web.seeother('/alumnos/index_alumno') # render trayectorias_academicas index.html
