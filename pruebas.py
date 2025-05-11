import psycopg2

URL="postgresql://jesse:NuIyzDWW4PVYHCF7HVRjPrKdMdzGbdi0@dpg-d0d4vq15pdvs73f7o7ag-a.oregon-postgres.render.com/pokemones_nqom"


conn = psycopg2.connect(URL)
cursor=conn.cursor()

cursor.execute("""DROP TABLE kanto;""")

cursor.execute("""CREATE TABLE IF NOT EXISTS kanto (
               id SERIAL PRIMARY KEY,
               numero NUMERIC UNIQUE,
               nombre VARCHAR(50) UNIQUE, 
               tipo1 VARCHAR (50),
               tipo2 VARCHAR (50))"""
               )


conn.commit()
cursor.close()
conn.close()