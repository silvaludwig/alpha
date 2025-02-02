/*Exerc�cios sobre os fundamentos
1 - Quantos produtos temos cadastrados que custam mais de 1500?*/
SELECT *
FROM Production.Product
WHERE ListPrice > 1500

/*solu��o do curso:*/
SELECT COUNT(ListPrice)
FROM Production.Product
WHERE ListPrice > 1500

/*Vou considerar um acerto pq, mesmo que n�o tenham sido solu��es iguais, 
se fosse uma demanda real, eu conseguiria resolver e responder corretamente que
s�o 39 produtos cadastrados acima de 1500*/


/* 2 - Quantas pessoas temos cadastradas cujo sobrenome se inicia com a letra P?*/
SELECT COUNT(LastName)
FROM Person.Person
WHERE LastName LIKE 'p%'

/*Solu��o do curso ficou igual a minha, ent�o GG*/

/* 3 - Em quantas cidades �nicas est�o cadastrados os clientes?*/
SELECT COUNT(City)
FROM Person.Address

/*Solu��o do curso*/
SELECT COUNT(Distinct(City))
FROM Person.Address

/* A minha solu��o entrega TODOS os registros de cidade cadastradas, 
enquanto que o exerc�cio pediu somente registros '�nicos', ou seja, 
sem repeti��es. Faltou o distinct pra ficar completo.*/

/* 4 - QUAIS S�o as cidades �nicas cadastradas no sistema?*/
SELECT DISTINCT(City)
FROM Person.Address

/*Solu��o igual ao do curso. Mas tbm, era de se esperar, rsrs*/

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

/*solu��o do curso:*/
SELECT COUNT(*)
FROM Production.Product
WHERE Name LIKE '%road%'

/* a principal diferen�a foi a falta do % mesmo*/