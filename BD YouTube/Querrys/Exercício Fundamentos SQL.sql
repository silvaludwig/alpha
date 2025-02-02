/*Exercícios sobre os fundamentos
1 - Quantos produtos temos cadastrados que custam mais de 1500?*/
SELECT *
FROM Production.Product
WHERE ListPrice > 1500

/*solução do curso:*/
SELECT COUNT(ListPrice)
FROM Production.Product
WHERE ListPrice > 1500

/*Vou considerar um acerto pq, mesmo que não tenham sido soluções iguais, 
se fosse uma demanda real, eu conseguiria resolver e responder corretamente que
são 39 produtos cadastrados acima de 1500*/


/* 2 - Quantas pessoas temos cadastradas cujo sobrenome se inicia com a letra P?*/
SELECT COUNT(LastName)
FROM Person.Person
WHERE LastName LIKE 'p%'

/*Solução do curso ficou igual a minha, então GG*/

/* 3 - Em quantas cidades únicas estão cadastrados os clientes?*/
SELECT COUNT(City)
FROM Person.Address

/*Solução do curso*/
SELECT COUNT(Distinct(City))
FROM Person.Address

/* A minha solução entrega TODOS os registros de cidade cadastradas, 
enquanto que o exercício pediu somente registros 'únicos', ou seja, 
sem repetições. Faltou o distinct pra ficar completo.*/

/* 4 - QUAIS São as cidades únicas cadastradas no sistema?*/
SELECT DISTINCT(City)
FROM Person.Address

/*Solução igual ao do curso. Mas tbm, era de se esperar, rsrs*/

/* 5 - Quantos produtos VERMELHO custam entre 500 e 1000?*/
SELECT COUNT(Color)
FROM Production.Product
WHERE Color = 'red' AND ListPrice BETWEEN 500 and 1000

/*resultado do curso*/
SELECT COUNT(*)
FROM Production.Product
WHERE Color = 'red'
AND ListPrice BETWEEN 500 AND 1000

/*tbm vou considerar que eu acertei, por mais que a sintaxe esteja diferente,
os resultados foram os mesmos. */


/* 6 - Quantos produtos tem a palavra road no nome?*/

SELECT COUNT(Name)
FROM Production.Product
WHERE Name LIKE 'road'

/*solução do curso:*/
SELECT COUNT(*)
FROM Production.Product
WHERE Name LIKE '%road%'

/* a principal diferença foi a falta do % mesmo*/