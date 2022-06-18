from array import array
import flask
from flask import render_template
import pickle
import sklearn
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np


app = flask.Flask(__name__, template_folder='templates')
@app.route('/', methods = ['POST','GET'])
@app.route('/index', methods = ['POST','GET'])
def main():
    if flask.request.method == 'GET':
        return render_template('main.html')
    if flask.request.method == 'POST':
        with open('fl_net.pkl', 'rb') as f:
            loader_model = pickle.load(f)

        exp = np.array([float(flask.request.form[iter])] for iter in ['Соотношение матрица-наполнитель', 'Плотность, кг/м3',
        'модуль упругости, Гпа', 'Количество отвердителя, м.%', 'Содержание эпоксидных групп, %_2',
        'Температура вспышки, С_2', 'Поверхностная плотность, г/м2', 'Потребление смолы, г/м2',
        'Угол нашивки, град', 'Шаг нашивки', 'Плотность нашивки'])
        print('FRDSFDKSLFSJDFLKSDF')
        print(exp)

        y_pred_LR_all = loader_model.predict(exp)
        
        return render_template ('mail.html', result={y_pred_LR_all})
    
if __name__ == '__main__':
        app.run(debug=True)

        # exp = np.array(float(flask.request.form[iter]) for iter in ['Соотношение матрица-наполнитель', 'Плотность, кг/м3',
        # 'модуль упругости, Гпа', 'Количество отвердителя, м.%', 'Содержание эпоксидных групп, %_2',
        # 'Температура вспышки, С_2', 'Поверхностная плотность, г/м2', 'Потребление смолы, г/м2',
        # 'Угол нашивки, град', 'Шаг нашивки', 'Плотность нашивки']).reshape(-1, 1)

     #   exp = float(flask.request.form[[('Соотношение матрица-наполнитель'), ('Плотность, кг/м3'), ('модуль упругости, Гпа'),
     #   ('Количество отвердителя, м.%'), ('Содержание эпоксидных групп, %_2'), 
     #   ('Температура вспышки, С_2'), ('Поверхностная плотность, г/м2'), ('Потребление смолы, г/м2'), ('Угол нашивки, град'), 
     #   ('Шаг нашивки'), ('Плотность нашивки')]])  
    #    y_pred_LR_all = loader_model.predict[[[exp]]]

      #      exp1 = float(flask.request.form['Соотношение матрица-наполнитель'])
   #     exp2 = float(flask.request.form['Плотность, кг/м3'])
   #     exp3 = float(flask.request.form['модуль упругости, Гпа'])
   #     exp4 = float(flask.request.form['Количество отвердителя, м.%'])
   #     exp5 = float(flask.request.form['Содержание эпоксидных групп, %_2'])
   #     exp6 = float(flask.request.form['Температура вспышки, С_2']) 
   #     exp7 = float(flask.request.form['Поверхностная плотность, г/м2']) 
   #     exp8 = float(flask.request.form['Потребление смолы, г/м2']) 
   #     exp9 = float(flask.request.form['Угол нашивки, град']) 
   #     exp10 = float(flask.request.form['Шаг нашивки']) 
    #    exp11 = float(flask.request.form['Плотность нашивки'])  
    #    y_pred_LR_all = loader_model.predict[[[exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8, exp9, exp10, exp11]]]