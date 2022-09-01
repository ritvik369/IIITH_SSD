CREATE DEFINER=`root`@`localhost` PROCEDURE `SUMS`(num1 int(30),num2 int(30))
BEGIN
     select num1+num2;
END
