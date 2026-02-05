import mysql.connector
from logging_setup import setup_logger


logger=setup_logger("db_helper")


# ----------------DATABASE CONNECTION--------------------------------------
def connection():
        conn=mysql.connector.connect(
         host="localhost",
         user="root",
         passwd="1234",
         database="expense_manager"
        )
        return conn
# ----------------READ THE DATA--------------------------------------
def viewall_expense():
        logger.info(f"viewall_expense is called")
        conn=connection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute("select * from expenses")
        row=cursor.fetchall()
        # for r in row:
        #         print(r)
        conn.close()
        return row
# ----------------READ THE DATA IN PARTICULAR DATE--------------------------------------
def view_expense(Edate):
        logger.info(f"view_expense is called with expense_date={Edate}")
        conn=connection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute("select * from expenses where expense_date=%s",(Edate.strftime("%Y-%m-%d"),))
        row=cursor.fetchall()
        # for r in row:
        #     print(r)
        conn.close()
        return row

# ----------------READ THE DATA SUMMARY IN PARTICULAR DATE--------------------------------------
def expense_summary(sdate,edate):
    logger.info(f"expense_summary is called with Start date={sdate} End date={edate}")
    conn=connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("select category,sum(amount) as total_amount from expenses where "
                   "expense_date between %s and %s group by category;",(sdate,edate))
    row=cursor.fetchall()
    # for r in row:
    #     print(r)
    conn.close()
    return row

# ----------------INSERT THE DATA--------------------------------------
def insert_expense(Edate,amount,category,notes):
        logger.info(f"insert_expense is called with Edate={Edate},amount={amount},category={category},notes={notes}")
        conn=connection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute("insert into expenses(expense_date,amount,category,notes) "
                       "values (%s,%s,%s,%s)",(Edate,amount,category,notes))
        conn.commit()
        print("data inserted")
        conn.close()
# ----------------DELETE THE DATA--------------------------------------
def delete_expense(Edate):
    logger.info(f"delete_expense is called with expense_date={Edate}")
    conn=connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("delete from expenses where expense_date=%s",(Edate,))
    conn.commit()
    print("data deleted")
    conn.close()

#
if __name__=="__main__":
#         # viewall_expense()
#         # view_expense("2024-08-02")
#         # insert_expense("2025-2-12",600,"item","a new headphone")
#         # delete_expense("2025-2-12")
        row=expense_summary( "2024-8-4","2024-9-5")
        for r in row:
            print(r)



        # a=connection()
        # if a.is_connected():
        #         print("Connected to MySQL database")
        # else:
        #         print("Connection to MySQL database failed.")
