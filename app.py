from flask import Flask, render_template, request
import pymssql



conn = pymssql.connect("--database-url--", "username", "password", "database-name")
cursor = conn.cursor(as_dict=True)


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

        
        cursor.execute("INSERT INTO --table name-- (ID, fullname, msg) VALUES(%s, %s, %s)", (ID , fullname , msg))
        for row in cursor:
            print("SELECT TOP (1000) * FROM tablename")

        conn.commit()

    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)