import config
import hashlib
import app

class Insert:

    def __init__(self):
        pass


    
    def GET(self):
        tutores = config.model_users.get_all_users().list()
        grupos = config.model_grupos.get_all_grupos().list()
        return config.render.insert(tutores,grupos)


    def POST(self):
        form = config.web.input() # get form data

        # call model insert_tutores_grupos and try to insert new data
        config.model.insert_tutores_grupos(
            form['user'],
            form['id_grupo'],
        )
        raise config.web.seeother('/tutores_grupos') # render tutores_grupos index.html
