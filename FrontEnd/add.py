import streamlit as st
from datetime import datetime
import requests

API_URL = "http://localhost:8000"


def add_update_tab():
    expense_date = st.date_input("Expense Date", datetime(2024, 8, 3))
    date_str = expense_date.strftime("%Y-%m-%d")

    try:
        response = requests.get(f"{API_URL}/expenses/{expense_date}")
        if response.status_code == 200:
            existing_expense = response.json()
        else:
            st.error(f"Failed to fetch expenses: {response.status_code}")
            existing_expense = []
    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to API. Make sure the backend server is running on port 8000.")
        existing_expense = []

    categories = ["Item", "Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form(key=f"Expense table_{date_str}"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")
        rows = max(5, len(existing_expense))
        expenses = []
        for i in range(rows):
            if i < len(existing_expense):
                amount = existing_expense[i]["amount"]
                category = existing_expense[i]["category"]
                notes = existing_expense[i]["notes"]
            else:
                amount = 0.0
                category = "Other"
                notes = ""

            col1, col2, col3 = st.columns(3)
            with col1:
                amount = st.number_input(label="Amount", min_value=0.0, step=1.0, value=amount, key=f"{date_str}_amount_{i}",
                                         label_visibility="collapsed")
            with col2:
                category = st.selectbox(label="category", options=categories, index=categories.index(category),
                                        key=f"{date_str}_category_{i}", label_visibility="collapsed")
            with col3:
                note_input = st.text_input(label="Note", value=notes, key=f"{date_str}_Note_{i}", label_visibility="collapsed")
            expenses.append({
                "amount": amount,
                "category": category,
                "notes": note_input
            })

        submit_button = st.form_submit_button(label="submit")
        if submit_button:
            filtered_expenses = [expense for expense in expenses if expense["amount"] > 0]

            response = requests.post(f"{API_URL}/expenses/{expense_date}", json=filtered_expenses)
            if response.status_code == 200:
                st.success("Expenses updated successfully!")
            else:
                st.error("Failed to update expenses.")
# import streamlit as st
# from datetime import datetime
# import requests
#
# API_URL = "http://localhost:8000"
#
#
# def add_update_tab():
#     st.subheader("Add / Update Expenses")
#
#     expense_date = st.date_input(
#         "Expense Date",
#         value=datetime(2024, 8, 3)
#     )
#
#     date_str = expense_date.strftime("%Y-%m-%d")
#
#     # ---------------- Fetch expenses for selected date ----------------
#     try:
#         response = requests.get(f"{API_URL}/expenses/{date_str}")
#         existing_expense = response.json() if response.status_code == 200 else []
#     except requests.exceptions.ConnectionError:
#         st.error("Backend server is not running")
#         return
#
#     categories = ["Item", "Rent", "Food", "Shopping", "Entertainment", "Other"]
#
#     # ---------------- Form ----------------
#     with st.form(key=f"expense_form_{date_str}"):
#
#         col1, col2, col3 = st.columns(3)
#         col1.write("Amount")
#         col2.write("Category")
#         col3.write("Notes")
#
#         rows = max(5, len(existing_expense))
#         expenses = []
#
#         for i in range(rows):
#             if i < len(existing_expense):
#                 amount = float(existing_expense[i]["amount"])
#                 category = existing_expense[i]["category"]
#                 notes = existing_expense[i]["notes"]
#             else:
#                 amount = 0.0
#                 category = "Other"
#                 notes = ""
#
#             c1, c2, c3 = st.columns(3)
#
#             with c1:
#                 amount = st.number_input(
#                     "",
#                     min_value=0.0,
#                     value=amount,
#                     key=f"{date_str}_amount_{i}"
#                 )
#
#             with c2:
#                 category = st.selectbox(
#                     "",
#                     categories,
#                     index=categories.index(category),
#                     key=f"{date_str}_category_{i}"
#                 )
#
#             with c3:
#                 notes = st.text_input(
#                     "",
#                     value=notes,
#                     key=f"{date_str}_notes_{i}"
#                 )
#
#             if amount > 0:
#                 expenses.append({
#                     "amount": amount,
#                     "category": category,
#                     "notes": notes
#                 })
#
#         submitted = st.form_submit_button("Save Expenses")
#
#     # ---------------- Submit ----------------
#     if submitted:
#         response = requests.post(
#             f"{API_URL}/expenses/{date_str}",
#             json=expenses
#         )
#
#         if response.status_code == 200:
#             st.success("Expenses saved successfully")
#             st.rerun()
#         else:
#             st.error("Failed to save expenses")
