from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import random
import pandas as pd
import re

colors = ['red', 'orange', 'yellow', 'green', 'yellowgreen', 'lime', 'aqua', 'deepskyblue', 'blue',
          'dodgerblue', 'royalblue', 'blueviolet', 'mediumorchid', 'fuchsia', 'hotpink', 'gold',
          'lightcoral', 'tomato', 'rosybrown', 'khaki', 'darkslateblue', 'teal', 'purple', 'crimson',
          'indianred', 'slategray', 'pink', 'darkorange', 'deeppink', 'chocolate']

def chart1(X, Y, ax, kob, fig):
    dict = {'a': X[0], 'b': X[-1]}
    ax.set_title(f'Sells Evolution from {dict["a"]} until {dict["b"]}')
    if kob == 'Vertical':
        ax.tick_params(axis='x', rotation=70)
        bars = ax.bar(X, Y, color=random.sample(colors, k=len(X)))
        textAnno = [ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), '', ha='center', va='bottom') for bar in bars]
        def animate(i):
            for bar, height, text in zip(bars, Y, textAnno):
                current_height = height * (i / 100)
                bar.set_height(current_height)
                text.set_text(f'{current_height}')
                text.set_y(current_height)
    else:
        bars = ax.barh(X, Y, color=random.choices(colors, k=len(X)))
        textAnno = [ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, '', ha='left', va='center') for bar in bars]
        def animate(i):
            for bar, width, text in zip(bars, Y, textAnno):
                   current_width = width * (i / 100)
                   bar.set_width(current_width)
                   text.set_text(f'{current_width}')
                   text.set_x(current_width)
    for _ in range(101):
        ani = FuncAnimation(fig, animate, frames=np.arange(0, 101) ,interval=30, repeat=False)
        fig.canvas.draw()

def chart2(X, Y, ax, fig):
    dict = {'a': X[0], 'b': X[-1]}
    ax.set_title(f'Sells Evolution from {dict["a"]} until {dict["b"]}')
    ym = r'^\d{4}/\d{1,2}$' 
    if bool(re.match(ym, str(X[0]))):
        X = pd.to_datetime(X, format='%Y/%m')
        ser = pd.Series(X)
        ser.dt.strftime('%Y/%m')
        ax.xaxis.set_major_locator(mdates.MonthLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m'))
    else:
        X = pd.to_datetime(X, format='mixed')
        ser = pd.Series(X)
        ser.dt.strftime('%Y')
        ax.xaxis.set_major_locator(mdates.YearLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    a = random.choice(colors)
    line, = ax.plot([], [], marker='o',  linestyle='-', color=a, mfc=a, mec=a)
    padding = (X[-1] - X[0]) * 0.05  #5% padding on each side
    x_start = X[0] - padding
    x_end = X[-1] + padding
    ax.set_xlim(x_start, x_end)
    ax.set_ylim(min(Y) - min(Y), max(Y) + 1000)
    fig.autofmt_xdate()
    annotations = []
    def animate(i):
        x_values = X[:i+1]
        y_values = Y[:i+1]
        line.set_data(x_values, y_values)
        # Clear existing annotations
        for annotation in annotations:
            annotation.remove()
        annotations.clear()

        # Add annotations for each point
        for (x, y) in zip(x_values, y_values):
            annotation = ax.annotate(f'{y}', xy=(x, y), xytext=(5, 5), textcoords='offset points', fontsize=8, color='black')
            annotations.append(annotation)
        return line,

    ani = FuncAnimation(fig, animate, frames=np.arange(0, 101), interval=60, repeat=False)
    fig.canvas.draw()

def chart3(X, Y, ax, fig):
    fy = Y[Y != 0]
    fx = X[Y != 0]
    piecolors = random.sample(colors, k=len(X))
    ax.pie(fy, labels=fx, colors=piecolors, autopct='%1.2f%%')
    dict = {'a': X[0], 'b': X[-1]}
    ax.set_title(f'Sells Evolution from {dict["a"]} until {dict["b"]}')
    legend = [f'{i}: {j:.2f}%' for i, j in zip(X, 100 * (Y / Y.sum()))]
    legend_colors = []
    color_index = 0
    for value in Y:
        if value != 0:
            legend_colors.append(piecolors[color_index])
            color_index += 1
        else:
            legend_colors.append('w')
    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=legend_colors[i], markersize=10)
               for i in range(len(X))]
    ax.legend(handles[:len(X)], legend, title="Info", loc="best", bbox_to_anchor=(1, 0, 0.5, 1))
    fig.canvas.draw()