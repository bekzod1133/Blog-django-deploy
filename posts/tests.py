from django.test import TestCase
from .models import PostModel
from django.contrib.auth.models import User


# Create your tests here.


class PostsTest(TestCase):
    def setUp(self) -> None:
        User.objects.create_user('User_test', password='osonpalov')
        author = User.objects.get(username='User_test')
        PostModel.objects.create(title='TestTitle', body='first body', author=author)
        PostModel.objects.create(title='TestTitle2', author=author)

    def test_post_functions(self):
        obj1 = PostModel.objects.get(title='TestTitle')
        obj2 = PostModel.objects.get(title='TestTitle2')
        self.assertEqual(str(obj1), 'TestTitle')
        self.assertEqual(str(obj2), 'TestTitle2')
        request = self.client.get('/')
        self.assertTemplateUsed(request, 'posts/home.html')
