CREATE DEFINER=`root`@`localhost` PROCEDURE `SelectName`(City varchar(30))
BEGIN
     SELECT CUST_NAME from customer WHERE WORKING_AREA=City;
END
