create database bank;
use bank;

CREATE TABLE accounts (
  account_number int(11) DEFAULT NULL,
  account_holder_name varchar(50) DEFAULT NULL,
  account_holder_surname varchar(50) DEFAULT NULL,
  balance float DEFAULT NULL,
  overdraft_allowed tinyint(1) DEFAULT NULL
);

insert into accounts
(account_number, account_holder_name, account_holder_surname, balance, overdraft_allowed)
VALUES
(111112, 'Julie', 'Smith', 150, true),
(111113, 'James', 'Andrews', 20, false),
(111114, 'Jack', 'Oakes', -70, true),
(111115, 'Jasper', 'Wolf', 200, true);

SELECT *
FROM accounts;

DELIMITER //
CREATE FUNCTION is_eligible (balance INT)
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
	DECLARE customer_status VARCHAR(20);
    IF balance > 100 THEN
		SET customer_status = 'YES';
	ELSEIF (balance >= 50 AND balance <= 100) THEN
		SET customer_status = 'MAYBE';
	ELSEIF balance < 50 THEN
		SET customer_status = 'NO';
	END IF;
    RETURN (customer_status);
END//
DELIMITER ;
        
SELECT
	account_holder_name,
    account_holder_surname,
    balance,
    is_eligible(balance)
FROM accounts;




-- procedures
DELIMITER //
CREATE PROCEDURE Greetings( GreetingWord VARCHAR(100), FirstName VARCHAR(100))
BEGIN
	DECLARE FullGreeting VARCHAR(200);
	SET FullGreeting = CONCAT(GreetingWord,' ',FirstName);
	SELECT FullGreeting;
END//
-- Change Delimiter again
DELIMITER ;

CALL Greetings('Hello', 'Youri');
CALL Greetings('Good evening', 'Varvara');


-- 2nd procedures example
USE bakery;

SELECT *
FROM sweet;

-- Change Delimiter
DELIMITER //
-- Create Stored Procedure
CREATE PROCEDURE InsertValue(
IN id INT, 
IN sweetItem VARCHAR(100),
IN price FLOAT)
BEGIN
INSERT INTO sweet(id,item_name, price)
VALUES (id,sweetItem, price);
END//
-- Change Delimiter again
DELIMITER ;

CALL InsertValue (11, 'cherry_cake', 5);

SELECT *
FROM sweet;

DROP PROCEDURE InsertValue;