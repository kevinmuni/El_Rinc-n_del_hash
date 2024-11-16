from flask import Flask , render_template 

app = Flask(__name__)

# la ruta raiz que devulve la pagina principal 
@app.route('/')
def raiz():
    return render_template('index.html')

# # ahora un recolector de rutas faillas
# @app.errorhandler(404)
# def recolector():
#     return "Pagina no encontrada , vuelve a intentarlo ", 404
#     pass 

if __name__ == '__main__':
    app.run(debug=True,port=3000)
