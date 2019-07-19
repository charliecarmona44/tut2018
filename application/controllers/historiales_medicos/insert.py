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

        # call model insert_historiales_medicos and try to insert new data
        config.model.insert_historiales_medicos(
            form['email'],
            form['imss'],
            form['no_imss'],
            form['institucion_salud'],
            form['nombre_institucion_salud'],
            form['no_afiliacion_otra'],
            form['tipo_sangre'],
            form['alergias'],
            form['descripcion_alergias'],
            form['enfermedades'],
            form['descripcion_enfermedad'],
            form['medicamentos'],
            form['descripcion_medicamentos'],
        )
        #raise config.web.seeother('/padres_tutores/insert') # render historiales_medicos index.html
         
        app.session.loggedin = True
        app.session.user 
        app.session.privilege = 4 
        raise config.web.seeother('/alumnos/index_alumno') # render trayectorias_academicas index.html
