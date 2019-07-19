import config
import hashlib
import app

class PadresTutoresIngreso:
    
    def __init__(self):
        pass
   ##### validacion de existencia y raise a direccion de ingreso a formularios 
    def GET(self):
        email=app.session.user
        busqueda = config.model.validar_padres_tutores(email)
        if busqueda:
           padres_tutores = busqueda

           params={}
           params['privilege']= app.session.privilege
           params['user'] = email
           message = None 
           return config.web.seeother('/padres_tutores')
        if busqueda == None:
           return config.web.seeother('/padres_tutores/insert')