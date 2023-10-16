import unittest
import app
# create a class that displays the test results carri out 



class AppTest(unittest.TestCase):
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()





    def test_get_crimes(self):
        rv = self.app.get('/crimes')
        self.assertEqual(rv.status, '200 OK')



    def test_post_crime(self):
        rv = self.app.post('/crimes', json={"name": "Test crime", "description": "This is a test crime"})
        self.assertEqual(rv.status, '201 CREATED')






    def test_get_suspects(self):
        rv = self.app.get('/suspects')
        self.assertEqual(rv.status, '200 OK')

    def test_post_suspect(self):
        rv = self.app.post('/suspects', json={"name": "Test suspect"})
        self.assertEqual(rv.status, '201 CREATED')

if __name__ == '__app__':
    unittest.app()
