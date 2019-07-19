import web
from . import config

db = config.db

def validate_alumno(clave_registro_alumnos):
    try:
        # select * from users where username=$username and password=$password;
        return db.select('clases',
            where='clave_registro_alumnos=$clave_registro_alumnos', vars=locals())[0]
    except Exception as e:
        print(("Model get all Error {}".format(e.args)))
        print(("Model get all Message {}".format(e.message)))
        return None
        