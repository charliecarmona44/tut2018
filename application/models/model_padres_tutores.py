import web
import config

db = config.db


def validar_padres_tutores(email):
    try:
        return db.select('padres_tutores', where='email=$email', vars=locals())[0]
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_all_padres_tutores():
    try:
        return db.select('padres_tutores')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_padres_tutores(id_padre_tutor):
    try:
        return db.select('padres_tutores', where='id_padre_tutor=$id_padre_tutor', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_padres_tutores(id_padre_tutor):
    try:
        return db.delete('padres_tutores', where='id_padre_tutor=$id_padre_tutor', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_padres_tutores(email,nombre,ap_paterno,ap_materno,parentesco,telefono_celular,telefono_casa,telefono_trabajo,email_tutor,calle,colonia,cp,no_exterior,no_interior,municipio,referencias):
    try:
        return db.insert('padres_tutores',email=email,
nombre=nombre,
ap_paterno=ap_paterno,
ap_materno=ap_materno,
parentesco=parentesco,
telefono_celular=telefono_celular,
telefono_casa=telefono_casa,
telefono_trabajo=telefono_trabajo,
email_tutor=email_tutor,
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


def edit_padres_tutores(id_padre_tutor,email,nombre,ap_paterno,ap_materno,parentesco,telefono_celular,telefono_casa,telefono_trabajo,email_tutor,calle,colonia,cp,no_exterior,no_interior,municipio,referencias):
    try:
        return db.update('padres_tutores',id_padre_tutor=id_padre_tutor,
email=email,
nombre=nombre,
ap_paterno=ap_paterno,
ap_materno=ap_materno,
parentesco=parentesco,
telefono_celular=telefono_celular,
telefono_casa=telefono_casa,
telefono_trabajo=telefono_trabajo,
email_tutor=email_tutor,
calle=calle,
colonia=colonia,
cp=cp,
no_exterior=no_exterior,
no_interior=no_interior,
municipio=municipio,
referencias=referencias,
                  where='id_padre_tutor=$id_padre_tutor',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
