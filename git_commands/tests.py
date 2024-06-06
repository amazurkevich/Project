from django.test import TestCase

# Create your tests here.

class TestGit(TestCase):

    def test_index(self):
        resp = self.client.get('/git/')
        self.assertEqual(resp.status_code, 200)

    def test_publish(self):
        resp = self.client.get('/git/publish')
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Команды для публикации изменений:", resp.content.decode())

    def test_publish_redirect(self):
        resp = self.client.get('/git/push')
        self.assertEqual(resp.status_code, 302)
        # self.assertIn("Команды для публикации изменений:", resp.content.decode())

# test = TestGit
