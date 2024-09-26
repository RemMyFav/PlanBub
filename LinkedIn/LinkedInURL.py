class LinkedInJobSearchURL:
    def __init__(self):
        self.base_url = "https://www.linkedin.com/jobs/search"
        # A dictionary to hold all the URL parameters
        self.params = {
            "f_E": "",    # Experience levels
            "f_WT": "",   # Work types
            "f_TPR": "",  # Time posted
            "f_SB2": "",  # Salary range
            "f_JT": "",   # Job types
            "geoId": "",  # Geographic location
            "keywords": "",  # Keywords for search
            "f_PP": "",  # Specific job location
            "f_CF": "",  # Company filter
            "f_TP": ""   # Top companies or preferred companies filter
        }
        self.final_url = ""
    
    def get_user_input(self, prompt):
        """General method to get user input."""
        return input(prompt).strip()

    def set_parameter(self, param_name, param_value):
        """General method to set a URL parameter."""
        if param_name in self.params:
            self.params[param_name] = param_value
            print(f"Parameter '{param_name}' has been set to: {param_value}")
        else:
            print(f"Invalid parameter name: {param_name}")

    def set_experience_level(self):
        experience_levels = {
            "1": "Internship",
            "2": "Entry level",
            "3": "Associate",
            "4": "Mid-Senior level",
            "5": "Director",
            "6": "Executive"
        }
        print("Select experience levels (e.g., '1,2'), or press Enter to skip: ")
        for key, value in experience_levels.items():
            print(f"{key}: {value}")
        selection = self.get_user_input("Enter your choice(s): ")
        if selection:  # Only set if there is a valid selection
            selected = [s.strip() for s in selection.split(',') if s.strip() in experience_levels]
            self.set_parameter("f_E", "%2C".join(selected))
        else:
            self.set_parameter("f_E", "")

    def set_work_type(self):
        work_types = {
            "1": "On-site",
            "2": "Remote",
            "3": "Hybrid"
        }
        print("Select work types (e.g., '1,2'), or press Enter to skip: ")
        for key, value in work_types.items():
            print(f"{key}: {value}")
        selection = self.get_user_input("Enter your choice(s): ")
        if selection:
            selected = [s.strip() for s in selection.split(',') if s.strip() in work_types]
            self.set_parameter("f_WT", "%2C".join(selected))
        else:
            self.set_parameter("f_WT", "")

    def set_time_posted(self):
        time_ranges = {
            "1": "Past 24 hours",
            "2": "Past week",
            "3": "Past month"
        }
        print("Select time posted (1: 24 hours, 2: past week, 3: past month), or press Enter to skip: ")
        for key, value in time_ranges.items():
            print(f"{key}: {value}")
        selection = self.get_user_input("Enter your choice: ")
        mapping = {"1": "r86400", "2": "r604800", "3": "r2592000"}
        self.set_parameter("f_TPR", mapping.get(selection, ""))

    def set_salary_range(self):
        salary_ranges = {
            "21": "$40,000+",
            "22": "$60,000+",
            "23": "$80,000+",
            "24": "$100,000+",
            "25": "$120,000+",
            "26": "$140,000+",
            "27": "$160,000+",
            "28": "$180,000+",
            "29": "$200,000+"
        }
        print("Select salary range (e.g., '24' for $100,000+), or press Enter to skip: ")
        for key, value in salary_ranges.items():
            print(f"{key}: {value}")
        selection = self.get_user_input("Enter your choice: ")
        if selection and selection in salary_ranges:
            self.set_parameter("f_SB2", selection)
        else:
            self.set_parameter("f_SB2", "")

    def set_job_type(self):
        job_types = {
            "F": "Full-time",
            "P": "Part-time",
            "C": "Contract",
            "T": "Temporary",
            "V": "Volunteer",
            "I": "Internship",
            "O": "Other"
        }
        print("Select job types (e.g., 'F,P,C'), or press Enter to skip: ")
        for key, value in job_types.items():
            print(f"{key}: {value}")
        selection = self.get_user_input("Enter your choice(s): ").upper()
        if selection:
            selected = [s.strip() for s in selection.split(',') if s.strip() in job_types]
            self.set_parameter("f_JT", "%2C".join(selected))
        else:
            self.set_parameter("f_JT", "")

    def set_geoId(self):
        known_geo_ids = {
            "1": ("101174742", "Canada"),
            "2": ("105149290", "Ontario, Canada"),
            "3": ("100025096", "Toronto, Ontario, Canada"),
            "4": ("101788145", "Mississauga, Ontario, Canada")
        }
        
        print("Please select a geoId from the list or enter your own value, or press Enter to skip:")
        for key, (geoId, location) in known_geo_ids.items():
            print(f"{key}: {geoId} ({location})")
        
        user_input = self.get_user_input("Enter your choice (number or custom geoId): ")
        
        if user_input in known_geo_ids:
            selected_geoId, location = known_geo_ids[user_input]
            self.set_parameter("geoId", selected_geoId)
            print(f"GeoID set to {selected_geoId} corresponding to location: {location}")
        else:
            self.set_parameter("geoId", user_input if user_input else "")
            if user_input:
                print(f"GeoID set to a new value: {user_input}, this is not in the known list")
    
    def set_keywords(self):
        user_input_keywords = self.get_user_input("Please enter search keywords using Boolean operators (AND, OR, NOT), or press Enter to skip: ")
        
        if user_input_keywords:
            # Replace spaces with %20 and commas with %2C
            encoded_keywords = user_input_keywords.replace(" ", "%20").replace(",", "%2C")
            self.set_parameter("keywords", encoded_keywords)
            print(f"Keywords have been set to: {encoded_keywords}")
        else:
            self.set_parameter("keywords", "")

    def generate_url(self):
        """Generates the final URL and saves it to self.final_url"""
        query_string = "&".join([f"{key}={value}" for key, value in self.params.items() if value])
        
        self.final_url = f"{self.base_url}?{query_string}" if query_string else self.base_url
        
        print(f"Generated URL: {self.final_url}")
        return self.final_url


    def reset_parameters(self):
        """Resets all parameters to their default values"""
        self.params = {key: "" for key in self.params}
        self.final_url = ""
        print("All parameters have been reset.")
    
    def get_parameter(self, param_name):
        """Retrieve the value of a specified parameter."""
        if param_name in self.params:
            param_value = self.params[param_name]
            if param_value:
                print(f"The value of parameter '{param_name}' is: {param_value}")
                return param_value
            else:
                print(f"The parameter '{param_name}' is currently not set.")
                return None
        else:
            print(f"Invalid parameter name: '{param_name}'.")
            return None
    
    def get_all_params(self):
        """Retrieve and display all parameters with their current values."""
        print("Current LinkedIn Job Search Parameters:")
        for param_name, param_value in self.params.items():
            if param_value:  # Only show parameters that have been set
                print(f"{param_name}: {param_value}")
            else:
                print(f"{param_name}: Not set")
