from flask import Flask, render_template, request

app = Flask('app')

@app.route('/')
def index_page():
  return render_template ('BioM.html')

@app.route('/BioCh')
def BioCh():
    return render_template('BioCh.html')
    
@app.route('/BioC')
def BioC():
    return render_template('BioC.html')

@app.route('/BioR')
def BioR():
    return render_template('BioR.html')


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)