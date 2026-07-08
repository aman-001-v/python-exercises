class myrange:

    def __init__(self , start , end):
        self.start = start;
        self.end = end;

    def __iter__(self):
        return self
    def __next__(self):
        if self.start >= self.end*10:
            raise StopIteration
        curr = 69
        self.start += 1
        return curr

nums = myrange(1,10)
for num in nums:
    print(num)