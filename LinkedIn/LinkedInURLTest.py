import unittest
from urllib.parse import parse_qs, urlparse
from LinkedInURL import LinkedInJobSearchURL

class TestLinkedInJobSearchURL(unittest.TestCase):

    def setUp(self):
        """Set up an instance of the LinkedInJobSearchURL class before each test"""
        self.job_search = LinkedInJobSearchURL()

    def test_set_experience_level(self):
        """Test setting the experience level parameter"""
        # Simulate user input for experience levels
        self.job_search.set_parameter("f_E", "1,3")
        self.assertEqual(self.job_search.get_parameter("f_E"), "1,3")

    def test_set_work_type(self):
        """Test setting the work type parameter"""
        # Simulate user input for work types
        self.job_search.set_parameter("f_WT", "1,3")
        self.assertEqual(self.job_search.get_parameter("f_WT"), "1,3")

    def test_set_time_posted(self):
        """Test setting the time posted parameter"""
        # Simulate user input for time posted
        self.job_search.set_parameter("f_TPR", "r86400")
        self.assertEqual(self.job_search.get_parameter("f_TPR"), "r86400")

    def test_generate_url(self):
        """Test URL generation with multiple parameters set"""
        # Set multiple parameters
        self.job_search.set_parameter("f_E", "1,2")
        self.job_search.set_parameter("f_WT", "2")
        self.job_search.set_parameter("keywords", "software%20engineer")
        
        # Generate the URL
        generated_url = self.job_search.generate_url()
        
        # Parse the generated URL
        parsed_url = urlparse(generated_url)
        query_params = parse_qs(parsed_url.query)

        # Assertions for checking correctness of generated URL
        self.assertEqual(query_params.get("f_E"), ["1,2"])
        self.assertEqual(query_params.get("f_WT"), ["2"])
        self.assertEqual(query_params.get("keywords"), ["software%20engineer"])

    def test_reset_parameters(self):
        """Test resetting parameters"""
        # Set some parameters
        self.job_search.set_parameter("f_E", "1,2")
        self.job_search.set_parameter("f_WT", "2")
        
        # Check parameters before reset
        self.assertEqual(self.job_search.get_parameter("f_E"), "1,2")
        self.assertEqual(self.job_search.get_parameter("f_WT"), "2")

        # Reset parameters
        self.job_search.reset_parameters()
        
        # Check parameters after reset
        self.assertIsNone(self.job_search.get_parameter("f_E"))
        self.assertIsNone(self.job_search.get_parameter("f_WT"))

    def test_keywords_encoding(self):
        """Test encoding of keywords with special characters"""
        # Set keywords with special characters
        self.job_search.set_keywords()
        
        # Check that the keywords are properly encoded in the URL
        encoded_keywords = "Python%20AND%20Django%20OR%20Flask"
        self.assertEqual(self.job_search.params["keywords"], encoded_keywords)

if __name__ == "__main__":
    unittest.main()
