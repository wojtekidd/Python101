create database sda;
use sda;
create table wojtek
(
id int auto_increment primary key,
first_name varchar(30) not null,
last_name varchar(60) not null,
photo blob
);
