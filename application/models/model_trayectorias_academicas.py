import web
import config

db = config.db

def validar_trayectorias_academicas(email):
    try:
        return db.select('trayectorias_academicas', where='email=$email', vars=locals())[0]
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_all_trayectorias_academicas():
    try:
        return db.select('trayectorias_academicas')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_trayectorias_academicas(id_trayectoria_academica):
    try:
        return db.select('trayectorias_academicas', where='id_trayectoria_academica=$id_trayectoria_academica', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_trayectorias_academicas(id_trayectoria_academica):
    try:
        return db.delete('trayectorias_academicas', where='id_trayectoria_academica=$id_trayectoria_academica', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_trayectorias_academicas(email,primaria_institucion,primaria_promedio,secundaria_institucion,secundadria_promedio,bachillerato_institucion,bachillerato_promedio,tsu_institucion,tsu_promedio,cuatrimestre_promedio01,cuatrimestre_promedio02,cuatrimestre_promedio03,cuatrimestre_promedio04,cuatrimestre_promedio05,cuatrimestre_promedio06,cuatrimestre_promedio07,cuatrimestre_promedio08,cuatrimestre_promedio09,cuatrimestre_promedio10):
    try:
        return db.insert('trayectorias_academicas',email=email,
primaria_institucion=primaria_institucion,
primaria_promedio=primaria_promedio,
secundaria_institucion=secundaria_institucion,
secundadria_promedio=secundadria_promedio,
bachillerato_institucion=bachillerato_institucion,
bachillerato_promedio=bachillerato_promedio,
tsu_institucion=tsu_institucion,
tsu_promedio=tsu_promedio,
cuatrimestre_promedio01=cuatrimestre_promedio01,
cuatrimestre_promedio02=cuatrimestre_promedio02,
cuatrimestre_promedio03=cuatrimestre_promedio03,
cuatrimestre_promedio04=cuatrimestre_promedio04,
cuatrimestre_promedio05=cuatrimestre_promedio05,
cuatrimestre_promedio06=cuatrimestre_promedio06,
cuatrimestre_promedio07=cuatrimestre_promedio07,
cuatrimestre_promedio08=cuatrimestre_promedio08,
cuatrimestre_promedio09=cuatrimestre_promedio09,
cuatrimestre_promedio10=cuatrimestre_promedio10)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_trayectorias_academicas(id_trayectoria_academica,email,primaria_institucion,primaria_promedio,secundaria_institucion,secundadria_promedio,bachillerato_institucion,bachillerato_promedio,tsu_institucion,tsu_promedio,cuatrimestre_promedio01,cuatrimestre_promedio02,cuatrimestre_promedio03,cuatrimestre_promedio04,cuatrimestre_promedio05,cuatrimestre_promedio06,cuatrimestre_promedio07,cuatrimestre_promedio08,cuatrimestre_promedio09,cuatrimestre_promedio10):
    try:
        return db.update('trayectorias_academicas',id_trayectoria_academica=id_trayectoria_academica,
email=email,
primaria_institucion=primaria_institucion,
primaria_promedio=primaria_promedio,
secundaria_institucion=secundaria_institucion,
secundadria_promedio=secundadria_promedio,
bachillerato_institucion=bachillerato_institucion,
bachillerato_promedio=bachillerato_promedio,
tsu_institucion=tsu_institucion,
tsu_promedio=tsu_promedio,
cuatrimestre_promedio01=cuatrimestre_promedio01,
cuatrimestre_promedio02=cuatrimestre_promedio02,
cuatrimestre_promedio03=cuatrimestre_promedio03,
cuatrimestre_promedio04=cuatrimestre_promedio04,
cuatrimestre_promedio05=cuatrimestre_promedio05,
cuatrimestre_promedio06=cuatrimestre_promedio06,
cuatrimestre_promedio07=cuatrimestre_promedio07,
cuatrimestre_promedio08=cuatrimestre_promedio08,
cuatrimestre_promedio09=cuatrimestre_promedio09,
cuatrimestre_promedio10=cuatrimestre_promedio10,
                  where='id_trayectoria_academica=$id_trayectoria_academica',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
