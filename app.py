import flask
from flask import render_template
import pickle
import sklearn
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


print('Hello')
#model_load = pickle.load(open('C:\Users\NVetchinov\Desktop\python\видео\ВКР\Flask\\reg_PL_2_CU.pkl', 'rb'))
app = flask.Flask(__name__, template_folder='temp')
@app.route('/', methods = ['POST','GET'])
@app.route('/index', methods = ['POST','GET'])
def main():
    if flask.request.method == 'GET':
        return render_template('main.html')
    if flask.request.method == 'POST':
        with open('C:\Users\NVetchinov\Desktop\python\видео\ВКР\Flask\\reg_PL_2_CU.pkl', 'rb') as f:
            loader_model = pickle.load(f)
            
        exp = float(flask.request.form['experience'])
        y_pred = loader_model.predict([[exp]])
        
        return render_template ('mail.html', result=y_pred)
    
if __name__ == '__main__':
        app.run()