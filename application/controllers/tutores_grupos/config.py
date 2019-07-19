import web
import hmac
import application.models.model_tutores_grupos
import application.models.model_grupos
import application.models.model_users
import application.models.model_grupos_tutores_users

render = web.template.render('application/views/tutores_grupos/', base='master')
model = application.models.model_tutores_grupos
model_tutores_grupos = application.models.model_tutores_grupos
model_grupos = application.models.model_grupos
model_users = application.models.model_users
model_grupos_tutores_users = application.models.model_grupos_tutores_users

secret_key = "kuorra_key"


def hash_str(s):
    return hmac.new(secret_key, s).hexdigest()


def make_secure_val(s):
    return "%s!%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split('!')[0]
    if h == make_secure_val(val):
        return val
