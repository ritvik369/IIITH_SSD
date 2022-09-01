CREATE DEFINER=`root`@`localhost` PROCEDURE `SelectInfo`()
BEGIN
     Select CUST_NAME,GRADE from customer WHERE (customer.OPENING_AMT+customer.RECEIVE_AMT>10000);
END
