from . import config
import app
import hashlib
import web
import auth
import json

# Valores asignados de id_cliente proporcionado por el proveedor en este caso google
# En caso de trabajar con otros provedores como Facebook se cambiaran los valores 
# En caso de trabajar con dos o mas provedores al mismo tiempo se tendran valores asiganados independientes por cada proveedor  
auth.parameters['google']['app_id'] = '364672633912-hbhtatjd9kbkbeaocn0902pivum4t0cd.apps.googleusercontent.com'#ID_cliente
auth.parameters['google']['app_secret'] = 'b_HGPbqiY-gBHSCBuS38fVau'#Secret_del_cliente  


class Login:
    def __init__(self):
        pass
    
     #@staticmethod
     #def GET(*a):
     #   message = None
     #   return config.render.login(message)

    #@staticmethod
    #def POST(*a):
         #i = config.web.input()
class handler(auth.handler):
  def callback_uri(self, provider):
    """Please return appropriate url according to your app setting.
    """
    return 'http://localhost:8080/auth/%s/callback' % provider

  def on_signin(self, provider, profile):
    """Callback when the user successfully signs in the account of the provider
    (e.g., Google account or Facebook account).

    Arguments:
      provider: google or facebook
      profile: the user profile of Google or facebook account of the user who
               signs in.
    """
    user_id = '%s:%s' % (provider, profile['id'])

    # set '_id' in the cookie to sign-in the user in our webapp
  
    web.setcookie('_id', user_id)
    web.setcookie('_profile', json.dumps(profile))
    
    #redireccion a entorno de usuario de login 
    raise web.seeother('/login') 


class AuthPage(handler):
  def GET(self, provider):
    self.auth_init(provider)


class AuthCallbackPage(handler):
  def GET(self, provider):
    self.auth_callback(provider)



class LoginPage:
  #hd = ''
  def GET(self):

    #if
    hd = ''
    #if profile = json.loads( web.cookies().get('_profile'))

    #raise web.seeother('/logout')
    #profile = json.loads( web.cookies().get('_profile'))

    if web.cookies().get('_id'):
      
      
      profile = json.loads( web.cookies().get('_profile'))
      
      email = profile['email']
      picture = profile['picture']
      try:
        
      #hd = profile['hd']
         hd = profile['hd']
      except KeyError:
         pass
         web.setcookie('_id', '', 0)
         raise web.seeother('/logout')
      
      
      
      if hd == 'utectulancingo.edu.mx' or 'utec-tgo.edu.mx':
     
     
            verifica = config.model_alumnos.validate_alumno(email)
            if verifica:
                #grupo=config.model_alumnos.validate_id(email)
                #raise config.web.seeother('/alumno/index_alumno')
                
                app.session.loggedin = True
                app.session.user = email
                app.session.privilege = 4
                app.session.picture = picture
                app.session.grupo = ''
                raise config.web.seeother('/alumnos/index_alumno')




                

                ip = web.ctx['ip']
                res = config.model_logs.insert_logs(config.check_secure_val(email), ip)
                #raise web.seeother('/logout')
                now = datetime.datetime.now()
                future = now + datetime.timedelta(minutes = app.expires)
                future_str = str(future).split('.')[0]
                app.session.expires = config.make_secure_val(future_str)

            #ip = web.ctx['ip']

            #config.model_logs.insert_logs(check['user'], ip)
          

            if verifica==None:
                #message = email + ": User not found"
                #app.session.loggedin = True
                #app.session.user = email
                #app.session.privilege = 3
                #app.session.picture = None
                #raise web.seeother('/ingresoclave')
                check = config.model_users.validate_user_google(email)
                if check:
                    app.session.loggedin = True
                    app.session.user = check['user']
                    app.session.privilege = check['privilege']

                    if check['privilege'] == 0:
                       user = app.session.user 
                       privilege = app.session.privilege 
                       params = {}
                       params['user']= user
                       params['privilege']= privilege
                       return config.render.admin(params)
                       #raise config.web.seeother('/admin')

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
                     

              
                if check == None:
                    message = email + ": User not found"
                    app.session.loggedin = True
                    app.session.user = email
                    app.session.privilege = 3
                    app.session.picture = None
                    raise web.seeother('/ingresoclave')



            else:
                message = email + ": User not found"
                app.session.loggedin = True
                app.session.user = email
                app.session.privilege = 3
                app.session.picture = None
                raise web.seeother('/ingresoclave')

      if hd == '':
          checks = config.model_users.validate_user_google(email)
          if checks:
              app.session.loggedin = True
              app.session.user = check['user']
              app.session.privilege = check['privilege']

              if checks['privilege'] == 0:
                 user = app.session.user 
                 privilege = app.session.privilege 
                 params = {}
                 params['user']= user
                 params['privilege']= privilege
                 return config.render.admin(params)
                 #raise config.web.seeother('/admin')

              if checks['privilege'] == 1:
                 user = app.session.user 
                 privilege = app.session.privilege 
                 params = {}
                 params['user']= user
                 params['privilege']= privilege
                 return config.render.admin(params)

              if checks['privilege'] == 2:
                 user = app.session.user 
                 privilege = app.session.privilege 
                 params = {}
                 params['user']= user
                 params['privilege']= privilege
                 return config.render.admin(params)
                    
          if checks == None:
             web.setcookie('_id', '', 0)
             raise web.seeother('/logout')
             raise config.web.seeother('/index')#redireccion al index

    else:
      
      #raise web.seeother('/auth/google')
      raise web.seeother('/auth/google')


       
#https://accounts.google.com/Logout?
