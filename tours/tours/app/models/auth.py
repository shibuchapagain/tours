from app import mysql

def add_user(firstName, lastName, email,  password):
    cur = mysql.connection.cursor()
    cur.execute("insert into users (first_name, last_name, email, password) values(%s, %s, %s, %s)",(firstName, lastName, email, password));
    mysql.connection.commit()
    cur.close()
    return True;


def get_single_user(email):
    cur = mysql.connection.cursor()
    cur.execute("select * from users where email = %s", (email,))
    user = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    if user:
        return user
    return False

def verify_password(email, password):
    cur = mysql.connection.cursor()
    cur.execute("select password from users where email = %s",(email,))
    db_pass = cur.fetchone()
    mysql.connection.commit()
    
    cur.close()
    if db_pass and str(db_pass[0]) == password:
        return True
    return False


