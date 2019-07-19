import web
from . import config

db = config.db


def validate_user_google(user):
    try:
        # select * from users where username=$username and password=$password;
        return db.select('users',
            where='user=$user', vars=locals())[0]
    except Exception as e:
        print(("Model get all Error {}".format(e.args)))
        print(("Model get all Message {}".format(e.message)))
        return None


def validate_user(user,other_data):
    try:
        # select * from users where username=$username and password=$password;
        return db.select('users',
            where='user=$user and other_data=$other_data', vars=locals())[0]
    except Exception as e:
        print(("Model get all Error {}".format(e.args)))
        print(("Model get all Message {}".format(e.message)))
        return None



def get_all_users():
    try:
        # select * from users;
        return db.select('users') 
    except Exception as e:
        print(("Model get all Error {}".format(e.args)))
        print(("Model get all Message {}".format(e.message)))
        return None


def get_users(user):
    try:
        # select * from users where username = $username;
        return db.select('users', where='user=$user', vars=locals())[0] 
    except Exception as e:
        print(("Model get Error {}".format(e.args)))
        print(("Model get Message {}".format(e.message)))
        return None


def delete_users(user):
    try:
        # delete * from users where username = $username;
        return db.delete('users', where='user=$user', vars=locals())
    except Exception as e:
        print(("Model delete Error {}".format(e.args)))
        print(("Model delete Message {}".format(e.message)))
        return None


def insert_users(user, privilege, status, name, email, other_data, user_hash):
    try:
        """
        insert into users (user, privilege, status, name, email, other_data, user_hash, change_pwd) 
        values ($user, $privilege, $status, $name, $email, $other_data, $user_hash, $change_pwd);
        """
        db.insert('users',
            user=user,
            privilege=privilege,
            status=status,
            name=name,
            email=email,
            other_data=other_data,
            user_hash=user_hash
                    )
    except Exception as e:
        print(("Model insert Error {}".format(e.args)))
        print(("Model insert Message {}".format(e.message)))
        return None


def edit_users(user, privilege, status, name, email, other_data, user_hash):
    try:
        """
        update users set password=$password, privilege=$privilege, status=$status, name=$name,
            email=$email, other_data=$other_data, user_hash=$user_hash, change_pwd=$change_pwd 
            where username=$username;
        """
        return db.update('users',
            user=user,
            privilege=privilege,
            status=status,
            name=name,
            email=email,
            other_data=other_data,
            user_hash=user_hash,
            where='user=$user',
            vars=locals())
            
    except Exception as e:
        print("Model update Error {}".format(e.args))
        print("Model updateMessage {}".format(e.message))
        return None


