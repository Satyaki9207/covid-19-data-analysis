import pandas as pd

def table_info(conn,cur):
    '''
    conn: Database connection object
    cur: Database cursor object
    
    Lists tables present in the database and columns associated with each table
    '''
    tables=cur.execute('SELECT name from sqlite_master where type=\'table\';').fetchall()
    
    for x in tables:
        table_name=x[0]
        table=pd.read_sql('SELECT * FROM {} LIMIT 0'.format(table_name),conn)
        print(table_name)
        
        for col in table.columns:
            print('\t'+col)
        print()
    return None

def bubble_sort(arr1,f=lambda x:x,desc=False):
    '''
    Implements bubble sort on an array based on the value of a given function f
    
    if desc==True
    returns array sorted in desccending order
    '''
    arr=arr1.copy()
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if f(arr[i])>f(arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    if desc:
        return arr[::-1]
    else:
        return arr
    
def bubble_sort_dict(some_dict,desc=False):
    '''
    Implements bubble sort on a dictionary where values are numbers
    '''
    arr=list(some_dict.items())
    sorted_arr=bubble_sort(arr,f=lambda x:x[1],desc=desc)
    
    return {k:v for k,v in sorted_arr}

def convert2float(some_str):
    '''
    Function to clean total charges that contains mix of numbers as strings and empty strings
    
    Input: A string
    Output: returns a float if the string can be converted to float else 0
    '''
    try:
        out=float(some_str)
    except:
        out=0
    return out