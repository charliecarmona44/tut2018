import web
import config

db = config.db


def get_all_programas_educativos():
    try:
        return db.select('programas_educativos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_programas_educativos(id_programa_educativo):
    try:
        return db.select('programas_educativos', where='id_programa_educativo=$id_programa_educativo', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_programas_educativos(id_programa_educativo):
    try:
        return db.delete('programas_educativos', where='id_programa_educativo=$id_programa_educativo', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_programas_educativos(programa):
    try:
        return db.insert('programas_educativos',programa=programa)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_programas_educativos(id_programa_educativo,programa):
    try:
        return db.update('programas_educativos',id_programa_educativo=id_programa_educativo,
programa=programa,
                  where='id_programa_educativo=$id_programa_educativo',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
