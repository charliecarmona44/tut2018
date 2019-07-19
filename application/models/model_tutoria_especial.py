import web
import config

db = config.db


def get_all_tutoria_especial():
    try:
        return db.select('tutoria_especial')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_tutoria_especial(id_tutoria_especial):
    try:
        return db.select('tutoria_especial', where='id_tutoria_especial=$id_tutoria_especial', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_tutoria_especial(id_tutoria_especial):
    try:
        return db.delete('tutoria_especial', where='id_tutoria_especial=$id_tutoria_especial', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_tutoria_especial(id_area_atencion,email,user,id_grupo,id_programa_educativo,fecha,motivo_tutoria,acciones,resolucion_tutoria,nota):
    try:
        return db.insert('tutoria_especial',id_area_atencion=id_area_atencion,
email=email,
user=user,
id_grupo=id_grupo,
id_programa_educativo=id_programa_educativo,
fecha=fecha,
motivo_tutoria=motivo_tutoria,
acciones=acciones,
resolucion_tutoria=resolucion_tutoria,
nota=nota)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_tutoria_especial(id_tutoria_especial,id_area_atencion,email,user,id_grupo,id_programa_educativo,fecha,motivo_tutoria,acciones,resolucion_tutoria,nota):
    try:
        return db.update('tutoria_especial',id_tutoria_especial=id_tutoria_especial,
id_area_atencion=id_area_atencion,
email=email,
user=user,
id_grupo=id_grupo,
id_programa_educativo=id_programa_educativo,
fecha=fecha,
motivo_tutoria=motivo_tutoria,
acciones=acciones,
resolucion_tutoria=resolucion_tutoria,
nota=nota,
                  where='id_tutoria_especial=$id_tutoria_especial',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
