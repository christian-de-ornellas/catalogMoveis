from app import app, db

# Este decorate retorna as features no terminal
@app.shell_context_processor
def shell_conext():
    return dict(
        app=app,
        db=db
    )
if __name__ == "__main__":
    app.run(debug=True)
