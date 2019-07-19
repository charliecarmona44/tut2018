import web
import config

db = config.db


def get_all_grupos_tutores_users():
    try:
        return db.select('grupos_tutores_users')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_grupos_tutores_users():
    try:
        return db.select('grupos_tutores_users', where='=$', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None
