# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pymysql
import config as cfg


def getDBConnection():
    conn = pymysql.connect(host=cfg.mysql_url ,user=cfg.mysql_user , password=cfg.mysql_pwd , db=cfg.mysql_db_name,connect_timeout=5)
    return conn

def addUserInfo():
    sqlParams = []
    try:
        conn = getDBConnection()
        cursor = conn.cursor()

        sql_insert_statement = "insert into localtestdb.user_info(email, first_name , last_name , phone_number, user_name) values(%s,%s,%s,%s,%s)"
        sqlParams.append("test1@gmail.com")
        sqlParams.append("Lakshmi_1")
        sqlParams.append("K")
        sqlParams.append("9999999999")
        sqlParams.append("Lakshmi_9876")

        cursor.execute(sql_insert_statement , sqlParams)

        conn.commit()



    except Exception as e:
        print(e)
    finally:
        conn.close()

def updateUserInfo():
    sqlParams = []
    try:
        conn = getDBConnection()
        cursor = conn.cursor()

        sql_statement = "update localtestdb.user_info set first_name = %s where user_id = %s"
        sqlParams.append("Lucky")
        sqlParams.append(1)

        cursor.execute(sql_statement, sqlParams)

        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def deleteUserInfo():
    sqlParams = []
    try:
        conn = getDBConnection()
        cursor = conn.cursor()

        sql_statement = "delete from localtestdb.user_info where user_id = %s"
        sqlParams.append(1)

        cursor.execute(sql_statement , sqlParams)

        conn.commit()

    except Exception as e:
        print(e)
    finally:
        conn.close()

def getUserData():
    usersList = []
    try:
        conn = getDBConnection()
        cursor = conn.cursor()

        sql_statement = "select * from localtestdb.user_info"
        cursor.execute(sql_statement)
        columns = cursor.description

        for value in cursor.fetchall():
            tmp = {}

            for (index, column) in enumerate(value):
                tmp[columns[index][0]] = column


            usersList.append(tmp)

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

    print(usersList)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # addUserInfo()
    # updateUserInfo()
    # deleteUserInfo()
    getUserData()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
