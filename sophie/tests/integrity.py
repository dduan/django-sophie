from django.test import TestCase

class MultiBlogIntegrityTest(TestCase):

    fixtures = ['integrity']

    def test_home_page_behaves_well(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
    
    def test_blog_index_behaves_well(self):
        response = self.client.get('/blog-2/')
        self.assertEquals(response.status_code, 200)
    
    def test_entry_list_behaves_well(self):
        response = self.client.get('/blog-1/entries/1/')
        self.assertEquals(response.status_code, 200)
    
    def test_entry_details_behaves_well(self):
        response = self.client.get('/blog-1/entry/essay-1/')
        self.assertEquals(response.status_code, 200)
        
    def test_category_details_behaves_well(self):
        response = self.client.get('/blog-1/category/category-1/')
        self.assertEquals(response.status_code, 200)
    
    def test_original_feed_behaves_well(self):
        response = self.client.get('/blog-2/feed/')
        self.assertEquals(response.status_code, 200)

    def test_root_sitemap_behaves_well(self):
        response = self.client.get('/sitemap.xml')
        self.assertEquals(response.status_code, 200)

    def test_blog_sitemap_behaves_well(self):
        response = self.client.get('/blog-2/sitemap.xml')
        self.assertEquals(response.status_code, 200)
