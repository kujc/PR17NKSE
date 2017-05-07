from csv import DictReader
import pandas as ps

def fileReaderSmucNesrece():
    fp = open("evidencanesrecnasmuciscihV1.csv", "rt", encoding=" utf -8 ")
    reader = DictReader(fp)
    return [line for line in reader]   #branje



SmucNes = fileReaderSmucNesrece()

SmucNes = ps.DataFrame(SmucNes) # uporaba pandas

print(SmucNes)
