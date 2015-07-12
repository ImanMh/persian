import re



class TextToDate ():
    @staticmethod
    def convert(text):
        #matches 23/11/1345, 31/11/3234
        standardNumericPattern = '^([0-2][0-9]|3[0-1])\/([0][0-9]|1[0-2])\/[0-9]{0,4}$'
        #matches all standards plus 3/3/3001, 3/04/2133
        noneStandardNumericPattern = '(([0-2][0-9]|3[0-1])|[0-9])\/(([0][0-9]|1[0-2])|[0-9])\/[0-9]{0,4}';

        if (re.match(standardNumericPattern, text)):
            return text
        if (re.match(noneStandardNumericPattern, text)):
            dateSections = text.split('/')
            for i, section in enumerate(dateSections):
                if (i == 2):
                    while len(dateSections[i]) < 4:
                        dateSections[i] = "0" + dateSections[i]
                if (len(section) < 2):
                    dateSections[i] = "0" + section
            delimeter = '/'
            return delimeter.join(dateSections)


        return 1
