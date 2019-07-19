import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, id_historial_medico, message=None):
        if app.session.loggedin is True: # validate if the user is logged
            session_user = app.session.user
            session_privilege = app.session.privilege # get the session_privilege
            message = None
            params = {}
            params['user'] = session_user
            params['privilege'] = session_privilege
            if session_privilege == 4: # admin user
                return self.GET_EDIT(id_historial_medico,params,message) # call GET_EDIT function
            elif session_privilege == 0: # guess user
                return self.GET_EDIT(id_historial_medico,params,message)
        else: # the user dont have logged
            raise config.web.seeother('/') # render login.html

    def POST(self, id_historial_medico, message=None):
        if app.session.loggedin is True: # validate if the user is logged
            session_user = app.session.user
            session_privilege = app.session.privilege # get the session_privilege
            message = None
            params = {}
            params['user'] = session_user
            params['privilege'] = session_privilege
            if session_privilege == 4: # admin user
                return self.POST_EDIT(id_historial_medico,params,message) # call POST_EDIT function
            elif session_privilege == 0: # guess user
                return self.GET_EDIT(id_historial_medico,params,mesage)
        else: # the user dont have logged
            raise config.web.seeother('/') # render login.html

   

    
        
    
    @staticmethod
    def GET_EDIT(id_historial_medico, params, message):
        message = None # Error message
        result = config.model.get_historiales_medicos(id_historial_medico) # search for the id_historial_medico
        return config.render.edit(result,params,message) # render historiales_medicos edit.html


    @staticmethod
    def POST_EDIT(id_historial_medico, params, message):
        form = config.web.input()  # get form data
        
        # edit user with new data
        result = config.model.edit_historiales_medicos(
            form['id_historial_medico'],
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
        
        raise config.web.seeother('/alumnos/index_alumno')