import web
import config

db = config.db


def get_all_alumnos_grupos():
    try:
        return db.select('alumnos_grupos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_alumnos_grupos(id_grupo):
    try:
        return db.select('alumnos_grupos', where='id_grupo=$id_grupo', vars=locals())
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None

def get_alumno(matricula):
    try:
        return db.select('alumnos_grupos', where='matricula=$matricula', vars=locals())
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)