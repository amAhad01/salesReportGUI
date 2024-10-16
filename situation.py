import numpy as np
from charting import chart1, chart2, chart3

def chartCaller(x, y, ax, kob, fig, con, koc):
    X = np.array(x)
    Y = np.array(y)
    if koc == 'Bar':
        chart1(X, Y, ax, kob, fig)
    elif koc == 'Line':
        chart2(X, Y, ax, fig)
    else:
        chart3(X, Y, ax, fig)
    con.close()

def fetcher1(q, con, lim, ax, kob, fig, koc):
    x2, y2, nx, ny = [], [], [], []
    con.execute(q)
    rows = con.fetchall()
    for r in rows:
        x2.append(r[1])
        y2.append(r[0]) 
    begin = f'{lim["h"]}/{lim["b"]}'
    end = f'{lim["h"]}/{lim["c"]}'
    event = begin
    while event != end:
        while 1 <= lim['b'] <= 12:
            if event not in x2:
                nx.append(event)
                ny.append(0)
            else:
                nx.append(event)
                ny.append(y2[x2.index(event)])
            lim['b'] += 1
            event = f'{lim["h"]}/{lim["b"]}'
            if event == end:
                break
        if end not in x2:
            nx.append(end)
            ny.append(0)
        else:
            nx.append(end)
            ny.append(y2[x2.index(end)])
    chartCaller(nx, ny, ax, kob, fig, con, koc)

def fetcher2(q, con, lim, ax, kob, fig, koc):
    x2, y2, nx, ny = [], [], [], []
    con.execute(q)
    rows = con.fetchall()
    for r in rows:
        x2.append(r[1])
        y2.append(r[0]) 
    begin = f'{lim["h"]}/{lim["b"]}'
    end = f'{lim["v"]}/{lim["c"]}'
    event = begin
    while event != end:
        while 1 <= lim['b'] <= 12:
            if event not in x2:
                nx.append(event)
                ny.append(0)
            else:
                nx.append(event)
                ny.append(y2[x2.index(event)])
            lim['b'] += 1
            if lim['b'] >= 13:
                lim['b'] = 1
                lim['h'] += 1
            event = f'{lim["h"]}/{lim["b"]}'
            if event == end:
                break
        if end not in x2:
            nx.append(end)
            ny.append(0)
        else:
            nx.append(end)
            ny.append(y2[x2.index(end)])
        chartCaller(nx, ny, ax, kob, fig, con, koc)

def sit1(x, y, z, con, kob, fig, ax, koc):
    lim = {'h': x, 'b': y, 'c': z}
    q = f"SELECT SUM(price) AS total, CONCAT(orderYear,'/',orderMonth) AS event FROM good \
          INNER JOIN orders ON orders.proIDfk = good.proID \
          GROUP BY orderYear, orderMonth ORDER BY orderYear ASC"
    fetcher1(q, con, lim, ax, kob, fig, koc)
    
def sit2(w, x, y, z, con, kob, fig, ax, koc):
    lim = {'h': w, 'v': x, 'b': y, 'c': z}
    q = f"SELECT SUM(price) AS total, CONCAT(orderYear,'/',orderMonth) AS event FROM good \
          INNER JOIN orders ON orders.proIDfk = good.proID \
          GROUP BY orderYear, orderMonth ORDER BY orderYear ASC"
    fetcher2(q, con, lim, ax, kob, fig, koc)

def sit3(x, y, con, kob, fig, ax, koc):
    lim = {'a': x, 'b': y}
    con.execute(f"SELECT SUM(price) AS total, STR(orderYear) FROM good \
                INNER JOIN orders ON orders.proIDfk = good.proID \
                WHERE orderYear BETWEEN {lim['a']} AND {lim['b']} \
                GROUP BY orderYear ORDER BY orderYear ASC")  
    rows = con.fetchall()
    y2 = [i[0] for i in rows]
    x2 = [j[1] for j in rows]
    chartCaller(x2, y2, ax, kob, fig, con, koc)
