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

