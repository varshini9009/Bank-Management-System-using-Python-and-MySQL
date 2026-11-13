# Bank Management System

## Project Description
The Bank Management System is a console-based application developed using Python and MySQL. It allows users to perform basic banking operations such as creating accounts, depositing money, withdrawing money, checking account balances, and viewing transaction history.

The application uses MySQL to store account details and transaction records. Database transactions are used to maintain data consistency during deposit and withdrawal operations.

## Features
- **Create Account:** Create a new bank account with an automatically generated account number.
- **Deposit Money:** Deposit money into an existing account.
- **Withdraw Money:** Withdraw money after checking the available balance.
- **Check Balance:** View account number, account holder name, and current balance.
- **Transaction History:** View previous deposit and withdrawal records.
- **Database Integration:** Store account and transaction details using MySQL.

## Technologies Used
- Python
- MySQL
- MySQL Connector/Python
- python-dotenv

## Project Structure

```text
Bank_Management_System/
│
├── main.py
├── bank_db.sql
├── README.md
├── requirements.txt
|_.env.example
```

## Database Structure

### Accounts Table
Stores bank account information:
- account_id
- account_number
- account_holder
- balance

### Transactions Table
Stores transaction details:
- transaction_id
- account_number
- transaction_type
- amount
- transaction_date

## Installation and Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create the Database

Open MySQL Workbench and execute the SQL commands in `bank_db.sql` to create the database and required tables.

### 4. Configure Environment Variables

Create a `.env` file in the project directory using `.env.example` as a reference.

Add your MySQL credentials:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=bank_db
```

**Note:** The `.env` file contains private database credentials and should never be uploaded to GitHub.

### 5. Run the Application

```bash
python main.py
```

## Learning Outcomes
- Practiced Python functions and control flow.
- Implemented MySQL database connectivity.
- Performed database operations using SQL queries.
- Understood database transactions using commit and rollback.
- Practiced handling banking operations through a console-based application.

