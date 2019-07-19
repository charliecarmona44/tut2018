import web
import config

db = config.db


def validar_aspectos_personales(email):
    try:
        return db.select('aspectos_personales', where='email=$email', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None

        

def get_all_aspectos_personales():
    try:
        return db.select('aspectos_personales')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_aspectos_personales(id_aspecto_personal):
    try:
        return db.select('aspectos_personales', where='id_aspecto_personal=$id_aspecto_personal', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_aspectos_personales(id_aspecto_personal):
    try:
        return db.delete('aspectos_personales', where='id_aspecto_personal=$id_aspecto_personal', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_aspectos_personales(email,estado_civil,numero_hijos,quien_los_cuida,no_integrantes_familia,comunicacion_familiar,responsable,respetuosa,trabajo_equipo):
    try:
        return db.insert('aspectos_personales',email=email,
estado_civil=estado_civil,
numero_hijos=numero_hijos,
quien_los_cuida=quien_los_cuida,
no_integrantes_familia=no_integrantes_familia,
comunicacion_familiar=comunicacion_familiar,
responsable=responsable,
respetuosa=respetuosa,
trabajo_equipo=trabajo_equipo)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_aspectos_personales(id_aspecto_personal,email,estado_civil,numero_hijos,quien_los_cuida,no_integrantes_familia,comunicacion_familiar,responsable,respetuosa,trabajo_equipo):
    try:
        return db.update('aspectos_personales',id_aspecto_personal=id_aspecto_personal,
email=email,
estado_civil=estado_civil,
numero_hijos=numero_hijos,
quien_los_cuida=quien_los_cuida,
no_integrantes_familia=no_integrantes_familia,
comunicacion_familiar=comunicacion_familiar,
responsable=responsable,
respetuosa=respetuosa,
trabajo_equipo=trabajo_equipo,
                  where='id_aspecto_personal=$id_aspecto_personal',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
