-- create_tables.sql
-- Created by Mohamed Shafik for 100x Data Engineer Assessment

create table customers (
    customer_id int primary key,
    first_name varchar(50),
    last_name varchar(50),
    email varchar(100),
    signup_date date
);

create table orders (
    order_id int primary key,
    customer_id int,
    order_date date,
    amount decimal(10,2)
);

