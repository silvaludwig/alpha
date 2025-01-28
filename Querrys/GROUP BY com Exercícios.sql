/* 
GROUP BY - basicamente divide o resultado da busca em grupos
Pra cada grupo vc pode aplicar uma fun��o de agrega��o, por exemplo:
- Calcular a Soma dos itens 
- Contar o n�mero de itens do grupo

Exemplo: 
SELECT Coluna1, Fun��oAgrega��o(Coluna2)
FROM NomeTabela
GROUP BY Coluna1
*/

/* Query pra conhecer os dados da tabela em quest�o */
SELECT *
FROM Sales.SalesOrderDetail

/* Query pra agrupar por SpecialOfferID e somar os valores dos pre�os dos produtos*/ 
SELECT SpecialOfferID, SUM(UnitPrice) AS "Soma"
FROM Sales.SalesOrderDetail
GROUP BY SpecialOfferID

/*Quanto de cada produto foi vendido at� hj?*/
SELECT * FROM Sales.SalesOrderDetail

/* Query usando o GOUP BY e SUM pra somar o valor total de venda de cada produto no banco de dados*/
SELECT ProductID, SUM(UnitPrice) AS Soma
FROM Sales.SalesOrderDetail
GROUP BY ProductID

/*Query usando GOUP BY e COUNT pra contar quantas undades de cada produto foram vendidos*/
SELECT ProductID, COUNT(ProductID) AS Contagem
FROM Sales.SalesOrderDetail
GROUP BY ProductID

/*Query pra saber quantas vezes cada FirstName aparece no banco de dados*/
SELECT FirstName, COUNT(FirstName) AS Contagem 
FROM Person.Person
GROUP BY FirstName

/*Query pra saber em Production.Product a m�dia de pre�o dos produtos com a cor Prata*/
SELECT Color, AVG(ListPrice) AS M�dia
FROM Production.Product
WHERE Color = 'Silver'
GROUP BY Color

/* 
EXERC�CIO #1
- Quantas Pessoas tem o mesmo MiddleName, agrupe a informa��o por MiddleName
*/

SELECT MiddleName, COUNT(MiddleName) AS Contagem
FROM Person.Person
GROUP BY MiddleName

/* 
EXERC�CIO #2
- M�dia da Quantidade de cada produto vendido
*/

SELECT ProductID, AVG(OrderQty) AS M�dia
FROM Sales.SalesOrderDetail
GROUP BY ProductID

/*
EXERC�CIO #3
- Quais foram as 10 vendas que, no total, tiveram os maiores 
valores de venda (line total) por produto do maior para o menor
*/

SELECT * FROM Sales.SalesOrderDetail

SELECT TOP 10 SalesOrderID, MAX(LineTotal) AS 'Maior Valor' 
FROM Sales.SalesOrderDetail
GROUP BY SalesOrderID

/* SOLU��O DO CURSO */

SELECT TOP 10 ProductID, SUM(LineTotal)
FROM Sales.SalesOrderDetail
GROUP BY ProductID
ORDER BY SUM(LineTotal) DESC;

/* 
EXERC�CIO #4
- Quantos produtos e qual quantidade m�dia de produtos
temos cadastrados nas ordens de servi�o, agrupados pelo ProductID?
*/

SELECT ProductID, AVG(ProductID)
FROM Production.WorkOrder
GROUP BY ProductID

/*Solu��o do Curso*/
SELECT ProductID, COUNT(ProductID) "Contagem", AVG(OrderQty) AS "M�dia"
FROM Production.WorkOrder
GROUP BY ProductID

/* tudo bem que o resultado foi bem diferente, 
mas em minha defesa eu n�o sabia que podia colocar 
mais de duas ordens no select */
