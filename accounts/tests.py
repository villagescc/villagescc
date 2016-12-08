from django.test import TestCase, Client


# Create your tests here.
class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_login(self):
        # Login GET
        response = self.client.get('/accounts/login')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_post_login(self):
        # Login POST
        response = self.client.post('/accounts/login', {'username': 'john', 'password': 'smith'})

        # Check that response is 200 OK.
        self.assertEqual(response.status_code, 200)


    def test_get_signup(self):
        # Login Get
        response = self.client.get('/accounts/signup')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


    def test_post_signup(self):
        # Login Post
        response = self.client.post('/accounts/signup')

        self.assertEqual(response.status_code, 200)
