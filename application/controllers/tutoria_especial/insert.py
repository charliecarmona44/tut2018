import config
import hashlib
import app

class Insert:

    def __init__(self):
        pass

    '''
    def GET(self):
        if app.session.loggedin is True:
            # session_username = app.session.username
            session_username = app.session.privilege  # get the session_privilege
            if session_username == 0: # admin user
                return self.GET_INSERT() # call GET_INSERT() function
            elif session_username == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_username = app.session.privilege # get the session_privilege
            if session_username == 0: # admin user
                return self.POST_INSERT() # call POST_EDIT function
            elif privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INSERT():

    @staticmethod
    def POST_INSERT():
    '''

    def GET(self):
        programas_educativos = config.model_programas_educativos.get_all_programas_educativos()
        grupos = config.model_grupos.get_all_grupos()
        users =  config.model_users.get_all_users()
        alumnos = config.model_alumnos.get_all_alumnos()
        area = config.model_area_atencion.get_all_area_atencion()

        return config.render.insert(programas_educativos,grupos,users,alumnos,area) # render insert.html


    def POST(self):
        form = config.web.input() # get form data

        # call model insert_tutoria_especial and try to insert new data
        config.model.insert_tutoria_especial(
            form['id_area_atencion'],
            form['email'],
            form['user'],
            form['id_grupo'],
            form['id_programa_educativo'],
            form['fecha'],
            form['motivo_tutoria'],
            form['acciones'],
            form['resolucion_tutoria'],
            form['nota'],
        )
        raise config.web.seeother('/tutoria_especial') # render tutoria_especial index.html
