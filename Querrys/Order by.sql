SELECT TOP 10 *
FROM Person.Address


SELECT FirstName, LastName
FROM Person.Person
ORDER BY LastName asc


/* obter ProductID dos 10 prod mais caros, listando do mais caro -> barato*/
SELECT TOP 10 *
FROM Production.Product
ORDER BY ListPrice desc

/* solução do curso */
SELECT TOP 10 ProductID
FROM Production.Product
ORDER BY ListPrice desc

/* nome e número dos produtos cujo ProductID está entre 1 e 4 */
SELECT TOP 4 ProductID
FROM Production.Product
ORDER BY Name, ProductNumber asc

/*solução do curso*/
SELECT TOP 4 Name, ProductNumber
FROM Production.Product
ORDER BY ProductID