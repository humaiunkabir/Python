
import sqlite3 as sq3
from AccountBalanceOperation import AccountBalanceOperation

from AccountHolder import AccountHolder


# tableName
ACCOUNT_HOLDER_TABLE = "accountholder"
ACCOUNT_BALANCE_OPERATION_TABLE = "accountbalanceopration"

# accountholder table field name
EMPID = 'empid'
NAME = 'name'
FATHERSNAME = 'fathersname'
MOTHERSNAME = 'mothersname'
MOBILENO = 'mobileno'
ADDRESS = 'address'
NID = 'nid'
HOMEDISTRICT = 'homedistrict'
PIN = 'pin'

# accountbalanceoperation table field name
EMPID = 'empid'
DEBIT = 'debit'
CREDIT = 'credit'
BALANCE = 'balance'


class DatabaseOperation:

    def __init__(self, databaseName):

        try:
            self.databaseName = databaseName

            conn = sq3.connect(self.databaseName)
            cursore = conn.cursor()
            queryAHT = "CREATE TABLE if not exists " + ACCOUNT_HOLDER_TABLE + "(" + EMPID + " INT PRIMARY KEY , " + NAME + " TEXT, " + FATHERSNAME + " TEXT, " + \
                MOTHERSNAME + " TEXT, " + MOBILENO + " TEXT, " + ADDRESS + " TEXT, " + \
                NID + " TEXT, " + HOMEDISTRICT + " TEXT, " + PIN + " TEXT" + ")"
            print(queryAHT)
            queryABO = "CREATE TABLE if not exists " + ACCOUNT_BALANCE_OPERATION_TABLE + \
                "(" + EMPID + " INT PRIMARY KEY , " + DEBIT + \
                " INT, " + CREDIT + " INT, " + BALANCE + " INT " + ")"
            print(queryABO)
            cursore.execute(queryAHT)
            cursore.execute(queryABO)
            cursore.close()
        except sq3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if conn:
                conn.close()
                print("The SQLite connection is closed")

    def insertOperation(self, operationStatus, amount, obj=AccountHolder()) -> int:

        try:
            conn = sq3.connect(self.databaseName)
            print(conn)
            cursore = conn.cursor()
            valuesAH = (obj.empId, obj.name, obj.fathersName, obj.mothersName,
                        obj.mobileNo, obj.address, obj.nid, obj.homeDistrict, obj.pin)
            queryInsertAH = "INSERT INTO " + ACCOUNT_HOLDER_TABLE + " ( " + EMPID + ", " + NAME + ", " + FATHERSNAME + ", " + MOTHERSNAME + \
                ", " + MOBILENO + ", " + ADDRESS + ", " + NID + ", " + \
                HOMEDISTRICT + ", " + PIN + \
                ")"  " VALUES(?,?,?,?,?,?,?,?,?)"
            print(queryInsertAH)
            empid = obj.empId
            if(operationStatus == 1):
                debit = 0
                credit = 0
                balance = amount
            elif(operationStatus == 2):
                debit = 0
                credit = amount
                balance = self.balance + self.credit
            elif(operationStatus == 3):
                debit = amount
                credit = 0
                balance = self.balance + self.credit
            else:
                return "Invalid Data."

            objABO = AccountBalanceOperation(empid, operationStatus, amount)
            objABO.empId = empid
            objABO.debit = debit
            objABO.credit = credit
            objABO.balance = balance
            valuesABO = (objABO.empId, objABO.debit,
                         objABO.credit, objABO.balance)
            queryInsertABO = "INSERT INTO " + ACCOUNT_BALANCE_OPERATION_TABLE + \
                "(" + EMPID + ", " + DEBIT + ", " + CREDIT + \
                ", " + BALANCE + ")"  " VALUES(?,?,?,?)"
            print(queryInsertABO)
            print(valuesAH)
            print(valuesABO)
            a = cursore.execute(queryInsertAH, valuesAH)
            b = cursore.execute(queryInsertABO, valuesABO)

            result = cursore.execute("""select * from accountholder""")
            print(list(result))
            print(a, b)
            conn.commit()
            conn.close()
            print("Success")
            return 1

        except sq3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if conn:
                conn.close()
                print("The SQLite connection is closed")

    def accountHolderMaxID(self) -> int:
        conn = sq3.connect(self.databaseName)
        cursor = conn.cursor()
        cursor.execute("Select max(empid) as maxId from accountholder")
        row = cursor.fetchone()

        maxId = int(row[0])
        conn.commit()
        conn.close()
        return maxId
