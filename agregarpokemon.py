import psycopg2

URL="postgresql://jesse:NuIyzDWW4PVYHCF7HVRjPrKdMdzGbdi0@dpg-d0d4vq15pdvs73f7o7ag-a.oregon-postgres.render.com/pokemones_nqom"

conn = psycopg2.connect(URL)
cursor=conn.cursor()

pokemons=[
    ("Bulbasaur","Planta"),
    ("Charmander","Fuego")

]

cursor.executemany("ISERT INTO kanto (nombre,tipo) VALUES (%s,%s)", pokemons)

print(cursor.fetchone())

cursor.close()
conn.close()