import config
import hashlib
import app

class Insert:

    def __init__(self):
        pass

    def GET(self):
        if app.session.loggedin is True:
            email = app.session.user
            privilege = app.session.privilege  # get the session_privilege
            if privilege == 4: # admin user
              return self.GET_INSERT() # call GET_INSERT() function
            else: # guess user
              raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            privilege = app.session.privilege # get the session_privilege
            if privilege == 4: # admin user
                return self.POST_INSERT() # call POST_EDIT function
            else: # guess user
                raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html


    @staticmethod
    def GET_INSERT():
        message = None 
        email = app.session.user
        return config.render.insert(email,message) # render insert.html

    @staticmethod
    def POST_INSERT():
        form = config.web.input() # get form data

        # call model insert_trayectorias_academicas and try to insert new data
        config.model.insert_trayectorias_academicas(
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

        app.session.loggedin = True
        app.session.user 
        app.session.privilege = 4 
        raise config.web.seeother('/alumnos/index_alumno') # render trayectorias_academicas index.html
