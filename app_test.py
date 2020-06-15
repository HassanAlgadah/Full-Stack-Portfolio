import unittest
from app import app
from models import setup_db, Project
from flask_sqlalchemy import SQLAlchemy


class PortfolioTestCase(unittest.TestCase):
    def setUp(self):
        self.admin_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRHNEhFN2ZOaUo3aUNMbDQ3ZWdpayJ9.eyJpc3MiOiJodHRwczovL2Rldi0tZzhjczhrNS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlNWRiMmZjNzBlYjAwMDE5MzE5YjA5IiwiYXVkIjoiUG9ydGZvbGlvIEFQSSIsImlhdCI6MTU5MjE4NDc1NiwiZXhwIjoxNTkyMjcxMTU2LCJhenAiOiI0MkR2UVJPTTdpVVlHbFYxT3MwTmNmN0IwRkRIYVJ5byIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnByb2plY3QiLCJnZXQ6bWVzc2FnZXMgIiwicGF0Y2g6cHJvamVjdCIsInBvc3Q6cHJvamVjdCJdfQ.Ggg3ESY4etJ36yXXFa00eMmegJlxXi_usKD-RggS7jGd8IIJ0wcF65LlWNIusO2uhJ3YjWd1rzczUKlCmFmZbkichwKJBle7gMobQFocpp59UOwBKcKOgWeCsMxdyZF_en1vQKAkr4mpa6q7P4knYV5Ji4XSSpfkxbehVDqNkLD8kZvDQ1EZx9Ry8HtYJNuhqOoAKJ6dNeTlY7ZXjTDX_ugEJKm3r3vdN5dCf1_Tn32OwjU5Wy2841DGrQkaiEE9D0wZbYp9BGW4fKKDE-B88dks1aGHTNNpzUEZ8qvrC0b_Dtcxrlkd8HwsOUZ4q_S0tuyW1blCOuDhh-ixyv3H7A'
        self.headers = {'Authorization': 'Bearer ' + self.admin_token}
        self.app = app
        self.client = self.app.test_client
        setup_db(self.app)

        self.new_good_project = {
            'name': 'p1',
            'description': 'description',
            'image': 'image',
            'link': 'www.example.come'
        }
        self.new_bad_project = {
            'questionww': 'what the meaning of the universe',

        }
        self.new_good_message = {
            'name': 'name',
            'email': 'email',
            'number': 'number',
            'message': 'message'
        }
        self.new_bad_message = {
            'questionww': 'what the meaning of the universe',

        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

    def tearDown(self):
        pass

    # testing all the endpoints for one success and one fail each
    # creating a new project successfully
    def test_create_new_project_success(self):
        res = self.client().post('/projects', json=self.new_good_project, headers=self.headers)
        self.assertEqual(res.status_code, 200)

    # creating a new project failing
    def test_create_new_project_fail(self):
        res = self.client().post('/projects', json=self.new_bad_project, headers=self.headers)
        self.assertEqual(res.status_code, 422)

    # update a project successfully
    def test_update_project_success(self):
        id = str(Project.query.all()[0].id)
        res = self.client().patch('/projects/' + id, json=self.new_good_project, headers=self.headers)
        self.assertEqual(res.status_code, 200)

    # update a project failing
    def test_update_project_fail(self):
        res = self.client().patch('/projects/-1', json=self.new_bad_project, headers=self.headers)
        self.assertEqual(res.status_code, 400)

    # delete a project successfully
    def test_delete_project_success(self):
        id = str(Project.query.all()[0].id)
        res = self.client().delete('/projects/' + id, headers=self.headers)
        self.assertEqual(res.status_code, 200)

    # delete a project failing
    def test_delete_project_fail(self):
        res = self.client().delete('/projects/-1', headers=self.headers)
        self.assertEqual(res.status_code, 404)

    # creating a new message successfully
    def test_create_new_message_success(self):
        res = self.client().post('/messages', json=self.new_good_message)
        self.assertEqual(res.status_code, 302)

    # creating a new message failing
    def test_create_new_message_fail(self):
        res = self.client().post('/messages', json=self.new_bad_message)
        self.assertEqual(res.status_code, 400)

    # testing for the access control role of admin
    # creating a new project failing as not admin
    def test_create_new_project_fail_not_authorized(self):
        self.headers = {'Authorization': 'Bearer ' + 'im not admin'}
        res = self.client().post('/projects', json=self.new_good_project, headers=self.headers)
        self.assertEqual(res.status_code, 401)


if __name__ == '__main__':
    unittest.main()
