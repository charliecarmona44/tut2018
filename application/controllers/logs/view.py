from . import config
import app


class View:
    
    def __init__(self):
        pass

    def GET(self, user):
        if app.session.loggedin is True:
            # username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.GET_VIEW(user)
            elif privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    @staticmethod
    def GET_VIEW(user):
        user = config.check_secure_val(str(user))
        result = config.model_users.get_users(user)
        print result
        return config.render.view(result)
