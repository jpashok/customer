import MySQLdb
import re
import logger
import traceback

from datetime import datetime

class PUCustMySQLDBOps(object):
    
    
    def __init__(self):
        self.currentDate = datetime.now().isoformat()
        self.conn = MySQLdb.connect(user='root', passwd='****', db='1000lookz', host='localhost', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
        
    def verify_user_name(self,username):
        try:
            query = ("SELECT username FROM user_det WHERE username=%s")
            self.cursor.execute(query,(username,))
            return self.cursor.rowcount
        except MySQLdb.Error, e:
            tb = traceback.format_exc()
            logger.customer_logger().error('Error : %s' %tb)
            return -1

    
    def verify_user_pwd(self,username, password):
        try:
            query = ("SELECT passwd FROM user_det WHERE passwd=%s and username=%s")
            self.cursor.execute(query,(password,username))
            return self.cursor.rowcount
        except MySQLdb.Error, e:
            tb = traceback.format_exc()
            logger.customer_logger().error('Error : %s' %tb)
            return -1

    def insert_basic_user_det(self,username,password):
        try:
            self.cursor.execute("""INSERT INTO user_det VALUES (%s, %s)""", (username,password))
            self.conn.commit()
            return 1
        except MySQLdb.Error, e:
            tb = traceback.format_exc()
            logger.customer_logger().error('Error : %s' %tb)
            return -1

    def insert_user_det(self,user_det):
        try:
            self.cursor.execute("""INSERT INTO user_det VALUES (%s,%s,%s,%s,%s)""", (user_det['username'],user_det['password'],user_det['firstname'],user_det['lastname'],user_det['email']))
            self.conn.commit()
            return 1
        except MySQLdb.Error, e:
            tb = traceback.format_exc()
            logger.customer_logger().error('Error : %s' %tb)
            return -1

