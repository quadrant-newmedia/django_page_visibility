from django.test import TestCase, override_settings


# Sample - you can override any settings you require for your tests
# @override_settings(ROOT_URLCONF='django_page_visibility.tests.urls')
class MyTestCase(TestCase):
    # minimal test case; TODO: actual tests
    def test_things_import(self):
        from django_page_visibility import (
            LinkPathDoesNotExist,
            PageVisibilityError,
            ViewDoesNotSupportVisibilityTest,
            is_visible,
            is_visible_to_user,
        )
