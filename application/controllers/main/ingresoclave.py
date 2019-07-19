import config
import app
import hashlib
import web
import auth
import json


class ValidacionClave:


        def __init__(self):
               pass
        

        @staticmethod
        def GET(*a):
            message = None
            return config.render.ingresoclave(message)
           
        @staticmethod
        def POST(*a):	
              email =app.session.user
              user = app.session.user
              privilege = app.session.privilege 

              i = config.web.input()
              clave_grupo=i.clave_grupo

              verificar = config.model_grupos.buscarclave(clave_grupo)
              if verificar:
                    grupo=config.model_grupos.validate_id(clave_grupo)
                    app.session.clave_grupo=clave_grupo
                    raise config.web.seeother('/alumnos/insert')


                    #@staticmethod
                    #def grupo(grupo):
                        #self.grupo=grupo
                        #return grupo                     
              else:
              #essage = "La clave no es invalida que sea correcta"
              #eturn config.render.ingresoclave(message)
                    message="Password are not correct!!!!!!"
                    raise config.render.ingresoclave(message)

        