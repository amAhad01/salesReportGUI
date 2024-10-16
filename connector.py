import pyodbc

def connector():
    cxn = 'driver={SQL Server}; server=DED\MSQL2022; database=MyProj; trusted_connection=yes;'
    cxn2 = pyodbc.connect(cxn)
    cursor = cxn2.cursor()
    return cursor 