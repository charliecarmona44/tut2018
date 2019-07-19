import config
import hashlib
import app

class HistorialesMedicosIngreso:
    
    def __init__(self):
        pass
   ##### validacion de existencia y raise a direccion de ingreso a formularios 
    def GET(self):
        email=app.session.user
        busqueda = config.model.validar_historial_medico(email)
        if busqueda:
           historiales_medicos = busqueda

           params={}
           params['privilege']= app.session.privilege
           params['user'] = email
           message = None 
           return config.web.seeother('/historiales_medicos')
        if busqueda == None:
           return config.web.seeother('/historiales_medicos/insert')