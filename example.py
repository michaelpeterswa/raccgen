from raccgen import generate

datafile = "lists/data.csv"

raccdata = generate.build(datafile)
pair = generate.racc(raccdata)

print(pair)