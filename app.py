from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Initialize the counter
counter = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global counter
    if request.method == 'POST':
        if 'add' in request.form:
            counter += 1
        elif 'subtract' in request.form:
            counter -= 10
        return redirect(url_for('index'))
    
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>Counter</title>
          </head>
          <body>
            <div style="text-align: center; margin-top: 50px;">
              <h1>Counter: {{ counter }}</h1>
              <form method="post">
                <button type="submit" name="add">Add 1</button>
                <button type="submit" name="subtract">Subtract 10</button>
              </form>
            </div>
          </body>
        </html>
    ''', counter=counter)

if __name__ == '__main__':
    app.run(debug=True)
