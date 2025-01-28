/* Select dentro de um grupo específico usando IN
Faz uma busca em um determinado grupo de dados 
sem a necessidade de escrever várias linhas*/
SELECT *
FROM Person.Person
WHERE BusinessEntityID IN (2,7,13)

/* Select dentro de um grupo específico usando NOT IN
Mesmo princípio, porém ao contrário. Esse SELECT vai 
buscar tudo que não estiver na seleção*/
SELECT *
FROM Person.Person
WHERE BusinessEntityID NOT IN (2,7,13)