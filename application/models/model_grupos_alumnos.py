import web
import config

db = config.db


def get_all_grupos_alumnos():
    try:
        return db.select('grupos_alumnos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_grupos_alumnos(id_grupos_alumnos):
    try:
        return db.select('grupos_alumnos', where='id_grupos_alumnos=$id_grupos_alumnos', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_grupos_alumnos(id_grupos_alumnos):
    try:
        return db.delete('grupos_alumnos', where='id_grupos_alumnos=$id_grupos_alumnos', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_grupos_alumnos(id_grupo,email):
    try:
        return db.insert('grupos_alumnos',id_grupo=id_grupo,
email=email)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_grupos_alumnos(id_grupos_alumnos,id_grupo,email):
    try:
        return db.update('grupos_alumnos',id_grupos_alumnos=id_grupos_alumnos,
id_grupo=id_grupo,
email=email,
                  where='id_grupos_alumnos=$id_grupos_alumnos',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
