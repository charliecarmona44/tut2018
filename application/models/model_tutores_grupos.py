import web
import config

db = config.db


def get_all_tutores_grupos():
    try:
        return db.select('tutores_grupos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_tutores_grupos(id_tutor_grupo):
    try:
        return db.select('tutores_grupos', where='id_tutor_grupo=$id_tutor_grupo', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_tutores_grupos(id_tutor_grupo):
    try:
        return db.delete('tutores_grupos', where='id_tutor_grupo=$id_tutor_grupo', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_tutores_grupos(user,id_grupo):
    try:
        return db.insert('tutores_grupos',user=user,
id_grupo=id_grupo)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_tutores_grupos(id_tutor_grupo,user,id_grupo):
    try:
        return db.update('tutores_grupos',id_tutor_grupo=id_tutor_grupo,
user=user,
id_grupo=id_grupo,
                  where='id_tutor_grupo=$id_tutor_grupo',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
