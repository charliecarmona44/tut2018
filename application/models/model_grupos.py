import web
import config

db = config.db

def buscarclave(clave_grupo):
    try:
        return db.select('grupos', where='clave_grupo=$clave_grupo',vars=locals())[0]
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def validate_id(clave_grupo):
    try:
        return db.select('grupos', what='id_grupo', where='clave_grupo=$clave_grupo',vars=locals())[0]
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None

def search_grup(id_grupo):
    try:
        return db.select('grupos', what="id_grupo", where='id_grupo=$id_grupo', vars=locals())[0]
    except Exception as e:
          print "Model get all Error {}".format(e.args)
          print "Model get all Message {}".format(e.message)
          return None

def get_all_grupos():
    try:
        return db.select('grupos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_grupos(id_grupo):
    try:
        return db.select('grupos', where='id_grupo=$id_grupo', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_grupos(id_grupo):
    try:
        return db.delete('grupos', where='id_grupo=$id_grupo', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_grupos(id_programa_educativo,id_periodo,grupo,clave_grupo):
    try:
        return db.insert('grupos',id_programa_educativo=id_programa_educativo,
id_periodo=id_periodo,
grupo=grupo,
clave_grupo=clave_grupo)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_grupos(id_grupo,id_programa_educativo,id_periodo,grupo,clave_grupo):
    try:
        return db.update('grupos',id_grupo=id_grupo,
id_programa_educativo=id_programa_educativo,
id_periodo=id_periodo,
grupo=grupo,
clave_grupo=clave_grupo,
                  where='id_grupo=$id_grupo',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
