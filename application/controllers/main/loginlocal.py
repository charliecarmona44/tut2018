from . import config
import app
import hashlib
import web


class LoginLocal:
    def __init__(self):
        pass

    @staticmethod
    def GET(*a):
        message = None
        return config.render.loginlocal(message)

    @staticmethod
    def POST(*a):
        i = config.web.input()
        
        check = config.model_users.validate_user(i.user,i.other_data)
        if check:
            app.session.loggedin = True
            app.session.user = check['user']
            app.session.privilege = check['privilege']
            
        

            ip = web.ctx['ip']
 
            #res = config.model_logs.insert_logs(check['user'], ip)
    
            if check['privilege'] == 0:
                user = app.session.user 
                privilege = app.session.privilege 
                params = {}
                params['user']= user
                params['privilege']= privilege
                return config.render.admin(params)

            if check['privilege'] == 1:
                user = app.session.user 
                privilege = app.session.privilege 
                params = {}
                params['user']= user
                params['privilege']= privilege
                return config.render.admin(params)

            if check['privilege'] == 2:
                user = app.session.user 
                privilege = app.session.privilege 
                params = {}
                params['user']= user
                params['privilege']= privilege
                return config.render.admin(params) 


                
        else:
            message = "User or Password are not correct!!!!"
            return config.render.loginlocal(message)