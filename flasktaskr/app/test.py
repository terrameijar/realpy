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

#######################################
######### Helper Functions ############
#######################################


    def login(self, name, password):
        return self.app.post('/', data=dict(name=name, password=password), follow_redirects=True)

    def register(self, name, email, password, confirm):
        return self.app.post('register/', data=dict(name=name,email=email, password=password, confirm=confirm), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout/', follow_redirects=True)

    def create_user(self, name, email,password):
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

    def create_task(self):
        return self.app.post('add/', data=dict(name='Go to the bank', 
                                               due_date='02/05/2014',
                                               priority='1',
                                               posted_date='02/04/2014',
                                               status='1'), follow_redirects=True)        

#######################################
############## Tests ##################
#######################################        

    # each test should start with
    def test_user_setup(self):
        new_user = User("vndlovu", "vndlovu@gmail.com", "vuyisilendlovu")
        db.session.add(new_user)
        db.session.commit()
        test = db.session.query(User).all()
        for t in test:
            t.name 
        assert t.name == "vndlovu"

    def test_form_is_present_on_login_page(self):
        response = self.app.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertIn('Please sign in to access your task list', response.data)


    def test_users_cannot_login_unless_registered(self):
        response = self.login('foo', 'bar')
        self.assertIn('Invalid username or password.', response.data)

    def test_users_can_login(self):
        self.register('Vuyisile', 'vuyisile@zimclix.co.zw', 'python', 'python')
        response = self.login('Vuyisile', 'python')
        self.assertIn('You are logged in. Go Crazy.', response.data)

    def test_invalid_form_data(self):
        self.register('Vuyisile', 'vuyisile@zimclix.co.zw', 'python', 'python')
        response = self.login('alert("alert box!");', 'foo')
        self.assertIn('Invalid username or password.',response.data)

    def test_form_is_present_on_register_page(self):
        response = self.app.get('register/')
        self.assertEquals(response.status_code, 200)
        self.assertIn('Please register to start a task list', response.data)

    def test_user_registration(self):
        self.app.get('register/', follow_redirects=True)
        response = self.register('Michael', 'michael@realpython.com', 'python', 'python')
        assert 'Thanks for registering. Please login.' in response.data

    def test_logged_in_users_can_logout(self):
        self.register('Fletcher', 'fletcher@realpython.com', 'python101', 'python101')
        self.login('Fletcher', 'python101')        
        response = self.logout()
        self.assertIn('You are logged out. Goodbye. :( ', response.data)

    def test_not_logged_in_users_cannot_logout(self):
        response = self.logout()
        self.assertNotIn('You are logged out. Goodbye. :( ', response.data)

    def test_logged_in_users_can_access_tasks_page(self):
        self.register('Duduzani', 'd@realpython.com', 'python101','python101')
        self.login('Duduzani', 'python101')
        response = self.app.get('tasks/')
        self.assertEquals(response.status_code,200)
        self.assertIn('Add a new task',  response.data)

    def test_not_logged_in_users_cannot_access_tasks_page(self):
        response = self.app.get('tasks/', follow_redirects=True)
        self.assertIn('You need to login first',response.data)

    def test_users_can_add_tasks(self):
        self.create_user('Vuyisile', 'vuyisile@zimclix.co.zw', 'python')
        self.login('Vuyisile', 'python')
        self.app.get('tasks/', follow_redirects=True)
        response = self.create_task()
        self.assertIn(
            'New entry was successfully posted. Thanks', response.data
        )

    def test_users_cannot_add_tasks_when_error(self):
        self.create_user('Vuyisile', 'vuyisile@zimclix.co.zw', 'python')
        self.login('Vuyisile', 'python')
        self.app.get('tasks/', follow_redirects=True)
        response = self.app.post('add/', data=dict(
            name='Go to the bank',
            due_date='',
            priority='1',
            posted_date='02/05/2015',
            status='1'),follow_redirects=True)
        self.assertIn('This field is required.', response.data)



if __name__ == '__main__':
    unittest.main()        

