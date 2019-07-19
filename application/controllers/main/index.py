from . import config
import app
import datetime

class Index:
    
    def __init__(self):
        pass


    @staticmethod
    def GET():
        if app.session.loggedin is True:
           
            #now = datetime.datetime.now()
            #now_str = str(now).split('.')[0]

            #expires = config.check_secure_val(app.session.expires)

            #print "now    : " , now_str
            #print "expires: " , expires

            #if (now_str > expires): # compare now with time login
                #raise config.web.seeother('/logout')

            user = app.session.user
            privilege = app.session.privilege
            picture = app.session.picture
            params = {}
            params['user'] = user
            params['privilege'] = privilege
            params['picture'] = picture
            if privilege == 0:   #admin
                return config.render.admin(params)
            elif privilege == 1: #coordinador_tutoria
                return config.render.guess(params)
            elif privilege == 2: #tutor
                return config.render.admin(params)
            elif privilege == 3: #alumno
                raise config.web.seeother('/ingresoclave')
            elif privilege == 4: #alumno inscrito
                raise config.web.seeother('/alumnos/index_alumno')
            elif privilege == 5: #guess
                raise config.web.admin(params)   
         
        else:
            message = None
            params = {}
            params['user'] = 'anonymous'
            params['privilege'] = '-1'
            return config.render.index(params, message)
