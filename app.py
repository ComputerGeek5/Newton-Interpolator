import base64
from io import BytesIO

from flask import Flask, render_template, request
import numpy as np
from matplotlib import pyplot as plt

app = Flask(__name__)
app.app_context().push()

@app.route('/', methods = ['GET'])
def index():
    return render_template("index.html")

@app.route('/interpolate', methods = ['POST', 'GET'])
def interpolate():
    data = request.get_json()
    x = np.array(data['x'])
    y = np.array(data['y'])
    np.set_printoptions(suppress=True)

    # get the divided difference coefficient
    a_s = divided_difference(x, y)[0, :]

    # evaluate on new data points
    x_left = np.amin(x)
    x_right = np.amax(x) + 0.1
    x_new = np.arange(x_left, x_right, .1)
    y_new = newton_polynomial(a_s, x, x_new)

    plt.figure(figsize=(12, 8))
    plt.title('Newton Interpolation')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.plot(x, y, 'bo')
    plt.plot(x_new, y_new)

    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

    # plot_image_name = 'plot.png'
    # plt.savefig(plot_image_name)
    # return str(a_s)

def divided_difference(x, y):
    n = len(y)
    coefficient = np.zeros([n, n])

    # the first column is y
    coefficient[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coefficient[i][j] = \
                (coefficient[i + 1][j - 1] - coefficient[i][j - 1]) / (x[i + j] - x[i])

    return coefficient

def newton_polynomial(coefficient, x_data, x):
    n = len(x_data) - 1
    p = coefficient[n]
    for k in range(1, n + 1):
        p = coefficient[n - k] + (x - x_data[n - k]) * p
    return p

if __name__ == '__main__':
    app.run()
