/* LIKE para fazer uma busca em dados que se pareçam com...
Exemplo: Suponha que vc quer encontrar uma pessoa cujo nome
se pareça com Ovi... alguma coisa. Segue a mesma lógica de
SELECT > FROM > WHERE ... LIKE 'ovi%'*/
SELECT *
FROM Person.Person
WHERE FirstName LIKE 'Ovi%'

/*quando vc não souber o começo da palavra que está buscando,
é só colocar o % no início*/
SELECT *
FROM Person.Person
WHERE FirstName LIKE '%nce'

/*e, logicamente, se vc souber só o miolo da palavra, 
coloca o % no início e no final*/
SELECT *
FROM Person.Person
WHERE FirstName LIKE '%arb%'

/* tbm é possível usar _ pra quando vc quer buscar apenas um caracter
depois do termo que vc não sabe o resto*/
SELECT *
FROM Person.Person
WHERE FirstName LIKE '_arb%'

/* aí é só combinar tudo e fazer um bem-bolado*/