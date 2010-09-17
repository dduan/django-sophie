from django.test import TestCase

from sophie.utils import route_template, LaidbackPaginator

class UtilRouteTemplateTest(TestCase):

    def setUp(self):
        self.base = 'testbase'
        self.extra = 'xxx_yyy'
        self.blog = 'test_slug'
    def test_routing_with_full_args(self):
        expected_result = [
            r'sophie/test_slug/testbase_xxx_yyy.html',
            r'sophie/test_slug/testbase.html',
            r'sophie/default/testbase_xxx_yyy.html',
            r'sophie/default/testbase.html'
        ]

        tested_result = route_template(self.base, self.extra, self.blog)
        self.assertEqual(tested_result, expected_result)

    def test_routing_fails_without_args_basename(self):
        # With 0 args, should raise a TypeError
        self.assertRaises(TypeError, route_template, ())
        # basename is a must have!
        self.assertRaises(
            TypeError, 
            route_template, 
            (), 
            { 'basename': self.base, 'blog_slug': self.blog }
        )
        self.assertRaises(
            TypeError, 
            route_template, 
            (), 
            { 'blog_slug':self.blog }
        )
        self.assertRaises(
            TypeError, 
            route_template, 
            (), 
            { 'basename': self.base, }
        )

    def test_routing_with_only_basename(self):
        expected_result = [
            r'sophie/default/testbase_.html',
            r'sophie/default/testbase.html',
            r'sophie/default/testbase_.html',
            r'sophie/default/testbase.html'
        ]

        tested_result = route_template(self.base)
        self.assertEqual(tested_result, expected_result)

    def test_routing_without_extraname_args(self):
        expected_result = [
            r'sophie/test_slug/testbase_.html',
            r'sophie/test_slug/testbase.html',
            r'sophie/default/testbase_.html',
            r'sophie/default/testbase.html'
        ]

        tested_result = route_template(self.base, blog_slug=self.blog)
        self.assertEqual(tested_result, expected_result)

class UtilLaidbackPaginatorPageMethodTest(TestCase):
    def setUp(self):
        self.dummy_data = range(0,20)
        self.PAGE_BY = 5
        self.pages = LaidbackPaginator(self.dummy_data, self.PAGE_BY)

    def test_should_return_normally(self):
        p = self.pages.page('2').object_list
        self.assertEquals(p, [5, 6, 7, 8, 9])

    def test_should_tolerate_nonsense_arg(self):
        p = self.pages.page(None).object_list
        self.assertEquals(p, [0, 1, 2, 3, 4])
    
    def test_should_accept_over_ranged_arg(self):
        p = self.pages.page(10).object_list
        self.assertEquals(p, [15, 16, 17, 18, 19])

    def test_should_accept_under_ranged_arg(self):
        p = self.pages.page(0).object_list
        self.assertEquals(p, [15, 16, 17, 18, 19])

