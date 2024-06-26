import sqlite3

try:
    banco = sqlite3.connect('primeiro.db')

    cursor = banco.cursor()

    cursor.execute("DELETE from pessoas WHERE idade - 34")

    banco.commit()
    banco.close()
    print("foram removido")
except sqlite3.Error as erro:


    print("erro ao excluir ", erro)