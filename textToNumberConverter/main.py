

class TextToNumber ():

    textNumbers = [
        {
            'sefr': 0,
            'yek': 1,
            'do': 2,
            'se': 3,
            'chahar': 4,
            'panj': 5,
            'shesh': 6,
            'haft': 7,
            'hasht': 8,
            'noh': 9,
        },
        {
            'bist': 20,
            'si': 30,
            'chehel': 40,
            'panjah': 50,
            'shast': 60,
            'haftad': 70,
            'hashtad': 80,
            'navad': 90,
        },
        {
            'sad': 100,
            'devist': 200,
            'sisad': 300,
            'chaharsad': 400,
            'pansad': 500,
            'sheshsad': 600,
            'haftsad': 700,
            'hashtsad': 800,
            'nohsad': 900
        },
        {
            'hezar': 1000,
            'dohezar': 2000,
            'sehezar': 3000,
            'chaharhezar': 4000,
            'panjhezar': 5000,
            'sheshhezar': 6000,
            'hafthezar': 7000,
            'hashthezar': 8000,
            'nohhezar': 9000
        },
    ]

    tenToNineteen = {
        'dah': 10,
        'yazdah': 11,
        'davazdah': 12,
        'sizdah': 13,
        'chahardah': 14,
        'panzdah': 15,
        'shanzdah': 16,
        'hefdah': 17,
        'hejdah': 18,
        'noonzdah': 19,
    }


    @staticmethod
    def convert(text):
        parted = text.split(' o ')
        first_word = parted[0]
        num_of_digits = None

        if text in TextToNumber.tenToNineteen:
            return TextToNumber.tenToNineteen[text]

        for i, number in enumerate(TextToNumber.textNumbers):
            if first_word in TextToNumber.textNumbers[i]:
                num_of_digits = i + 1

        result = 0
        expected_text_digit = 0
        for i in range(1, num_of_digits + 1):
            if expected_text_digit >= len(parted):
                break
            part = parted[expected_text_digit]
            if part in TextToNumber.textNumbers[num_of_digits - i]:
                result += TextToNumber.textNumbers[num_of_digits - i][part]
                expected_text_digit += 1
            elif part in TextToNumber.tenToNineteen:
                result += TextToNumber.tenToNineteen[part]
                expected_text_digit += 2

        return result
