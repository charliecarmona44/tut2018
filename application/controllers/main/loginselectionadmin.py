import application.controllers.main.config as config
import datetime
import app


class LoginSelectionAdmin:
    
    def __init__(self):
        pass

    def GET(self, **k):
        message = None
        return config.render.loginselectionadmin(message)