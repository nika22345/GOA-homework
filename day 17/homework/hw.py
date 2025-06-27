#1) რაში გვეხმარება Indexing-ი?
#შესანიშნავია! აი **სამი უფრო მარტივი დავალება**, რაც ინდექსების გამოყენებას ეხება და შესაფერისია დამწყებთათვის:
#indeqsingi gvexmareba rom movdzebnot konkretuli adgili rame siashi an sityvashi

#2)
#შეიყვანე ტექსტი და დაბეჭდე მისი პირველი სიმბოლო.

#მაგ: "hello" → `h`

text = input("enter a text: ")
print(text[0])
#3)
#მოცემულია სია: `['cat', 'dog', 'fish']`
#დაბეჭდე მეორე ელემენტი (ინდექსინგით).

#ელემენტი უნდა იყოს `"dog"`

animals = ['cat', 'dog', 'fish']
print(animals[1])


#4)
#შეიყვანე ტექსტი და დაბეჭდე ბოლო სიმბოლო ინდექსის მეშვეობით (არა სლაისინგით და არა უარყოფითი ინდექსით).
#მაგ: "hello" → `o` (მოძებნე `len(text) - 1` ინდექსით)

text = input("enter a text: ")
print(text[len(text) - 1])


