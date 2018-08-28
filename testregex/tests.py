from django.test import TestCase


class RegexTestCase(TestCase):

    def test_assert_regex(self):
        self.assertRegex('regex', 'regex')
