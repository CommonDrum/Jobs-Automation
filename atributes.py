import json

class BasicInfo:
    def __init__(self, name: str, description: str, info_type: str):
        self.name = name
        self.description = description
        self.info_type = info_type

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'info_type': self.info_type
        }


class Employment(BasicInfo):
    def __init__(self, name: str, description: str, start_date: str, end_date: str, job_title: str):
        super().__init__(name, description, "job")
        self.start_date = start_date
        self.end_date = end_date
        self.job_title = job_title

    def to_dict(self):
        parent_dict = super().to_dict()
        parent_dict.update({
            'start_date': self.start_date,
            'end_date': self.end_date,
            'job_title': self.job_title
        })
        return parent_dict


class Education(BasicInfo):
    def __init__(self, name: str, description: str, start_date: str, end_date: str, degree: str, field_of_study: str):
        super().__init__(name, description, "education")
        self.start_date = start_date
        self.end_date = end_date
        self.degree = degree
        self.field_of_study = field_of_study

    def to_dict(self):
        parent_dict = super().to_dict()
        parent_dict.update({
            'start_date': self.start_date,
            'end_date': self.end_date,
            'degree': self.degree,
            'field_of_study': self.field_of_study
        })
        return parent_dict


class Skill(BasicInfo):
    def __init__(self, name: str, description: str):
        super().__init__(name, description, "skill")


class Certificate(BasicInfo):
    def __init__(self, name: str, description: str, issue_date: str, expiration_date: str, credential_id: str, credential_url: str):
        super().__init__(name, description, "certificate")
        self.issue_date = issue_date
        self.expiration_date = expiration_date
        self.credential_id = credential_id
        self.credential_url = credential_url

    def to_dict(self):
        parent_dict = super().to_dict()
        parent_dict.update({
            'issue_date': self.issue_date,
            'expiration_date': self.expiration_date,
            'credential_id': self.credential_id,
            'credential_url': self.credential_url
        })
        return parent_dict


class PersonalInfo():
    def __init__(self, first_names: str, last_name: str, birthday: str, phone: int, email: str, city: str, postcode: str, linkedin: str, website: str):
        self.first_names = first_names
        self.last_name = last_name
        self.birthday = birthday
        self.phone = phone
        self.email = email
        self.city = city
        self.postcode = postcode
        self.linkedin = linkedin
        self.website = website

    def to_dict(self):
        dict = { 
                'first_names' : self.first_names,
                'last_name' : self.last_name,
                'birthday' : self.birthday,
                'phone' : self.phone,
                'email'  :   self.email,
                'city' : self.city,
                'postcode' : self.postcode,
                'linkedin' : self.linkedin,
                'website' : self.website 
                }
        return dict
        
        
