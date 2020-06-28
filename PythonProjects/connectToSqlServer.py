
#--------------------------------------------------------
# Using odbc connector to get the data from the database
#--------------------------------------------------------

import pyodbc

driver = 'SQL Server'
server = 'GMOFBIPUB'
db1 = 'GMOFBI'
tcon = 'yes'
uname = 'a-dmvakh'
pword = 'Krevetka37'
select = """SELECT"""
y = list()

cnxn = pyodbc.connect(driver='{SQL Server}'
    ,host=server
    ,database=db1
    ,trusted_connection=tcon
    ,user=uname
    ,password=pword)

cursor = cnxn.cursor()

x = cursor.execute("""SELECT TOP 10
                 [MSSTPID]
                ,[TPName]
                ,[SegmentName]
                ,[CountryName]

  FROM [GMOFBI].[dbo].[vw_Dim_MSS_Organization]
  WHERE CountryName = 'Canada' AND IsTopParent = 'Yes'""")

for i in x:
    y.append(i)

print(y)

