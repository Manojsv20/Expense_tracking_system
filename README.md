💰 Expense Tracking System

A full-stack Expense Tracking System built to help users efficiently manage daily expenses, visualize spending patterns, and make smarter financial decisions. The application integrates a FastAPI backend, MySQL database, and an interactive Streamlit dashboard for analytics and reporting.

🚀 Features

✅ Add, update, and delete expenses
✅ Categorize spending for better financial tracking
✅ RESTful APIs for seamless data operations
✅ Interactive analytics dashboard
✅ Visual representation of expense trends
✅ Efficient database integration
✅ User-friendly interface

🏗️ Tech Stack

Frontend

Streamlit – Interactive dashboard and visualization

Backend

FastAPI – High-performance API framework

Python – Core programming language

Database

MySQL – Structured storage for expense data

Other Tools

Uvicorn – ASGI server

Pydantic – Data validation


## 📂 Project Structure

```bash
Expense_tracking_system/
│
├── BackEnd/
│   ├── server.py        # FastAPI application
│   ├── db_helper.py     # Database connection & queries
│   ├── schemas.py       # Pydantic models
│
├── FrontEnd/
│   ├── app.py           # Streamlit main app
│   ├── analytics.py     # Dashboard
│
├── requirements.txt
└── README.md
```


⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Manojsv20/Expense_tracking_system.git
cd Expense_tracking_system

2️⃣ Create Virtual Environment
python -m venv .venv


Activate it:

Windows

.venv\Scripts\activate


Mac/Linux

source .venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Database

Install MySQL

Create a database

Update your database credentials inside:

db_helper.py

▶️ Running the Application
Start FastAPI Server
uvicorn server:app --reload


Server runs at:

👉 http://127.0.0.1:8000

API docs:

👉 http://127.0.0.1:8000/docs

Launch Streamlit Dashboard
streamlit run app.py

📊 Use Cases

Personal finance tracking

Budget management

Expense analytics

Learning full-stack Python development

Demonstrating API + Dashboard integration

🔥 Future Enhancements

User authentication

Cloud deployment

Mobile responsiveness

AI-based spending insights

Export reports (PDF/Excel)

🤝 Contributing

Contributions are welcome!

Fork the repo

Create a feature branch

Commit your changes

Open a Pull Request

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Manoj S V
Aspiring Data Analyst

GitHub:
👉 https://github.com/Manojsv20
Email:
👉manojsv2003@gmail.com
