import config
import app


class Edit:
    def __init__(self):
        pass

    def GET(self, id_tutor_grupo, message=None):
        if app.session.loggedin is True:
            user = app.session.user
            privilege = app.session.privilege
            if privilege == 0:
                return self.GET_EDIT(id_tutor_grupo, message)
            else:
                raise config.web.seeother('/')
        else:
            raise config.web.seeother('/login')

    def POST(self, id_tutor_grupo, message=None):
        if app.session.loggedin is True:
            user = app.session.user
            privilege = app.session.privilege
            if privilege == 0:
                return self.POST_EDIT(id_tutor_grupo, message)
            else:
                raise config.web.seeother('/')
        else:
            raise config.web.seeother('/login')
    
    @staticmethod
    def GET_EDIT(id_tutor_grupo, message=None):
        id_tutor_grupo = config.check_secure_val(str(id_tutor_grupo))
        result = config.model_tutores_grupos.get_tutores_grupos(int(id_tutor_grupo))
        result.id_tutor_grupo = config.make_secure_val(str(result.id_tutor_grupo))
        tutores = config.model_users.get_all_users().list()
        grupos = config.model_grupos.get_all_grupos().list()
        return config.render.edit(tutores, grupos, result, message)

    @staticmethod
    def POST(id_tutor_grupo, message=None):
        form = config.web.input()
        form['id_tutor_grupo'] = config.check_secure_val(str(form['id_tutor_grupo']))
        res = config.model.edit_tutores_grupos(
            form['id_tutor_grupo'],
            form['user'],
            form['id_grupo'],
        )
        if res == 0:
            id_tutor_grupo = config.check_secure_val(str(id_tutor_grupo))
            result = config.model_tutores_grupos.get_tutores_grupos(int(id_tutor_grupo))
            result.id_tutor_grupo = config.make_secure_val(str(result.id_tutor_grupo))
            message = "Error al editar el registro"
            return config.render.edit(result, message)
        else:
            raise config.web.seeother('/tutores_grupos')