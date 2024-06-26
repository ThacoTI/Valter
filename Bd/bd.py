import sqlite3
nome =  "mada"
idade = 31

banco = sqlite3.connect('primeiro.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text, idade integer)")
#cursor.execute("INSERT INTO pessoas VALUES('"+nome+"', "+str(idade)+")")

cursor.execute("UPDATE pessoas SET nome = 'simao' WHERE idade = 28") # subistitui valores 

banco.commit()
""" cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall()) """