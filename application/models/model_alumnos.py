import web
import config

db = config.db

def obtener_alumno(email):
    try:
        return db.select('alumnos', where='email=$email', vars=locals())[0]
    except Exception as e:
        print (("Model get all Error {}".format(e.args)))
        print (("Model get all Message {}".format(e.args)))
        return None 


def validate_alumno(email):
    try:
        return db.select('alumnos', where='email=$email', vars=locals())[0]
    except Exception as e:
        print (("Model get all Error {}".format(e.args)))
        print (("Model get all Message {}".format(e.args)))
        return None 
     
def validate_id(email):
    try:
        return db.select('alumnos', id_grupo, where='email=$email', vars=locals())[0]
    except Exception as e:
        print (("Model get all Error {}".format(e.args)))
        print (("Model get all Message {}".format(e.args)))
        return None 



def get_all_alumnos():
    try:
        return db.select('alumnos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_alumnos(email):
    try:
        return db.select('alumnos', where='email=$email', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_alumnos(email):
    try:
        return db.delete('alumnos', where='email=$email', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_alumnos(email,id_grupo,matricula,fecha_alta,nombre,ap_paterno,ap_materno,fecha_nacimiento,curp,cuatrimestre,telefono_celular,telefono_casa,email_institucional,email_personal,calle,colonia,cp,no_exterior,no_interior,municipio,referencias,idioma_principal,segundo_idioma):
    try:
        return db.insert('alumnos',email=email,
id_grupo=id_grupo,
matricula=matricula,
fecha_alta=fecha_alta,
nombre=nombre,
ap_paterno=ap_paterno,
ap_materno=ap_materno,
fecha_nacimiento=fecha_nacimiento,
curp=curp,
cuatrimestre=cuatrimestre,
telefono_celular=telefono_celular,
telefono_casa=telefono_casa,
email_institucional=email_institucional,
email_personal=email_personal,
calle=calle,
colonia=colonia,
cp=cp,
no_exterior=no_exterior,
no_interior=no_interior,
municipio=municipio,
referencias=referencias,
idioma_principal=idioma_principal,
segundo_idioma=segundo_idioma)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_alumnos(email,id_grupo,matricula,fecha_alta,nombre,ap_paterno,ap_materno,fecha_nacimiento,curp,cuatrimestre,telefono_celular,telefono_casa,email_institucional,email_personal,calle,colonia,cp,no_exterior,no_interior,municipio,referencias,idioma_principal,segundo_idioma):
    try:
        return db.update('alumnos',email=email,
id_grupo=id_grupo,
matricula=matricula,
fecha_alta=fecha_alta,
nombre=nombre,
ap_paterno=ap_paterno,
ap_materno=ap_materno,
fecha_nacimiento=fecha_nacimiento,
curp=curp,
cuatrimestre=cuatrimestre,
telefono_celular=telefono_celular,
telefono_casa=telefono_casa,
email_institucional=email_institucional,
email_personal=email_personal,
calle=calle,
colonia=colonia,
cp=cp,
no_exterior=no_exterior,
no_interior=no_interior,
municipio=municipio,
referencias=referencias,
idioma_principal=idioma_principal,
segundo_idioma=segundo_idioma,
                  where='email=$email',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
