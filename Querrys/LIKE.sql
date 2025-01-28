/* LIKE para fazer uma busca em dados que se pare�am com...
Exemplo: Suponha que vc quer encontrar uma pessoa cujo nome
se pare�a com Ovi... alguma coisa. Segue a mesma l�gica de
SELECT > FROM > WHERE ... LIKE 'ovi%'*/
SELECT *
FROM Person.Person
WHERE FirstName LIKE 'Ovi%'

/*quando vc n�o souber o come�o da palavra que est� buscando,
� s� colocar o % no in�cio*/
SELECT *
FROM Person.Person
WHERE FirstName LIKE '%nce'

/*e, logicamente, se vc souber s� o miolo da palavra, 
coloca o % no in�cio e no final*/
SELECT *
FROM Person.Person
WHERE FirstName LIKE '%arb%'

/* tbm � poss�vel usar _ pra quando vc quer buscar apenas um caracter
depois do termo que vc n�o sabe o resto*/
SELECT *
FROM Person.Person
WHERE FirstName LIKE '_arb%'

/* a� � s� combinar tudo e fazer um bem-bolado*/