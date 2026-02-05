from BackEnd import db_helper

def test_view_expense_aug():
    expense=db_helper.view_expense("2024-8-15")
    assert len(expense)==1
    assert expense[0]["amount"]==10
    assert expense[0]["category"]=="Shopping"
    assert expense[0]["notes"]=="Bought potatoes"

def test_view_expense_invaild():
    expense=db_helper.view_expense("9999-8-15")
    assert len(expense)==0

def test_view_expense_invalidrange():
    expense=db_helper.expensive_summary("2099-8-15","2088-2-3")
    assert len(expense)==0