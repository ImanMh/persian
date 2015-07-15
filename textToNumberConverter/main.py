

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

        result = 0
        for part in parted:
            for num_group in TextToNumber.textNumbers:
                if part in num_group:
                    result += num_group[part]
                    break

        return result
