class LogFile:

    def __init__(self , file_name):
        try:
            self.f = open(file_name , 'r')
        except FileNotFoundError:
            print("File not found")

    def __iter__(self):
        return self
    
    def __next__(self):
        line = self.f.readline()
        if line == "":
            self.f.close()
            raise StopIteration
        return line
    


def filter_errors(log_iterator):
    for i in log_iterator:
        if i.startswith("ERROR"):
            yield i


def uppercase(generator):
    for log in generator:
        yield log.upper()


logs = LogFile("logs.txt")

errors = filter_errors(logs)

upper = uppercase(errors)

for line in upper:
    print(line)