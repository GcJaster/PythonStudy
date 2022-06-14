import random
from string import digits, ascii_letters


class EmailValidator:
    chars = ascii_letters + digits + '_'

    def __init__(self):
        pass

    @classmethod
    def check_email(cls, email) -> bool:
        if cls.__is_email_str(email):
            to = email[0:email.index('@')]
            after = email[email.index('@'):]
            if 1 <= len(to) <= 100 and 1 <= len(after) <= 50 and '.' in after and '.' not in to:
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def get_random_email(cls):
        after = list(random.sample(cls.chars, random.randint(1, 50)))
        after[random.randint(0, len(after))] = '.'
        email = ''
        for i in range(random.randint(1, 100)):
            email += cls.chars[random.randint(0, len(cls.chars)-1)]
        email += '@' + "".join(after)
        return email

    @staticmethod
    def __is_email_str(email):
        return type(email) is str


def main():
    # res = EmailValidator.check_email("sc_lib@list.ru")  # True
    print(EmailValidator.get_random_email())


if __name__ == '__main__':
    main()