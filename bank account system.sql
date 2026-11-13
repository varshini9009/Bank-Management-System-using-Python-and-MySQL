--- creating database---
create database bank_db;

--- use database---
use bank_db;

--- creating table---
create table accounts
(account_id int auto_increment primary key,
account_number varchar(50) unique,
account_holder varchar(50),
balance decimal(10,2)default 0);

create table transactions
(transaction_id int auto_increment primary key,
account_number varchar(50),
transaction_type varchar(20),
amount decimal(10,2),
transaction_date timestamp default current_timestamp,
foreign key(account_number)
references accounts(account_number));

select*from transactions;
