from app import app, db
from app.models import User, Movie, Cast

# Este decorate retorna as features no terminal
# Por exemplo, no terminal conseguimos gerar o 
# arquivo storage.db, persistir no banco via terminal
# entre outros recursos.
@app.shell_context_processor
def shell_conext():
    return dict(
        app=app,
        db=db,
        User=User,
        Movie=Movie,
        Cast=Cast
    )
if __name__ == "__main__":
    app.run(debug=True)
