import web
import hmac
import application.models.model_tutoria_especial
import application.models.model_users
import application.models.model_alumnos
import application.models.model_grupos
import application.models.model_area_atencion
import application.models.model_programas_educativos

render = web.template.render('application/views/tutoria_especial/', base='master')
model = application.models.model_tutoria_especial
model_users = application.models.model_users
model_alumnos =application.models.model_alumnos
model_grupos = application.models.model_grupos
model_area_atencion = application.models.model_area_atencion
model_programas_educativos = application.models.model_programas_educativos

secret_key = "kuorra_key"


def hash_str(s):
    return hmac.new(secret_key, s).hexdigest()


def make_secure_val(s):
    return "%s!%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split('!')[0]
    if h == make_secure_val(val):
        return val
