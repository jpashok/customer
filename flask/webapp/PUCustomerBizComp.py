__author__ = 'JP'
import logger
from config import Config

from PUCustMySQLDBOps import PUCustMySQLDBOps

mysqldbops = PUCustMySQLDBOps()
class PUCustomerBizComp:

    def verifyUserName(self,username):
        rowcount = mysqldbops.verify_user_name(username)
        if rowcount >= 1 :
            return 1

    def verifyUserPwd(self,username,password):
        rowcount = mysqldbops.verify_user_pwd(username,password)
        if rowcount >=1 :
            return 1

    def signup(self,user_det):
        retval = mysqldbops.insert_user_det(user_det)
        if retval != 1:
            raise Exception("Signup failed")
