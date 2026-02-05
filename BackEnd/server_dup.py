from fastapi import HTTPException

from fastapi import FastAPI
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class AnalyticsOut(BaseModel):
    category: str
    total_amount: float

class DateRange(BaseModel):
    start_date: date
    end_date: date
app=FastAPI()

@app.get("/expenses/{expense_date}",response_model=List[Expense])
def get_expense(expense_date:date):
    expense=db_helper.view_expense(expense_date)
    return expense

# @app.get("/analytics/{start_date},{end_date}",response_model=List[AnalyticsOut])
# def get_analytics(start_date:date,end_date:date):
#     expense=db_helper.expense_summary(start_date,end_date)
#     return expense

@app.post("/expenses/{expense_date}")
def post_expense(expense_date:date,expense:List[Expense]):
    db_helper.delete_expense(expense_date)
    for exp in expense:
        db_helper.insert_expense(expense_date,exp.amount,exp.category,exp.notes)
    return "expense posted"

# @app.post("/analytics/", response_model=List[AnalyticsOut])
# def get_analytics(range: DateRange):
#     """ Get category-wise expense summary between two dates """
#     return db_helper.expense_summary( range.start_date, range.end_date )




@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data = db_helper.expense_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the database.")

    total = sum([row['total_amount'] for row in data])

    breakdown = {}
    for row in data:
        percentage = (row['total_amount']/total)*100 if total != 0 else 0
        breakdown[row['category']] = {
            "total": row['total_amount'],
            "percentage": percentage
        }

    return breakdown