/* 
GROUP BY - basicamente divide o resultado da busca em grupos
Pra cada grupo vc pode aplicar uma função de agregação, por exemplo:
- Calcular a Soma dos itens 
- Contar o número de itens do grupo

Exemplo: 
SELECT Coluna1, FunçãoAgregação(Coluna2)
FROM NomeTabela
GROUP BY Coluna1
*/

/* Query pra conhecer os dados da tabela em questão */
SELECT *
FROM Sales.SalesOrderDetail

/* Query pra agrupar por SpecialOfferID e somar os valores dos preços dos produtos*/ 
SELECT SpecialOfferID, SUM(UnitPrice) AS "Soma"
FROM Sales.SalesOrderDetail
GROUP BY SpecialOfferID

/*Quanto de cada produto foi vendido até hj?*/
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

/*Query pra saber em Production.Product a média de preço dos produtos com a cor Prata*/
SELECT Color, AVG(ListPrice) AS Média
FROM Production.Product
WHERE Color = 'Silver'
GROUP BY Color

/* 
EXERCÍCIO #1
- Quantas Pessoas tem o mesmo MiddleName, agrupe a informação por MiddleName
*/

SELECT MiddleName, COUNT(MiddleName) AS Contagem
FROM Person.Person
GROUP BY MiddleName

/* 
EXERCÍCIO #2
- Média da Quantidade de cada produto vendido
*/

SELECT ProductID, AVG(OrderQty) AS Média
FROM Sales.SalesOrderDetail
GROUP BY ProductID

/*
EXERCÍCIO #3
- Quais foram as 10 vendas que, no total, tiveram os maiores 
valores de venda (line total) por produto do maior para o menor
*/

SELECT * FROM Sales.SalesOrderDetail

SELECT TOP 10 SalesOrderID, MAX(LineTotal) AS 'Maior Valor' 
FROM Sales.SalesOrderDetail
GROUP BY SalesOrderID

/* SOLUÇÃO DO CURSO */

SELECT TOP 10 ProductID, SUM(LineTotal)
FROM Sales.SalesOrderDetail
GROUP BY ProductID
ORDER BY SUM(LineTotal) DESC;

/* 
EXERCÍCIO #4
- Quantos produtos e qual quantidade média de produtos
temos cadastrados nas ordens de serviço, agrupados pelo ProductID?
*/

SELECT ProductID, AVG(ProductID)
FROM Production.WorkOrder
GROUP BY ProductID

/*Solução do Curso*/
SELECT ProductID, COUNT(ProductID) "Contagem", AVG(OrderQty) AS "Média"
FROM Production.WorkOrder
GROUP BY ProductID

/* tudo bem que o resultado foi bem diferente, 
mas em minha defesa eu não sabia que podia colocar 
mais de duas ordens no select */
