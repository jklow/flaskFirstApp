from flask import Flask,render_template
app = Flask(__name__)

@app.route('/') 
def home(): 
    #return "Welcome to my home page" #return output to the caller/browser
    return render_template("index.html")

@app.route('/hi',methods=['GET']) 
def hiPage(): 
    return "Hi, how are you?" #return output to the caller/browser

@app.route('/user/<int:userid>')
def getUser(userid):
    msg="Getting data of user id "+str(userid)
    return msg

if __name__ == '__main__':
    app.run(debug=True) #start the flask app with default port 5000
