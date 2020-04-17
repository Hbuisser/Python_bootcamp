class CsvReader():

    def __init__(self, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.fd = 0
        self.name = sep
        self.header_bool = header
        self.header = None
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        self.fd = open(self.name, "r")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fd.close()

    def getheader(self) :
        if self.header is None :
            self.header = self.fd.readline()
        return self.header

    def getdata(self):
        self.getheader()
        data = ""
        if self.header_bool :
            data += self.header
        if self.skip_bottom is 0 :
            lst = self.fd.readlines()[self.skip_top:]
            #lst[1:] -> 
            #lst[:-1] ->
        else :
            lst = self.fd.readlines()[self.skip_top:-self.skip_bottom]
        for s in lst:
            data += s
        return data

if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        data = file.getdata()
        print(data)
        header = file.getheader()

print(header)
# if __name__ == "__main__":
#     with CsvReader('bad.csv') as file:
#         if file == None:
#             print("File is corrupted")