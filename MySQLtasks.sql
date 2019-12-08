/**
1. Wyświetl imiona, nazwiska oraz pensje pracowników.
2. Wyświetl imiona, nazwiska pracowników. Nadaj aliasy „imie”, „nazwisko” odpowiednim kolumnom.
3. Wyświetl strukturę tabeli departments.
4. Wyświetl zawartość tabeli regions.
5. Wyświetl imiona i nazwiska pracowników w jednej kolumnie.
6. Wyświetl alfabetyczną listę pracowników.
7. Wyświetl nazwiska pracowników w porządku malejącym.
8. Wyświetl nazwiska i pensje pracowników w porządku malejącym wg pensji.
9. Wyświetl imiona, nazwiska i pensje pracowników w porządku rosnącym wg pensji i malejącym wg nazwisk.
10. Wyświetl listę nazwisk. W wyniku nie mogą pojawić się duplikaty nazwisk.
13. Wyświetl imię, nazwisko oraz datę zatrudnienia wszystkich pracowników, których pensja nie znajduje się w przedziale
 [4000, 12 000]. Wyniki posortuj rosnąco wg pensji.
11.Wyświetl dane pracowników, których email kończy się literą G i są zatrudnieni w oddziałach o identyfikatorach 90, 110.
20. Wyświetl nazwy stanowisk, i różnice pomiędzy maksymalnymi i minimalnymi pensjami
(nadaj kolumnie alias ROZNICA). Wyniki posortuj wg różnicy (podaj trzy rozwiązania).
24. Wyświetl minimalną i maksymalną pensję dla stanowisk o nazwie rozpoczynającej się
od ’Sale’.
**/
use hr;

select first_name, last_name, salary from employees;
select first_name as imię, last_name as nazwisko from employees;
--
select * from regions;
select concat_ws(" ",first_name,last_name) as employees from employees;
--
select first_name, last_name, salary from employees order by 2 asc, 3 desc;
select first_name, last_name, hire_date from employees where salary not between 4000 and 12000 order by salary;

select first_name, last_name from employees where employee_id in (100, 102, 105, 107);

select * from employees where commission_pct is null;
select first_name, last_name from employees where first_name like "_e%";
select first_name, last_name, salary + 0.25*salary from employees where department_id like 50;
select country_name from countries order by 1;

select * from employees where department_id in ('70', '80', '110') and salary not between 5000 and 9000 order by salary;
select first_name, last_name, hire_date, salary from employees where job_id = 'st_clerk' and year(hire_date) not between 1996 and 1998;
select first_name, last_name from employees where manager_id is null;
select first_name, last_name from employees where email like "%g" and department_id in (90, 110);
select job_title, max_salary - min_salary as roznica from jobs order by 2;
select distinct first_name from employees where first_name like "k%" or first_name like "a%" order by 1;
select job_title, min_salary, max_salary from jobs where job_title like "Sale%";

-- Wyświetl sumę, średnią, minimalną i maksymalną pensję pracowników kotrych przełożonym nie jest prezes.
select sum(salary), avg(salary), min(salary), max(salary) from employees where manager_id != 100;
-- Wyświetl zestawienie pokazujące sumy zarobków dla poszczególnych stanowisk + średnia.
select sum(salary), avg(salary), job_id from employees group by job_id order by 2;
-- Wyświetl zestawienie pokazujące średnie zarobków dla poszczególnych stanowisk, ale tylko dla tych na których jest zatrudnionych co 
-- najmniej trzech pracowników. W wyniku powinna pojawić się również liczba pracowników zatrudnionych na poszczególnych stanowiskach.
select avg(salary), count(*), job_id from employees
where job_id in ("FI_ACCOUNT", "SA_REP") 
group by job_id
having count(*) >= 3
order by 2 asc;

select first_name, count(*) from employees
group by first_name
having count(*) >= 2
order by 2 desc, 1 desc;

select max(salary), min(salary), max(salary) - min(salary), department_id from employees
where department_id is not null
group by department_id;

-- Wyświetl maksymalną pensję dla działów o identyfikatorach 50,60 i 100.
select max(salary), department_id from employees
where department_id in (50,60,100)
group by department_id;

select location_id, count(*) from departments
group by location_id order by 2 desc;

