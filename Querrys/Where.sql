/* Peças entre 500 e 700 kg */
SELECT Name
FROM Production.Product
WHERE Weight >= 500 and Weight <= 700

/* employees married and salaried */
SELECT *
FROM HumanResources.Employee
WHERE MaritalStatus = 'm' and SalariedFlag = 'true' 

/* Peter Krebs está devendo. conseguir o email. (person.person e person.emailaddress)*/
SELECT *
FROM Person.Person
WHERE FirstName = 'Peter' and LastName = 'Krebs'

SELECT *
FROM Person.EmailAddress
WHERE BusinessEntityID = 26
