import re



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

        if (firstWord in TextToNumber.textNumbers[2]):
            numOfDigits = 3
        if (firstWord in TextToNumber.textNumbers[1]):
            numOfDigits = 2
        if (firstWord in TextToNumber.textNumbers[0]):
            numOfDigits = 1

        results = 0
        currentDigit = numOfDigits
        for i, split in enumerate(splitted):
            print(numOfDigits, type(numOfDigits), text)
            results += TextToNumber.textNumbers[currentDigit - 1][split]
            currentDigit -= 1

        return results
