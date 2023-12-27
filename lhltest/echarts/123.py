import dmPython
conn=dmPython.connect(user='SYSDBA',password='SYSDBA',server= '192.168.95.128',port=5236)
cursor = conn.cursor()
cursor.execute('select username from dba_users')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()