# Import your LinkedInJobSearchURL class
from LinkedInURL import LinkedInJobSearchURL  # Adjust this import path as necessary

# Instantiate the class
job_search = LinkedInJobSearchURL()

# Set experience level (e.g., Entry level and Associate)
print("\nSetting experience level:")
job_search.set_experience_level()  # Follow the prompts, e.g., enter "2,3"

# Set work type (e.g., Hybrid and Remote)
print("\nSetting work type:")
job_search.set_work_type()  # Follow the prompts, e.g., enter "2,3"

# Set time posted (e.g., Past week)
print("\nSetting time posted:")
job_search.set_time_posted()  # Follow the prompts, e.g., enter "2"

# Set salary range (e.g., $100,000+)
print("\nSetting salary range:")
job_search.set_salary_range()  # Follow the prompts, e.g., enter "24"

# Set job type (e.g., Full-time and Contract)
print("\nSetting job type:")
job_search.set_job_type()  # Follow the prompts, e.g., enter "F,C"

# Set geographic location (geoId)
print("\nSetting geographic location:")
job_search.set_geoId()  # Follow the prompts, e.g., enter "3" for Toronto

# Set keywords (e.g., "computer science, data analysis")
print("\nSetting keywords:")
job_search.set_keywords()  # Follow the prompts, e.g., enter "computer science, data analysis"

# Generate the final URL
print("\nGenerating the LinkedIn job search URL...")
final_url = job_search.generate_url()

# Print the generated URL
print("\nThe final LinkedIn job search URL is:")
print(final_url)
