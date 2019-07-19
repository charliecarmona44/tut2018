import web
import config

db = config.db


def validar_aspectos_economicos(email):
    try:
        return db.select('aspectos_economicos', where='email=$email', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def get_all_aspectos_economicos():
    try:
        return db.select('aspectos_economicos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_aspectos_economicos(id_aspecto_economico):
    try:
        return db.select('aspectos_economicos', where='id_aspecto_economico=$id_aspecto_economico', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_aspectos_economicos(id_aspecto_economico):
    try:
        return db.delete('aspectos_economicos', where='id_aspecto_economico=$id_aspecto_economico', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_aspectos_economicos(email,beca,nombre_beca,depende_economicamente,tiene_computadora,tiene_telefono,trabaja,empresa,jefe_inmediato,telefono_trabajo,email_trabajo,actividad,jornada_laboral,calle,colonia,cp,no_exterior,no_interior,municipio,referencias):
    try:
        return db.insert('aspectos_economicos',email=email,
beca=beca,
nombre_beca=nombre_beca,
depende_economicamente=depende_economicamente,
tiene_computadora=tiene_computadora,
tiene_telefono=tiene_telefono,
trabaja=trabaja,
empresa=empresa,
jefe_inmediato=jefe_inmediato,
telefono_trabajo=telefono_trabajo,
email_trabajo=email_trabajo,
actividad=actividad,
jornada_laboral=jornada_laboral,
calle=calle,
colonia=colonia,
cp=cp,
no_exterior=no_exterior,
no_interior=no_interior,
municipio=municipio,
referencias=referencias)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_aspectos_economicos(id_aspecto_economico,email,beca,nombre_beca,depende_economicamente,tiene_computadora,tiene_telefono,trabaja,empresa,jefe_inmediato,telefono_trabajo,email_trabajo,actividad,jornada_laboral,calle,colonia,cp,no_exterior,no_interior,municipio,referencias):
    try:
        return db.update('aspectos_economicos',id_aspecto_economico=id_aspecto_economico,
email=email,
beca=beca,
nombre_beca=nombre_beca,
depende_economicamente=depende_economicamente,
tiene_computadora=tiene_computadora,
tiene_telefono=tiene_telefono,
trabaja=trabaja,
empresa=empresa,
jefe_inmediato=jefe_inmediato,
telefono_trabajo=telefono_trabajo,
email_trabajo=email_trabajo,
actividad=actividad,
jornada_laboral=jornada_laboral,
calle=calle,
colonia=colonia,
cp=cp,
no_exterior=no_exterior,
no_interior=no_interior,
municipio=municipio,
referencias=referencias,
                  where='id_aspecto_economico=$id_aspecto_economico',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
