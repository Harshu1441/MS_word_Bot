from flask import Flask, render_template, request





#...

app = Flask(__name__ , template_folder='template')

#...

@app.route('/', methods=['post', 'get'])
def home():
    message = ''
    if request.method == 'POST':
        ID = request.form.get('ID')  # access the data inside 
        fullname = request.form.get('fullname')
        msg = request.form.get('msg')

    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
