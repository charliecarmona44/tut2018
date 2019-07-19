import web
import application.models.model_users
import application.models.model_logs
import application.models.model_alumnos
import application.models.model_grupos


render = web.template.render('application/views/main/', base='master')
model_users = application.models.model_users
model_logs = application.models.model_logs
model_alumnos = application.models.model_alumnos
model_grupos = application.models.model_grupos


secret_key = "kuorra_key"

def validate_https():
    if app.web.ctx.protocol == "http":
            dom = app.web.ctx.homedomain
            dom = dom.replace("http","https")
            dom += app.web.ctx.path
            raise app.web.seeother(dom)

def hash_str(s):
    return hmac.new(secret_key, s).hexdigest()


def make_secure_val(s):
    return "%s!%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split('!')[0]
    if h == make_secure_val(val):
        return val