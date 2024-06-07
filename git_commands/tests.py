from django.test import TestCase
from .views import git_commands_to_group_dict as git_redirect_dict

# Create your tests here.

class TestGit(TestCase):

    def test_index(self):
        resp = self.client.get('/git/')
        self.assertEqual(resp.status_code, 200)

    def test_publish(self):
        resp = self.client.get('/git/publish')
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Команды для публикации изменений:", resp.content.decode())

    def test_redirects(self):
        for command, req in git_redirect_dict.items():
            resp = self.client.get(f'/git/{command}')
            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.url, f'/git/{req}')
