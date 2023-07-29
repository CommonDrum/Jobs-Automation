from user import *

# create user
info = PersonalInfo("John", "Doe", "2000-01-01", 1234567890, "john.doe@example.com", "Some City", "12345", "linkedin.com/in/johndoe", "johndoe.com")
user = User("johndoe", info.to_dict())

# add skills
user.add_skill(Skill("Python", 5))
user.add_skill(Skill("Java", 3))

# add education
user.add_education(Education("Some University", "Bachelor of Science", "Computer Science", "2020-01-01", "2024-01-01"))

# add job
user.add_job(Employment("Some Company", "Description", "2020-01-01", "2024-01-01", "Software Engineer"))

# Print the profile

print(user.to_dict())
