/* 
AULA 14 - HAVING
Usado com  GROUP BY pra filtrar ainda mais. Basicamente um WHERE pra dados agrupados. 
A diferença é que o WHERE é aplicado antes dos dados serem agrupados, e o HAVING é depois.

Exemplo de sintaxe:
SELECT coluna1, FuncAgreg(coluna2)
FROM NomeTabela
GROUP BY coluna1
HAVING condição
*/

/* 
EXERCÍCIO TESTE
- Quais nomes ocorrem no sistema mais de dez vezes?
*/

SELECT FirstName, COUNT(FirstName) AS "Quantidade"
FROM Person.Person
GROUP BY FirstName
HAVING COUNT(FirstName) > 10

/*
EXEMPLO 2
- Quais produtos que, no total de vendas, acumularam entre 162k e 500k?
*/

SELECT * FROM Sales.SalesOrderDetail

SELECT ProductID
FROM Sales.SalesOrderDetail
GROUP BY LineTotal
HAVING LineTotal >= 162000 and LineTotal <= 500000

SELECT ProductID, SUM(LineTotal) AS "Total"
FROM Sales.SalesOrderDetail
GROUP BY ProductID
HAVING SUM(LineTotal) BETWEEN 162000 AND 500000