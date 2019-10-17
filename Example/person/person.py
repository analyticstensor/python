import uuid
import string
import random
from datetime import datetime
import json


class Person:
    """Class Name:Person
    Description: Used to generate dummy personal structured data
    """

    batch_no = uuid.uuid4().bytes.hex()

    def __init__(self, country_code, **kwargs):
        self.__country_code = country_code
        self.__batch_no = Person.batch_no
        self.__person_id = self.person_id
        self.__full_name = self.full_name
        self.__phone_number = self.phone_number
        self.__created_date = self.created_date

    @property
    def country_code(self):
        return self.__country_code

    @property
    def person_id(self):
        return uuid.uuid4().hex

    @property
    def full_name(self):
        first_name = self.__format_string(self.__generate_random_string(string_length=7, is_formatted=False)).capitalize()
        middle_name = self.__generate_random_string(string_length=1, is_formatted=False).capitalize()
        last_name = self.__generate_random_string(string_length=5, is_formatted=False).capitalize()
        full_name = first_name + " " + middle_name + " " + last_name
        return full_name

    @property
    def phone_number(self):
        random_number = str(random.random())[-11:-1]
        formatted_phone = "(" + random_number[0:3] + ")" + random_number[3:6] + "-" + random_number[6:]
        return formatted_phone

    @property
    def created_date(self):
        return datetime.utcnow().isoformat()

    def __generate_random_string(self, string_length=10, is_formatted=False):
        """Generate a random string with defined length and formatted character"""
        alphabet_letter = string.ascii_lowercase
        random_string = ''.join(random.choice(alphabet_letter) for ctr in range(string_length))
        return random_string

    def __format_string(self, random_string, country_code=0):
        """Format String to human readable"""

        #todo
        # Track all the activity with logging

        # country code
        country_choice = {"all": 0, "us": 1, "euro": 2, "uk": 3}

        # Get styles from style_format by mapping with country_choice
        style_file = 'style/style_format.json'
        try:
            with open(style_file) as style_json:
                style_format = json.load(style_json)
        except FileNotFoundError:
            print("File not found: %s" % style_file)

        # Check country_choice exits on the exist else used default 'all'
        if country_code == 0:
            #todo
            # Sort dict and find the optimal way to get list elements with matchin with country code.

            ctr_id = style_format[0]['id']  # style_format.index(country_code)
            replace_words = style_format[0]['detail_info']['style']['common_letters']
            vowel = style_format[0]['detail_info']['style']['vowel']
            if vowel > 50:
                replace_string = "".join(random.choice(style_format[0]['detail_info']['style']['common_letters']))
            formatted_string = replace_string + random_string[len(replace_string):]
            return formatted_string
        else:
            return random_string

    def get_person(self, file_format='json'):
        if file_format == 'json':
            person_info = {}
            person_info['country_code'] = self.country_code
            person_info['batch_no'] = self.batch_no
            person_info['person_id'] = self.person_id
            person_info['full_name'] = self.full_name
            person_info['phone_number'] = self.phone_number
            email_parts = person_info['full_name'].split(" ")
            person_info['email'] = email_parts[0].lower() + "." + email_parts[2].lower() + "@gmail.com"
            person_info['created_date'] = self.created_date
            person_info_json = json.dumps(person_info, indent=3)
        return person_info_json


class OSInformation:
    """Class Name: OS Information
    Description: Create operating system information
    """
    pass


def main():
    person = Person(country_code=1);
    record = person.get_person()
    print(record)


if __name__ == "__main__":
    main()
