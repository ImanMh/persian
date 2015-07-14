

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
            'dah': 10,
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
        splitted = text.split(' o ')
        numOfWords = len(splitted)
        firstWord = splitted[0]
        numOfDigits = None

        if (text in TextToNumber.tenToNineteen):
            return TextToNumber.tenToNineteen[text]

        for i, number in enumerate(TextToNumber.textNumbers):
            if (firstWord in TextToNumber.textNumbers[i]):
                numOfDigits = i + 1

        result = 0
        expectedTextDigit = 0
        for i in range(0, numOfDigits + 1):
            if (expectedTextDigit >= len(splitted)):
                break
            split = splitted[expectedTextDigit]
            if (split in TextToNumber.textNumbers[numOfDigits - i - 1]):
                result += TextToNumber.textNumbers[numOfDigits - i - 1][split]
                expectedTextDigit += 1

        return result
