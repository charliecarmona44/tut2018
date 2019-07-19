import web
import config

db = config.db


def get_all_observaciones_individuales():
    try:
        return db.select('observaciones_individuales')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_observaciones_individuales(id_observacion_individual):
    try:
        return db.select('observaciones_individuales', where='id_observacion_individual=$id_observacion_individual', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_observaciones_individuales(id_observacion_individual):
    try:
        return db.delete('observaciones_individuales', where='id_observacion_individual=$id_observacion_individual', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_observaciones_individuales(email,user,fecha_observaciones,observaciones,fecha_atencion,acciones,resultados,semaforo):
    try:
        return db.insert('observaciones_individuales',email=email,
user=user,
fecha_observaciones=fecha_observaciones,
observaciones=observaciones,
fecha_atencion=fecha_atencion,
acciones=acciones,
resultados=resultados,
semaforo=semaforo)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_observaciones_individuales(id_observacion_individual,email,user,fecha_observaciones,observaciones,fecha_atencion,acciones,resultados,semaforo):
    try:
        return db.update('observaciones_individuales',id_observacion_individual=id_observacion_individual,
email=email,
user=user,
fecha_observaciones=fecha_observaciones,
observaciones=observaciones,
fecha_atencion=fecha_atencion,
acciones=acciones,
resultados=resultados,
semaforo=semaforo,
                  where='id_observacion_individual=$id_observacion_individual',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
