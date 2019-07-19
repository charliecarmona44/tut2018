import config
import hashlib
import app

class TrayectoriasAcademicasIngreso:
    
     
    def __init__(self):
        pass
   ##### validacion de existencia y raise a direccion de ingreso a formularios 
    def GET(self):
        email=app.session.user
        busqueda = config.model.validar_trayectorias_academicas(email)
        if busqueda:
           trayectorias_academicas = busqueda

           params={}
           params['privilege']= app.session.privilege
           params['user'] = email
           message = None 
           return config.web.seeother('/trayectorias_academicas')
        if busqueda == None:
           return config.web.seeother('/trayectorias_academicas/insert')