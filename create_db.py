import sqlite3
import pandas as pd




def create_db():
    conn=sqlite3.connect('covid_data.db')
    cur=conn.cursor()

    # Reading the files as pandas dataframes 
    covid_deaths=pd.read_csv('covid-deaths.csv')
    covid_deaths['date']=pd.to_datetime(covid_deaths['date'],format='%m/%d/%Y')
    covid_deaths['date']=covid_deaths['date'].dt.strftime('%Y-%m-%d')
    
    covid_vaccination=pd.read_csv('covid-vaccination.csv')
    covid_vaccination['date']=pd.to_datetime(covid_vaccination['date'],format='%m/%d/%Y')
    covid_vaccination['date']=covid_vaccination['date'].dt.strftime('%Y-%m-%d')
    

    # saving the files in sql-db
    covid_deaths.to_sql('covid_deaths',conn,if_exists='replace',index=False)
    covid_vaccination.to_sql('covid_vaccination',conn,if_exists='replace',index=False)

    # commiting the changes
    conn.commit()
    conn.close()
    return None 

if __name__=='__main__':
    create_db()