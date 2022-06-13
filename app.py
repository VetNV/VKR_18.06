import flask
from flask import render_template
import pickle
import sklearn
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


app = flask.Flask(__name__, template_folder='templates')
@app.route('/', methods = ['POST','GET'])
@app.route('/index', methods = ['POST','GET'])
def main():
    if flask.request.method == 'GET':
        return render_template('main.html')
    if flask.request.method == 'POST':
        with open('net_model.pkl', 'rb') as f:
            loader_model = pickle.load(f)
            
        X1 = float(flask.request.form['Соотношение матрица-наполнитель'])
        X2 = float(flask.request.form['Плотность, кг/м3'])
        X3 = float(flask.request.form['модуль упругости, Гпа'])
        X4 = float(flask.request.form['Количество отвердителя, м.%'])
        X5 = float(flask.request.form['Содержание эпоксидных групп, %_2'])
        X6 = float(flask.request.form['Температура вспышки, С_2'])
        X7 = float(flask.request.form['Поверхностная плотность, г/м2'])
        X8 = float(flask.request.form['Потребление смолы, г/м2'])
        X9 = float(flask.request.form['Угол нашивки, град'])
        X10 = float(flask.request.form['Шаг нашивки'])
        X11 = float(flask.request.form['Плотность нашивки'])
        y_pred_LR_all = loader_model.predict([[X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11]])
        
        return render_template ('mail.html', result=y_pred_LR_all)
    
if __name__ == '__main__':
        app.run(debug=True)