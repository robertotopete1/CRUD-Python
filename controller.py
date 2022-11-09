from flask import Flask, render_template, request
app = Flask(__name__)

#@app.route('/', methods=['GET', 'POST'])
#def index():
#    if request.method == 'POST':
#        nombre = request.form['Nombre']
#        return render_template('/index.html', nombre = nombre)
#    else:
#        return render_template('/index.html')
@app.route('/', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        nombre = request.form['Nombre']
        return render_template('/index.html', nombre = nombre)
    else:
        return render_template('/form.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('/contact.html')

if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)