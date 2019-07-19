import web
import config

db = config.db


def get_all_alumnos_observaciones():
    try:
        return db.select('alumnos_observaciones')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None