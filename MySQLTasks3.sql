SELECT e.employee_id, e.first_name, e.last_name, d.department_name
FROM employees e 
RIGHT JOIN departments d
ON e.department_id = d.department_id;

select * from employees where employee_id = 178;

-- Napisz zapytanie aby wyświetlić imię, nazwisko, numer działu i nazwę działu dla każdego pracownika.

select e.first_name, e.last_name, e.department_id, d.department_name
from employees e
left join departments d
on e.department_id = d.department_id;

--  Napisz zapytanie aby wyświetlić imię i nazwisko, departament, miasto i stan dla pracowników z departamentu IT.
select e.first_name, e.last_name, d.department_name, l.city, l.state_province
from employees e
join departments d
on e.department_id = d.department_id
join locations l
on d.location_id = l.location_id
where d.department_name = 'IT';

-- Napisz zapytanie aby wyświetlić imię, nazwisko, numer działu i nazwę działu dla wszystkich pracowników z działu 80 lub 40.
select e.first_name, e.last_name, d.department_id, d.department_name
from employees e
join departments d
on e.department_id = d.department_id
where d.department_id in (40,80);

-- Napisz zapytanie aby wyświetlić tych pracowników, którzy w posiadją lietrę z w imieniu, a także wyświetlić ich nazwisko, departament, 
-- miasto i stan.
select e.first_name, e.last_name, d.department_id, d.department_name, l.city, l.state_province
from employees e
join departments d
on e.department_id = d.department_id
join locations l
on d.location_id = l.location_id
where e.first_name like "%z%";

-- Napisz zapytanie aby wyświetlić wszystkie działy, w których nie ma żadnego pracownika.
select d.department_name, e.last_name, e.first_name, e.employee_id
from departments d
left join employees e
on e.department_id = d.department_id
where employee_id is null;

-- Napisz zapytanie aby wyświetlić imiona wszystkich pracowników, w tym imię ich menedżera.
select e.last_name as pracownik, m.last_name as manager
from employees e
join employees m
on m.employee_id = e.manager_id;

-- Napisz zapytanie aby wyświetlić ID pracownika, nazwę pracy, liczbę dni przepracowanych dla wszystkich zadań w dziale 80
select jb.employee_id, d.department_name, jb.start_date, jb.end_date, datediff(jb.end_date, jb.start_date) from job_history jb
join departments d
on jb.department_id = d.department_id
where d.department_id = 80;

-- Napisz zapytanie aby wyświetlić nazwę działu, średnią pensję pracowników oraz liczbę pracowników zatrudnionych
-- w każdym dziale, którzy otrzymali prowizję.
select d.department_name, avg(e.salary) as avg_salary, count(*) as empl_num
from employees e
join departments d
on e.department_id = d.department_id
where e.commission_pct is not null
group by department_name;
-- Napisz zapytanie aby wyświetlić imię, nazwisko i numer działu dla pracowników, 
-- którzy pracują w tym samym dziale, co pracownik, który ma nazwisko Taylor.
select e.department_id, e.first_name, e.last_name
from employees e
join employees s
on e.department_id = s.department_id and s.last_name = 'Taylor';

select first_name, last_name, department_id from employees
where department_id in (select department_id from employees where last_name like 'Taylor');

-- Wyświetl wszystkich pracowników którzy zarabiają więcej niż wynosi średnia zarobków wszystkich pracowników w dziale Sales
-- i nie są z działu Sales

select * from employees where salary > (select round(avg(salary),2) from employees 
where department_id = (select department_id from departments where department_name = 'Sales'))
and department_id != (select department_id from departments where department_name = 'Sales');

-- Napisz zapytanie aby wyświetlić imię, nazwisko, numer działu i nazwę dla wszystkich pracowników, którzy mają lub nie mają żadnego działu.

select * from employees

-- Wyświetl wszystkie nazwy regionów przyporządkowując je do nazw krajow

select r.region_name as Region, c.country_name as Country 
from regions r
join countries c
on r.region_id = c.region_id;

-- Wyświetl różnicę pomiędzy najwyższymi a najniższymi zarobkami w departamencie “Finance”
select max(e.salary) - min(salary),  d.department_name from employees e
join departments d
on e.department_id = d.department_id
where d.department_name = 'Finance';

select e.last_name, r.region_name from employees e
join departments d
on e.department_id = d.department_id
join locations l
on d.location_id = l.location_id
join countries c
on l.country_id = c.country_id
join regions r
on c.region_id = r.region_id;

-- Union

select first_name
from employees
union
select last_name
from employees;

-- Union all

select first_name
from employees
union all
select first_name
from employees;

select first_name, last_name, department_id
from employees 
where department_id in (50,80);

-- Join old-school
select e.first_name, e.last_name, d.department_name from employees e, departments d
where e.department_id = d.department_id;

select e.first_name, e.last_name, d.department_name from employees e
join departments d
where e.department_id = d.department_id;

INSERT INTO books (title, author, published, isbn, category, page_count, publisher, price) VALUES ('Spring w akcji. Wydanie IV', 'Craig Walls', '2017-08-13', '234-83-283-0849-1', 'programowanie java', 624, 'Helion', 89.00);
INSERT INTO books (title, author, published, isbn, category, page_count, publisher, price) VALUES ('MySQL. Vademecum profesjonalisty', 'Paul DuBois', '2016-03-29', '246-83-246-8146-9', 'bazy danych', 1216, 'Helion', 149.00);
INSERT INTO books (title, author, published, isbn, category, page_count, publisher, price) VALUES ('ORACLE-sql', 'Marek Mycha', '2016-08-13', '978-82-283-0849-8', 'programowanie sql', 454, 'Helion', 234.00);
INSERT INTO books (title, author, published, isbn, category, page_count, publisher, price) VALUES ('ORACLE-administracja', 'Paweł Nowak', '2015-03-28', '918-83-246-8146-5', 'bazy danych', 16, 'Helion', 1349.00);
INSERT INTO books (title, author, published, isbn, category, page_count, publisher, price) VALUES ('MS_SQL- bazy', 'Luja Śliwa', '2013-01-13', '323-82-283-0849-7', 'bazy danych', 6224, 'Helion', 2354.00);
INSERT INTO books (title, author, published, isbn, category, page_count, publisher, price) VALUES ('MS_SQL- programowanie', 'Mariusz Oziębły', '2012-04-15', '234-83-246-8146-4', 'programowanie sql', 162, 'Helion', 319.00);
INSERT INTO books (title, author, published, isbn, category, page_count, publisher, price) VALUES ('IBW', 'Adam Jakis', '2014-05-16', '345-83-246-8132-9', 'programowanie ibm', 262, 'Matrix', 198.00);
INSERT INTO books (title, author, published, isbn, category, page_count, publisher, price) VALUES ('IBM-DB2', 'Agata Loy', '2011-01-10', '678-23-316-913-1', 'bazy danych', 762, 'Matrix', 18.00);

select * from books where category = 'bazy danych';

create table db_books as select id, title, author, published, isbn, page_count, publisher, price, in_stock from books
where category = "bazy danych";

create table js_books as select id, title, author, published, isbn, page_count, publisher, price, in_stock from books
where category = "programowanie java";

select * from db_books;
select * from js_books;






