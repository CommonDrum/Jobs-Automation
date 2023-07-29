
from atributes import *

class User:
    def __init__(self, user_name: str, personal_info: dict):
        self.user_name = user_name
        self.personal_info = PersonalInfo(**personal_info)  # personal info like name, address, contact number, etc.
        self.skills = []
        self.jobs = []
        self.educations = []
        self.certificates = []

    def add_skill(self, skill: Skill):
        self.skills.append(skill)

    def add_job(self, job: Employment):
        self.jobs.append(job)

    def add_education(self, education: Education):
        self.educations.append(education)

    def add_certificate(self, certificate: Certificate):
        self.certificates.append(certificate)

    def to_dict(self):
        return {
            'user_name': self.user_name,
            'personal_info': self.personal_info.to_dict(),
            'skills': [skill.to_dict() for skill in self.skills],
            'jobs': [job.to_dict() for job in self.jobs],
            'educations': [edu.to_dict() for edu in self.educations],
            'certificates': [cert.to_dict() for cert in self.certificates]
        }

    @classmethod
    def from_dict(cls, data: dict):
        profile = cls(data['user_name'], data['personal_info'])

        for skill in data['skills']:
            profile.add_skill(Skill(**skill))

        for job in data['jobs']:
            profile.add_job(Employment(**job))

        for education in data['educations']:
            profile.add_education(Education(**education))

        for certificate in data['certificates']:
            profile.add_certificate(Certificate(**certificate))

        return profile

    def save_to_file(self):
        with open(f'{self.user_name}_user.json', 'w') as f:
            json.dump(self.to_dict(), f)

    @classmethod
    def load_from_file(cls, file_name):
        with open(file_name, 'r') as f:
            data = json.load(f)
        return cls.from_dict(data)
