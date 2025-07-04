# 📝 Flask CRUD App com SQLite

Este é um projeto simples de aplicação web usando **Flask** e **SQLite** para gerenciar clientes e produtos. A aplicação permite **adicionar, editar e deletar** registros de ambas as entidades.

![image](https://github.com/user-attachments/assets/eafff502-1c48-4602-a9d5-ad4a0b7fce7d)


## 📦 Funcionalidades

- Cadastrar novos clientes
- Cadastrar novos produtos
- Editar dados existentes
- Deletar registros
- Visualizar listas de clientes e produtos

## ⚙️ Tecnologias Utilizadas

- Python 3
- Flask
- SQLite

## 📂 Estrutura do Projeto

```
.
├── app.py            # Aplicação Flask com rotas e lógica de CRUD
├── form_db.py        # Script para criação do banco de dados SQLite
├── form_db.db        # Banco de dados SQLite
├── templates/        # (Você deve incluir os arquivos HTML aqui)
```

## 🚀 Como Executar

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo
   ```

2. **Crie e ative um ambiente virtual (opcional)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```bash
   pip install flask
   ```

4. **Crie o banco de dados**
   ```bash
   python form_db.py
   ```

5. **Execute a aplicação**
   ```bash
   python app.py
   ```

6. **Acesse no navegador**
   ```
   http://127.0.0.1:5000/
   ```

## ⚠️ Observações

- Os templates HTML (index.html, add_cliente.html, etc.) devem estar na pasta `templates/`.
- O script `form_db.py` recria o banco do zero — ideal para testes, mas **apaga os dados existentes**.
- A `secret_key` está definida como `"admin30"` no `app.py`. Altere para algo mais seguro em produção.

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.


