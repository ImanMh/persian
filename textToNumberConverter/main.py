

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

    @staticmethod
    def convert(text):
        parted = text.split(' o ')
        single_nums = []

        for part in parted:
            nums = part.split(' ')
            for num in nums:
                single_nums.append(num)

        result = 0
        parsed = []
        for part in single_nums:
            for num_group in TextToNumber.textNumbers:
                if part in num_group:
                    parsed.append(num_group[part])
                    break

        for i in range(0, len(parsed)):
            if i - 1 != -1 and parsed[i - 1] < parsed[i]:
                continue
            if i + 1 == len(parsed):
                result += parsed[i]
                continue
            if parsed[i] < parsed[i + 1]:
                result += parsed[i] * parsed[i + 1]
            else:
                result += parsed[i]

        return result
