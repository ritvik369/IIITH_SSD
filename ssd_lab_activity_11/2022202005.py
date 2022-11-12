import csv
data=[]
new_data=[]
c=0
with open("./lab_11_data.csv") as csvfile:
    filereader=csv.reader(csvfile, delimiter=',')
    for row in filereader:
        if c==0:
            c=1
            continue
        data.append([row[0],
        float(row[1].replace(',','')),
        float(row[2].replace(',','')),
        float(row[3].replace(',','')),
        float(row[4].replace(',','')),
        float(row[5].replace(',','')),
        float(row[6].replace(',',''))])

#print(data)
new_data=list(filter(lambda x:x[6]>-3.0,data))
#print(len(new_data))
avg_open=sum(map(lambda x:x[1],new_data))
avg_high=sum(map(lambda x:x[2],new_data))
avg_low=sum(map(lambda x:x[3],new_data))
avg_open=avg_open/len(new_data)
avg_high=avg_high/len(new_data)
avg_low=avg_low/len(new_data)
# print(avg_open)
# print(avg_high)
# print(avg_low)
print("Enter a character")
ch=input()
new_data2=list(filter(lambda x:x[0][0]==ch,new_data))
#print(new_data2)
fw=open("avg_output.txt","w")
fw.write(str(avg_open)+"\n")
fw.write(str(avg_high)+"\n")
fw.write(str(avg_low)+"\n")

fw=open("stock_output.txt","w")
for row in new_data2:
    for ele in row:
        fw.write(str(ele)+" ")
    fw.write("\n")
