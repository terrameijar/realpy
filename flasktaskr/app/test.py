import os
import unittest

from views import app, db
from config import basedir
from models import User

TEST_DB = 'test.db'

class AllTests(unittest.TestCase):

    ##############################
    ##### Setup and Teardown #####
    ##############################

    #executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()

   
    # executed after each test
    def tearDown(self):
        db.drop_all()

    # each test should start with
    def test_user_setup(self):
        new_user = User("vndlovu", "vndlovu@gmail.com", "vuyisilendlovu")
        db.session.add(new_user)
        db.session.commit()

if __name__ == '__main__':
            unittest.main()        

