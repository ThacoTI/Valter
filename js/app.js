const sqlite3 = require('sqlite3').verbose();

// Conectar ao banco de dados (será criado se não existir)
const db = new sqlite3.Database('novo.db', (err) => {
  if (err) {
    console.error('Erro ao conectar ao banco de dados:', err.message);
  } else {
    console.log('Conectado ao banco de dados primeiro.db');
    
    // Criação da tabela e inserção de dados
    db.serialize(() => {
      // Criar tabela se não existir
      db.run(`CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER
      )`, (err) => {
        if (err) {
          console.error('Erro ao criar a tabela:', err.message);
        } else {
          console.log('Tabela "pessoas" criada ou já existe.');

          // Inserir dados
          db.run(`INSERT INTO pessoas (nome, idade) VALUES (?, ?)`, ['mada', 31], function(err) {
            if (err) {
              console.error('Erro ao inserir dados:', err.message);
            } else {
              console.log('Registro inserido com sucesso.');
            }
          });

          db.run(`INSERT INTO pessoas (nome, idade) VALUES (?, ?)`, ['joao', 28], function(err) {
            if (err) {
              console.error('Erro ao inserir dados:', err.message);
            } else {
              console.log('Registro inserido com sucesso.');
            }
          });

          // Atualizar um registro na tabela pessoas
          db.run("UPDATE pessoas SET nome = ? WHERE idade = ?", ['simao', 28], function(err) {
            if (err) {
              console.error('Erro ao atualizar registro:', err.message);
            } else {
              console.log('Registro atualizado com sucesso.');
            }
          });
        }
      });
    });

    // Fechar a conexão após todas as operações
    db.close((err) => {
      if (err) {
        console.error('Erro ao fechar a conexão com o banco de dados:', err.message);
      } else {
        console.log('Conexão com o banco de dados fechada');
      }
    });
  }
});
