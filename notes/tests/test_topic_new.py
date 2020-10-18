from django.contrib.auth.models import User
from django.urls import resolve, reverse
from django.test import TestCase
from notes.views import topic_new
from notes.models import Note, Topic

# Tests with user not logged in:
class TopicTestsNewTopic(TestCase):
    def setUp(self):
        self.url = reverse('url_topic_new')
        self.response = self.client.get(self.url)

    def test_topic_new_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_topic_new_url_resolves_correct_method(self):
        method_to_serve_url = resolve('/topics/new').func
        self.assertEquals(method_to_serve_url, topic_new)

    def test_topic_new_view_form_exists(self):
        self.assertContains(self.response,'<form ', 1)

    def test_topic_new_check_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')