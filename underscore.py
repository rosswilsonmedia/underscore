class Underscore:
    def map(self, iterable, callback):
        result=[]
        for item in iterable:
            result=result+[callback(item)]
        return result
    def find(self, iterable, callback):
        for item in iterable:
            if callback(item)==True:
                return item
    def filter(self, iterable, callback):
        result=[]
        for item in iterable:
            if callback(item)==True:
                result=result+[item]
        return result
    def reject(self, iterable, callback):
        result=[]
        for item in iterable:
            if callback(item)==False:
                result=result+[item]
        return result

_ = Underscore()
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(evens)

arr=[13,53,7,3,72,4,8,9]
print(_.find(arr, lambda x: x%2 == 0))
print(_.map(arr, lambda x: x%2))