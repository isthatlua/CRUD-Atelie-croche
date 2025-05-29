from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    con = sql.connect('form_db.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    
    # Buscar dados dos clientes
    cur.execute("SELECT * FROM cliente")   
    clientes_data = cur.fetchall()
    
    # Buscar dados dos produtos
    cur.execute("SELECT * FROM produtos")
    produtos_data = cur.fetchall()
    
    con.close() # Fechar conexão após buscar todos os dados
    
    return render_template("index.html", datas=clientes_data, produtos=produtos_data)

@app.route("/add_cliente", methods=["POST", "GET"])
def add_cliente():
    if request.method == "POST":
        nome = request.form["nome"]
        telefone = request.form["telefone"]
        
        con = sql.connect('form_db.db')
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO cliente (NOME, TELEFONE) VALUES (?, ?)", (nome, telefone))
            con.commit()
            flash("Cliente adicionado com sucesso!", "success")
        except Exception as e:
            con.rollback()
            flash(f"Erro ao adicionar cliente: {e}", "danger")
        finally:
            con.close()
        return redirect(url_for("index"))
    
    return render_template("add_cliente.html")

@app.route("/edit_cliente/<string:id>", methods=["POST", "GET"])
def edit_cliente(id):
    if request.method == "POST":
        nome = request.form["nome"]
        telefone = request.form["telefone"]
        con = sql.connect('form_db.db')
        cur = con.cursor()
        try:
            cur.execute("UPDATE cliente SET NOME=?, TELEFONE=? WHERE ID=?", (nome, telefone, id))
            con.commit()
            flash("Cliente atualizado com sucesso!", "success")
        except Exception as e:
            con.rollback()
            flash(f"Erro ao atualizar cliente: {e}", "danger")
        finally:
            con.close()
        return redirect(url_for("index"))
    
    con = sql.connect('form_db.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM cliente WHERE ID=?", (id,))
    data = cur.fetchone()
    con.close()
    if data is None:
        flash("Cliente não encontrado!", "warning")
        return redirect(url_for("index"))
    return render_template("edit_cliente.html", cliente=data)

@app.route("/delete_cliente/<string:id>", methods=["GET"])
def delete_cliente(id):
    con = sql.connect('form_db.db')
    cur = con.cursor()
    try:
        cur.execute("DELETE FROM cliente WHERE ID=?", (id,))
        con.commit()
        flash("Cliente deletado com sucesso!", "warning")
    except Exception as e:
        con.rollback()
        flash(f"Erro ao deletar cliente: {e}", "danger")
    finally:
        con.close()
    return redirect(url_for("index"))

# --- Rotas de Produto ---
@app.route("/add_produto", methods=["POST", "GET"])
def add_produto():
    if request.method == "POST":
        nome_produto = request.form["nome_produto"]
        descricao_produto = request.form["descricao_produto"]
        preco_produto = request.form["preco_produto"]
        
        con = sql.connect('form_db.db')
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO produtos (NOME, DESCRICAO, PRECO) VALUES (?, ?, ?)", 
                        (nome_produto, descricao_produto, preco_produto))
            con.commit()
            flash("Produto adicionado com sucesso!", "success")
        except Exception as e:
            con.rollback()
            flash(f"Erro ao adicionar produto: {e}", "danger")
        finally:
            con.close()
        return redirect(url_for("index"))
    
    return render_template("add_produto.html")

@app.route("/edit_produto/<string:id_produto>", methods=["POST", "GET"])
def edit_produto(id_produto):
    if request.method == "POST":
        nome_produto = request.form["nome_produto"]
        descricao_produto = request.form["descricao_produto"]
        preco_produto = request.form["preco_produto"]
        
        con = sql.connect('form_db.db')
        cur = con.cursor()
        try:
            cur.execute("UPDATE produtos SET NOME=?, DESCRICAO=?, PRECO=? WHERE ID_PRODUTO=?", 
                        (nome_produto, descricao_produto, preco_produto, id_produto))
            con.commit()
            flash("Produto atualizado com sucesso!", "success")
        except Exception as e:
            con.rollback()
            flash(f"Erro ao atualizar produto: {e}", "danger")
        finally:
            con.close()
        return redirect(url_for("index"))

    con = sql.connect('form_db.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM produtos WHERE ID_PRODUTO=?", (id_produto,))
    produto_data = cur.fetchone()
    con.close()
    
    if produto_data is None:
        flash("Produto não encontrado!", "warning")
        return redirect(url_for("index"))
        
    return render_template("edit_produto.html", produto=produto_data)

@app.route("/delete_produto/<string:id_produto>", methods=["GET"])
def delete_produto(id_produto):
    con = sql.connect('form_db.db')
    cur = con.cursor()
    try:
        cur.execute("DELETE FROM produtos WHERE ID_PRODUTO=?", (id_produto,))
        con.commit()
        flash("Produto deletado com sucesso!", "warning")
    except Exception as e:
        con.rollback()
        flash(f"Erro ao deletar produto: {e}", "danger")
    finally:
        con.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.secret_key = "admin30" # Mantenha sua secret_key
    app.run(debug=True)
    