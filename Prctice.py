# import pymysql
# try:
#     query='create table employees1(eno int(5) primary key,ename varchar(10),easal double(10,2),eaddr varchar(10))'
#     con=pymysql.connect(host='localhost',database='jeweldb2',user='root',password='root')
#     cursor=con.cursor()
#     cursor.execute(query)
#     print('Table created successfully')
# except pymysql.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('There IS a problem:',e)
# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()
import pymysql
try:
    con=pymysql.connect(host='localhost',database='jeweldb2',user='root',password='root')
    cursor=con.cursor()
    records=[(1,'Jewel',100000,'angul'),(2,'Deepak',200000,'BBSR'),(3,'Preeti',120000,'Sambalpur'),(4,'Saket',170000,'Cuttack'),(5,'Ayan',1000000,'New york')]
    query='insert into employees1(eno,ename,easal,eaddr)values(%s,%s,%s,%s)'
    cursor.executemany(query,records)
    con.commit()
    print('Record Inserted Into Database')
    cursor.execute('select * from employees1')
    data=cursor.fetchall()
    for row in data:
        print('Empoyee Number:',row[0])
        print('Employee Name:',row[1])
        print('Empoyee Salary:',row[2])
        print('Employee Address:',row[3])
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print('There Is a problem',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()