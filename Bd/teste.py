from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

# Função para inicializar o banco de dados
def init_db():
    banco = sqlite3.connect('teste.db')
    cursor = banco.cursor()
    
    # Criar a tabela se não existir
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER
    )
    """)
    
    # Inserir dados iniciais se a tabela estiver vazia
    cursor.execute("SELECT COUNT(*) FROM pessoas")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", ("mada", 31))
        cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", ("joao", 28))
        banco.commit()
    
    banco.close()

# Rota principal para renderizar o template HTML
@app.route('/')
def index():
    return render_template('index.html')

# Rota para obter os dados da tabela pessoas
@app.route('/get_data', methods=['GET'])
def get_data():
    banco = sqlite3.connect('primeiro.db')
    cursor = banco.cursor()
    
    cursor.execute("SELECT * FROM pessoas")
    pessoas = cursor.fetchall()
    
    banco.close()
    
    # Retornar dados em formato JSON
    return jsonify({'pessoas': pessoas})

if __name__ == '__main__':
    # Inicializar o banco de dados ao iniciar o aplicativo
    init_db()
    
    # Executar o aplicativo Flask
    app.run(debug=True)
