from re import L
from app import mysql
from app.models.utils import encrypt_password, verify_encrypted_password

def add_trek(title, days, difficulty, total_cost, user_id):
    cur = mysql.connection.cursor()
    cur.execute('insert into trek_destinations (title, days, difficulty, total_cost, user_id ) values (%s, %s, %s, %s, %s)',(title, days, difficulty,total_cost, user_id));
    mysql.connection.commit()
    cur.close()
    return True

def get_all_treks():
    cur = mysql.connection.cursor()
    cur.execute('select * from trek_destinations')
    treks = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return treks or False

def get_single_trek(id):
    cur = mysql.connection.cursor()
    cur.execute('select * from trek_destinations where id = %s', (id,))
    trek = cur.fetchone()
    mysql.connection.commit()
    cur.close()
    return trek or False

def delete_single_trek(id):
    deleted = 0
    cur = mysql.connection.cursor()
    cur.execute('delete from trek_destinations where id = %s',(id,))
    mysql.connection.commit()
    deleted = cur.rowcount
    cur.close()
    return True if(deleted > 0) else False

def update_single_trek(id, title, days, difficulty, total_cost, user_id):
    updated = 0;
    cur = mysql.connection.cursor()
    cur.execute('update trek_destinations set title = %s, days = %s, difficulty = %s, total_cost = %s, user_id = %s where id = %s', (title, days, difficulty, total_cost, user_id, id))
    mysql.connection.commit()
    updated = cur.rowcount
    cur.close()
    return True if(updated > 0) else False
   
