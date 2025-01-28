/* funções de agregação SUM MIN AVG MAX 
usadas básicamente pra executar funções matemáticas*/
SELECT TOP 10 SUM(LineTotal) AS "Soma"
FROM Sales.SalesOrderDetail

/* nessa query eu peguei os dez primeiros valores de venda na tabela SalesOrderDetail
somei os valores na coluna LineTotal e criei uma espécie de alias pra operação, 
chamando de soma usando o AS*/

SELECT TOP 10 MIN(LineTotal) AS "Menor Valor"
FROM Sales.SalesOrderDetail

/* nessa query eu peguei, entre os dez primeiros valores de venda na tabela SalesOrderDetail
o menor valor na coluna LineTotal e criei uma espécie de alias pra operação, 
chamando de Menor Valor usando o AS*/

SELECT TOP 10 MAX(LineTotal) AS "Maior Valor"
FROM Sales.SalesOrderDetail

/* nessa query eu peguei, entre os dez primeiros valores de venda na tabela SalesOrderDetail
o maior valor na coluna LineTotal e criei uma espécie de alias pra operação, 
chamando de Maior Valor usando o AS*/

SELECT TOP 10 AVG(LineTotal) AS "Valor Médio"
FROM Sales.SalesOrderDetail

/* nessa query fiz a média entre os dez primeiros valores de venda 
na tabela SalesOrderDetail e criei uma espécie de alias pra operação, 
chamando de Valor Médio usando o AS*/