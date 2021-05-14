import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-PB7RER35\\SQLEXPRESS;'
                      'Database=demo;'
                      'Trusted_Connection=yes;')

def createOrDropTable():
  cursor = conn.cursor()
  cursor.execute('EXEC tablecreate')
  cursor.close()
  conn.commit()

def insertData(dt,code,status,errorMsg):
  cursor = conn.cursor()
  cursor.execute("INSERT INTO [dbo].[errordata]([insertdate],[code],[status],[errormsg])VALUES(?,?,?,?)",dt,code,status,errorMsg)
  cursor.close()
  conn.commit()