import web
import hmac
import application.models.model_programas_educativos

render = web.template.render('application/views/programas_educativos/', base='master')
model = application.models.model_programas_educativos

secret_key = "kuorra_key"


def hash_str(s):
    return hmac.new(secret_key, s).hexdigest()


def make_secure_val(s):
    return "%s!%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split('!')[0]
    if h == make_secure_val(val):
        return val
