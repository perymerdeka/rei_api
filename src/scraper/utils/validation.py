import re

from rich import print

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
    def is_valid_pages_number(self, page_number: str) -> int:
        # Mencari angka dalam teks menggunakan regex
        matches = re.findall(r'\d+', page_number)

        # Mengambil hasil pertama (jika ada)
        if matches:
            result = int(matches[0])
            print("Extracted Page Number :", result)
            return result
        else:
            raise Exception(matches)