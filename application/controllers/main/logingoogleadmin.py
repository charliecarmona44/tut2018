from . import config
import app
import hashlib
import web
import auth2
import json

auth2.parameters['google']['app_id'] = '364672633912-k1rhmfhnpchf0852frr3qchbl4jgaub1.apps.googleusercontent.com'
auth2.parameters['google']['app_secret'] = 'Hcdet2iG5b30YIP77eA343cw'


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
class handler(auth2.handler):
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

    raise web.seeother('/logingoogleadmin') #redireccion asi entorno de usuario no de la raiz


class AuthPage(handler):
  def GET(self, provider):
    self.auth_init(provider)


class AuthCallbackPage(handler):
  def GET(self, provider):
    self.auth_callback(provider)


#clase principal 
class LoginPage:


 # @staticmethod
  #def GET(self, message):
        #message = None
        #return config.render.index(message)

  #@staticmethod
  def GET(self):
         #i = config.web.input()
  #def GET(self):
    # check '_id' in the cookie to see if the user already sign in
    if web.cookies().get('_id'):
      # user already sign in, retrieve user profile
      #transformacion de archivo json para leer y obtener perfil de usuario
      profile = json.loads( web.cookies().get('_profile'))
      #Obtencion de valor email del archivo json 
      user = profile['email'] 
      #emision de valor email de archivo json para ver html
      obtencion_email = profile['email'], json.dumps(user)
      #obtenido = json.dumps(email)
      #profiless = profile['email']

      #return """<html><head></head><body>
       # <a href="/logout">Salir de la aplicacion</a><br />
        #Hello <b><i>%s</i></b> Sus Datos son correctos usted registrado en cuenta GMAIL el correo obtenido de su cuenta es el siguiente:<br/>
        #%s<br />
        #</body></html>
       #"""  % (obtencion_email) #impresion en html del correo obtenido
     
      check = config.model.validate_user(user)
      if check:
            app.session.loggedin = True
            app.session.user = check['user']
            app.session.privilege = check['privilege']
            app.session.picture = picture

            # get time now and N minutes
            now = datetime.datetime.now()
            future = now + datetime.timedelta(minutes = app.expires)
            future_str = str(future).split('.')[0]
            app.session.expires = config.make_secure_val(future_str)

            ip = web.ctx['ip']

            config.model_logs.insert_logs(check['user'], ip)

           
            params = {}
            params['user'] = app.session.user
            params['privilege'] = app.session.privilege
            params['picture'] = app.session.picture

            if check['privilege'] == 1:
               return config.render.admin(params)   


            # Estado usuario desactivado 
            if check['status'] == 0:
                message = check['user'] + ": User account disabled!!!!"
                app.session.loggedin = False
                app.session.user = 'anonymous'
                app.session.privilege = -1 #asignar privilegio solo para pagina de introduccion
                app.session.picture = None
                app.session.kill()#destruir la session de kuorra
                web.setcookie('_id', '', 0)#cierre de session en google 
                print message
                return config.render.login(message)
            else:
                raise config.web.seeother('/')

      # usuario no registrado
      if check==None:
        message = user + ": User not found"
        app.session.loggedin = False
        app.session.user = 'anonymous'
        app.session.privilege = -1 #asignar privilegio solo para pagina de introduccion
        app.session.picture = None
        app.session.kill()#destruir la session de kuorra
        web.setcookie('_id', '', 0)#cierre de session en google 
        
        print  message
        return config.render.login(message)
        # raise config.web.seeother('/logout')
    
    else:
      raise web.seeother('/auth/google')
      #return  redirect('/auth/google')


       
