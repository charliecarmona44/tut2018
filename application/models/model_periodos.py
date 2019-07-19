import web
import config

db = config.db


def get_all_periodos():
    try:
        return db.select('periodos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_periodos(id_periodo):
    try:
        return db.select('periodos', where='id_periodo=$id_periodo', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_periodos(id_periodo):
    try:
        return db.delete('periodos', where='id_periodo=$id_periodo', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_periodos(periodo):
    try:
        return db.insert('periodos',periodo=periodo)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_periodos(id_periodo,periodo):
    try:
        return db.update('periodos',id_periodo=id_periodo,
periodo=periodo,
                  where='id_periodo=$id_periodo',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
