from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET',"POST"])
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        function = request.form['function']
        pattern = request.form['pattern']
        string = request.form['string']
        if function == 'findall':
            result = re.findall(pattern,string)
        elif function == 'search':
            result = re.search(pattern,string)
            if result:
                result = [result.group()]
        elif function == 'split':
            result = re.split(pattern,string)
        elif function == 'sub':
            result = re.sub(pattern,'',string)
        length = len(result)
        return render_template('result.html', result=result, pattern=pattern, length=length)
    
if __name__ == '__main__':
    app.run(debug=True)