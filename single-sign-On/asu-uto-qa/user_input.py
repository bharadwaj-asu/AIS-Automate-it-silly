
#this is to get all the credentials of the user and user website
import getpass
#this makes your password not appear on the screen
from ASULogin import  ASULoginPythonScript
class User_input:
    def userprofile(self):
        self.username = raw_input("Enter your username")
        self.password=getpass.getpass(prompt="Enter you ASURITE Password")
        self.url=raw_input("Enter the Url")

    def connect_to_url(self):
        x=ASULoginPythonScript()
        cookies=x.test_a_s_u_login_python_script(self.username,self.password,self.url)
        print("done")
        return cookies







