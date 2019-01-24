from flask import Flask, render_template
app=Flask(__name__)

@app.route('/result')
def result():
    subject1={'Math':80 ,'C':79 ,'JAVA':60}
    print (subject1)
    return render_template('tmp.html', result=subject1)

if __name__ =="__main__":
    app.run(debug=True)
