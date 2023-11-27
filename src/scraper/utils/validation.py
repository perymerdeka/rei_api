import re

class Validation(object):
    def __init__(self) -> None:
        pass

    def is_valid_phone(self, phone_number: str):
        pattern = re.compile(r'^[\d\-]+$')

        # Lakukan pencocokan dengan pola regex
        match = pattern.match(phone_number)

        # Periksa apakah ada kecocokan dan panjang string tidak kosong
        if match and len(phone_number) > 0:
            return phone_number
        else:
            raise Exception("Ini Ga Valid")