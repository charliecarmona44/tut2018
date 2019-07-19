import web
import config

db = config.db


def get_all_area_atencion():
    try:
        return db.select('area_atencion')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_area_atencion(id_area_atencion):
    try:
        return db.select('area_atencion', where='id_area_atencion=$id_area_atencion', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_area_atencion(id_area_atencion):
    try:
        return db.delete('area_atencion', where='id_area_atencion=$id_area_atencion', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_area_atencion(area,descripcion):
    try:
        return db.insert('area_atencion',area=area,
descripcion=descripcion)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_area_atencion(id_area_atencion,area,descripcion):
    try:
        return db.update('area_atencion',id_area_atencion=id_area_atencion,
area=area,
descripcion=descripcion,
                  where='id_area_atencion=$id_area_atencion',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
