/* fun��es de agrega��o SUM MIN AVG MAX 
usadas b�sicamente pra executar fun��es matem�ticas*/
SELECT TOP 10 SUM(LineTotal) AS "Soma"
FROM Sales.SalesOrderDetail

/* nessa query eu peguei os dez primeiros valores de venda na tabela SalesOrderDetail
somei os valores na coluna LineTotal e criei uma esp�cie de alias pra opera��o, 
chamando de soma usando o AS*/

SELECT TOP 10 MIN(LineTotal) AS "Menor Valor"
FROM Sales.SalesOrderDetail

/* nessa query eu peguei, entre os dez primeiros valores de venda na tabela SalesOrderDetail
o menor valor na coluna LineTotal e criei uma esp�cie de alias pra opera��o, 
chamando de Menor Valor usando o AS*/

SELECT TOP 10 MAX(LineTotal) AS "Maior Valor"
FROM Sales.SalesOrderDetail

/* nessa query eu peguei, entre os dez primeiros valores de venda na tabela SalesOrderDetail
o maior valor na coluna LineTotal e criei uma esp�cie de alias pra opera��o, 
chamando de Maior Valor usando o AS*/

SELECT TOP 10 AVG(LineTotal) AS "Valor M�dio"
FROM Sales.SalesOrderDetail

/* nessa query fiz a m�dia entre os dez primeiros valores de venda 
na tabela SalesOrderDetail e criei uma esp�cie de alias pra opera��o, 
chamando de Valor M�dio usando o AS*/