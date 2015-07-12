import re



class TextToNumber ():

    zeroToTwenty = {
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
        'yazdah': 11,
        'davazdah': 12,
        'sizdah': 13,
        'chahardah': 14,
        'panzdah': 15,
        'shanzdah': 16,
        'hefdah': 17,
        'hejdah': 18,
        'noonzdah': 19,
        'bist': 20
    }

    twoDigitNumbers = {
        'bist': 20,
        'si': 30,
        'chehel': 40,
        'panjah': 50,
        'shast': 60,
        'haftad': 70,
        'hashtad': 80,
        'navad': 90,
    }

    @staticmethod
    def convert(text):
        if (len(text.split(' ')) == 1 ):
            if (text in TextToNumber.zeroToTwenty):
                return TextToNumber.zeroToTwenty[text]
            if (text in TextToNumber.twoDigitNumbers):
                return TextToNumber.twoDigitNumbers[text]
        else:
            sections = text.split(' ')
            numberParts = []
            numberParts.append(TextToNumber.twoDigitNumbers[sections[0]])
            numberParts.append(TextToNumber.zeroToTwenty[sections[2]])
            return numberParts[0] + numberParts[1]

        raise ValueError('Could not detect the input you just passed: ' + text)
