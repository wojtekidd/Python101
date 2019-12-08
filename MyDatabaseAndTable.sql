create database sda;
use sda;

create table wojtek
(
id int auto_increment primary key,
first_name varchar(30) not null,
last_name varchar(60) not null,
photo blob
);

create table books
(
title varchar(100) default 'nieznany',
author varchar(255),
published date,
isbn char(20) primary key,
category varchar(25),
page_count mediumint not null,
publisher varchar(100) default 'nieznany',
price decimal(10,2)
);

alter table books
change column title title varchar(128), change column author author varchar(128);

alter table books
change column publisher publisher varchar(128) default 'Nieznana';

alter table books
add in_stock int default 0;

insert into books
values(1,'Nausea', 'Jean-Paul Sratre', '12345', 320, 'Frenchy', 12.65 , 12);

select * from books;
alter table books



