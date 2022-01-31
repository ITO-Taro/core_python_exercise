
class PythonCoreExercise:

    @classmethod
    def find_modes(cls, x):
        """ finds duplicated values amd return them in dictionary format (i.e., 'vallues': 'frequency') """
        data, modes = {}, {}
        x.sort()
        cnt = 1
        for n in range(1, len(x)):
            if x[n] == x[n-1]:
                cnt += 1
            else:
                data [x[n-1]] = cnt
                cnt = 1
        for k, v in data.items():
            if v == max(data.values()) and v > 1:
                modes[k] = v
        return modes

    def char_counter(self, x):
        """ counts the number of alphabetical characters, numeric characters, and symbolic characters  and returns the counts in that order"""
        chars, digits, symbol = 0, 0, 0
        for i in x.lower():
            if ord(i) in range(97, 123):
                chars += 1
            elif ord(i) in range(48, 58):
                digits += 1
            else:
                symbol += 1
        return chars, digits, symbol

    def char_manupilation(self, x, y):
        """ takes two string values, compares them, manipulates the former to be identical to the latter, and returns the manipulated string """
        if x != y:
            goal = [i for i in y]
            y = [i for i in y]
            y.sort()
            common = [i for i in x if i in y]
            only_y = [i for i in y if not i in common]
            x = list(set(common+only_y))
            x.sort()
            duplicates = self.find_modes(y)
            cnt = 1
            for k , v in duplicates.items():
                while v > cnt:
                    x.append(k)
                    cnt += 1
            for n in range(len(goal)):
                x[n] = goal[n]
            res = "".join(x)
        else:
            res = x
        return res

