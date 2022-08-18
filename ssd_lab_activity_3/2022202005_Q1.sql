select concat(Fname,Minit,Lname) as Full_name,Ssn,Dno,Dname from DEPARTMENT as depart join (
select Fname,Minit,Lname,Ssn,Dno from EMPLOYEE WHERE Ssn IN(
select Mgr_ssn from DEPARTMENT WHERE Dnumber IN (
select distinct Dno from EMPLOYEE WHERE Ssn IN (
select Essn from
(select Essn,Pno, COALESCE (Hours,0) as Hours from WORKS_ON) AS WORKS
Group by WORKS.Essn HAVING SUM(WORKS.Hours)<40.0)))) AS TABLE_1 WHERE Dno=Dnumber ;
