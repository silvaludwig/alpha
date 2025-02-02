/* Select dentro de um grupo espec�fico usando IN
Faz uma busca em um determinado grupo de dados 
sem a necessidade de escrever v�rias linhas*/
SELECT *
FROM Person.Person
WHERE BusinessEntityID IN (2,7,13)

/* Select dentro de um grupo espec�fico usando NOT IN
Mesmo princ�pio, por�m ao contr�rio. Esse SELECT vai 
buscar tudo que n�o estiver na sele��o*/
SELECT *
FROM Person.Person
WHERE BusinessEntityID NOT IN (2,7,13)