import config
import app


class Alumnos:
    def __init__(self):
        pass

    def GET(self):
        if app.session.loggedin is True:
            user = app.session.user
            privilege = app.session.privilege
            params = {}
            params['user'] = user
            params['privilege'] = privilege
            
            if privilege == 0: # admin
                return self.GET_ALUMNOS()
            elif privilege == 1: # tutor
                return self.GET_ALUMNOS()
            elif privilege == 2: # docente
                return self.GET_ALUMNOS()
            elif privilege == 3: #alumno
                raise config.web.seeother('/')
            elif privilege == 4: #alumno inscrito
                raise config.web.seeother('/')
        else:
            params = {}
            params['user'] = 'anonymous'
            params['privilege'] = '-1'
            raise config.web.seeother('/login')

    @staticmethod
    def GET_ALUMNOS():
        result = config.model_alumnos_grupos.get_all_alumnos_grupos().list()
        for row in result:
            row.email = config.make_secure_val(str(row.email))
        return config.render.alumnos(result)