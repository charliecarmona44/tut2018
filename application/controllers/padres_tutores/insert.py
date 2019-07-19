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

        # call model insert_padres_tutores and try to insert new data
        config.model.insert_padres_tutores(
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
        app.session.loggedin = True
        app.session.user 
        app.session.privilege = 4 
        raise config.web.seeother('/alumnos/index_alumno') # render trayectorias_academicas index.html

        #raise config.web.seeother('/trayectorias_academicas/insert') # render padres_tutores index.html
