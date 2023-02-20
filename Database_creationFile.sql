create database passenger_details;
use passenger_details;
create table personal(name varchar(20),
                    Gender varchar(20),
                    Mobile_no varchar(10),
                    Email varchar(50),
                    Addhar varchar(15)not null,
                    passward varchar(15),
                    state boolean default 0,
                    total_balance float default 0,
                    primary key(addhar)
                    );