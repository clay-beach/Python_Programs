class Helpers:
    def locate_hyphen(self, hyphen, output):
        count = 0
        prefix = hyphen[:1]
        for i in hyphen:
            if i == '-':
                count += 1
        if prefix.isalpha() and count == 1:
            if hyphen[-1].isalpha():
                output = hyphen
        '''
        if prefix.isalpha() and count == 2:
            print(hyphen)
        '''
        return output


