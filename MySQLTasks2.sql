select first_name, last_name from employees;
desc employees;

select * from employees limit 5;

select first_name from employees;
select distinct job_id from employees;
select distinct job_id, first_name from employees;

select first_name as imie, last_name as nazwisko from employees;
select * from employees order by last_name asc;
select * from employees order by first_name desc, last_name desc;

select job_id, first_name from employees order by job_id asc, first_name desc;
select employee_id, last_name, first_name, email from employees
order by 3 desc, 4 asc;

select first_name, last_name from employees order by job_id;

select last_name, first_name, salary from employees;
select last_name, first_name, salary from employees limit 3,3;

select count(*) as liczba_pracownikow from employees;
select count(*) as liczba_dept from departments;

select count(commission_pct) from employees;
select count(distinct commission_pct) from employees;
select distinct commission_pct from employees order by 1 desc;

select * from employees where commission_pct < 0.20 order by salary asc;
select first_name from employees where first_name = "James";
select * from employees where salary >= 19000 or job_id = "AD_VP";

select * from employees where job_id in ("ad_pres", "ad_vp");
select * from employees where first_name like "a%";
select * from employees where first_name like "%a_";
select * from employees where first_name like "%m";

select * from employees where commission_pct is null;
select first_name, last_name, salary + 1000 from employees;
select employee_id, department_id, employee_id - department_id as differential from employees;

select sum(salary) from employees as sum where first_name like "A%";
select min(salary) from employees;

select count(*), region_id from countries group by region_id;
select count(*), job_id from employees group by job_id;
select avg(salary) from employees where job_id = "IT_PROG";


