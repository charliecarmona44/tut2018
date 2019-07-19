import web
import hmac
import application.models.model_observaciones_individuales
import application.models.model_alumnos_observaciones
import application.models.model_alumnos
import application.models.model_alumnos_grupos
import application.models.model_users

render = web.template.render('application/views/observaciones_individuales/', base='master')
model = application.models.model_observaciones_individuales
model_alumnos_observaciones = application.models.model_alumnos_observaciones
model_alumnos = application.models.model_alumnos
model_alumnos_grupos = application.models.model_alumnos_grupos
model_users = application.models.model_users




secret_key = "kuorra_key"


def hash_str(s):
    return hmac.new(secret_key, s).hexdigest()


def make_secure_val(s):
    return "%s!%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split('!')[0]
    if h == make_secure_val(val):
        return val
