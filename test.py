import pyodbc
import tkinter as tk
class SinhVien:
    def __init__(self, masv, tensv,lop,diachi,ns,daxoa):
        self.masv = masv
        self.tensv = tensv
        self.lop = lop
        self.diachi = diachi
        self.ns = ns
        self.daxoa = daxoa
    def introduce(self):
        print(self.masv+" "+self.tensv+" "+self.lop+" "+self.diachi+" "+self.ns+" "+self.daxoa)


# Create a Tkinter window
root = tk.Tk()

# Create a connection to the SQL Server database
conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-K32FQ05\CSDLPT06;'
    'Database=QUANLYSV;'
    'UID=sa;'
    'PWD=88888888;'
)

# Create a cursor to execute SQL queries
cursor = conn.cursor()

# Execute a SELECT query
cursor.execute('SELECT * FROM SINHVIEN')

# Fetch the results and display them in a Tkinter label
results = cursor.fetchall()
sinhvien=[]
for row in results:
    # struct={'masv':row[0],'tensv':row[1],'lop':row[2],'diachi':row[3],'ns':row[4],'daxoa':row[5]}
    person = SinhVien(row[0],row[1],row[2],row[3],row[4],row[5])
    sinhvien.append(person)

for sv in sinhvien:
    sv.introduce()
    
label = tk.Label(root, text=sinhvien)
label.pack()

# Close the cursor and connection
cursor.close()
conn.close()

# Start the Tkinter event loop
root.mainloop()