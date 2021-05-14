import dal

f = open("D:\\SSIS\source\data.txt", "r")
data = f.read();
p1 = data.split('\n')

dal.createOrDropTable();


for a in p1:
   ar1=a.split(',')
   ar2=ar1[1].split('[')
   text=ar1[1]
   date=ar1[0]
   code=text[0:3]
   status=text[4:9].strip()
   errorMsg= '['+ar2[1]
   dal.insertData(date,code,status,errorMsg)