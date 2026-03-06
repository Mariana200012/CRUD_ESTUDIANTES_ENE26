from flask import Flask, render_template

#crear instancia
app =  Flask(__name__)

#Ruta raiz
@app.route('/')
def index():
    return 'Hola Mundo'

@app.route('/estudiantes')
def getEstudiantes():
    #return 'Aqui se mostraran los estudiantes'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)