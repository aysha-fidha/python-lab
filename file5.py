import csv
data={"Name":"Anjali","Age":22,"Course":"MCA"}
with open("student.csv","w",newline='') as f:
    writer=csv.writer(f)
    writer.writerow(data.keys())
    writer.writerow(data.values())
with open("student.csv")as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)