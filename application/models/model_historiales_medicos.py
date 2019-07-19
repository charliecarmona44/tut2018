import web
import config

db = config.db

def validar_historial_medico(email):
    try:
        return db.select('historiales_medicos', where='email=$email', vars=locals())[0]
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None

def get_all_historiales_medicos():
    try:
        return db.select('historiales_medicos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_historiales_medicos(id_historial_medico):
    try:
        return db.select('historiales_medicos', where='id_historial_medico=$id_historial_medico', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_historiales_medicos(id_historial_medico):
    try:
        return db.delete('historiales_medicos', where='id_historial_medico=$id_historial_medico', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_historiales_medicos(email,imss,no_imss,institucion_salud,nombre_institucion_salud,no_afiliacion_otra,tipo_sangre,alergias,descripcion_alergias,enfermedades,descripcion_enfermedad,medicamentos,descripcion_medicamentos):
    try:
        return db.insert('historiales_medicos',email=email,
imss=imss,
no_imss=no_imss,
institucion_salud=institucion_salud,
nombre_institucion_salud=nombre_institucion_salud,
no_afiliacion_otra=no_afiliacion_otra,
tipo_sangre=tipo_sangre,
alergias=alergias,
descripcion_alergias=descripcion_alergias,
enfermedades=enfermedades,
descripcion_enfermedad=descripcion_enfermedad,
medicamentos=medicamentos,
descripcion_medicamentos=descripcion_medicamentos)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_historiales_medicos(id_historial_medico,email,imss,no_imss,institucion_salud,nombre_institucion_salud,no_afiliacion_otra,tipo_sangre,alergias,descripcion_alergias,enfermedades,descripcion_enfermedad,medicamentos,descripcion_medicamentos):
    try:
        return db.update('historiales_medicos',id_historial_medico=id_historial_medico,
email=email,
imss=imss,
no_imss=no_imss,
institucion_salud=institucion_salud,
nombre_institucion_salud=nombre_institucion_salud,
no_afiliacion_otra=no_afiliacion_otra,
tipo_sangre=tipo_sangre,
alergias=alergias,
descripcion_alergias=descripcion_alergias,
enfermedades=enfermedades,
descripcion_enfermedad=descripcion_enfermedad,
medicamentos=medicamentos,
descripcion_medicamentos=descripcion_medicamentos,
                  where='id_historial_medico=$id_historial_medico',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
