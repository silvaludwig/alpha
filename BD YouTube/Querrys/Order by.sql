SELECT TOP 10 *
FROM Person.Address


SELECT FirstName, LastName
FROM Person.Person
ORDER BY LastName asc


/* obter ProductID dos 10 prod mais caros, listando do mais caro -> barato*/
SELECT TOP 10 *
FROM Production.Product
ORDER BY ListPrice desc

/* solu��o do curso */
SELECT TOP 10 ProductID
FROM Production.Product
ORDER BY ListPrice desc

/* nome e n�mero dos produtos cujo ProductID est� entre 1 e 4 */
SELECT TOP 4 ProductID
FROM Production.Product
ORDER BY Name, ProductNumber asc

/*solu��o do curso*/
SELECT TOP 4 Name, ProductNumber
FROM Production.Product
ORDER BY ProductID