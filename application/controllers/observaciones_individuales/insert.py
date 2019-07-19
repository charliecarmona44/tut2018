import config
import app
import datetime

class Insert():
    def __init__(self):
        pass

    def GET(self, email):
        if app.session.loggedin is True:
            user = app.session.user
            privilege = app.session.privilege
            params = {}
            params['user'] = user
            params['privilege'] = privilege
            
            if privilege == 0: # admin
                return self.GET_INSERT(email)
            elif privilege == 1: # tutor
                return self.GET_INSERT(email)
            elif privilege == 2: # docente
                return self.GET_INSERT(email)
            elif privilege == 3: #alumno
                raise config.web.seeother('/')
            elif privilege == 4: #alumno inscrito
                raise config.web.seeother('/')
        else:
            params = {}
            params['username'] = 'anonymous'
            params['privilege'] = '-1'
            raise config.web.seeother('/login')

    def POST(self, email):
        if app.session.loggedin is True:
            user = app.session.user
            privilege = app.session.privilege
            params = {}
            params['user'] = user
            params['privilege'] = privilege
            
            if privilege == 0: # admin
                return self.POST_INSERT(email)
            elif privilege == 1: # tutor
                return self.POST_INSERT(email)
            elif privilege == 2: # docente
                return self.POST_INSERT(email)
            elif privilege == 3: #alumno
                raise config.web.seeother('/')
        else:
            params = {}
            params['user'] = 'anonymous'
            params['privilege'] = '-1'
            raise config.web.seeother('/login')

    @staticmethod
    def GET_INSERT(email):
        email = config.check_secure_val(str(email))     
        alumno = config.model_alumnos.get_alumnos(email)
        username = app.session.user
        #username = config.check_secure_val(app.session.user)
        email = config.model_users.get_users(username)
        return config.render.insert(alumno, email)
    
    @staticmethod
    def POST_INSERT(email):
        form = config.web.input()
        now = datetime.datetime.now()
        config.model.insert_observaciones_individuales(
            form['email'],
            form['user'],
            now,
            form['observaciones'],
            form['fecha_atencion'],
            form['acciones'],
            form['resultados'],
            form['semaforo'],
        )
        raise config.web.seeother('/observaciones_individuales')