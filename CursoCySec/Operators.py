platos = ["Paella", "Risotto", "Sushi", "Tacos", "Pizza"]
precios = (15, 12, 20, 10, 8)
tercer_plato = (platos[2])
print(tercer_plato)
precio_tercer_plato = (precios[2])
print(precio_tercer_plato)

platos_seleccionados = (platos[1:4])
print(platos_seleccionados)

menu = {
        "Paella": precios[0],
        "Risotto": precios[1],
        "Sushi": precios[2],
        "Tacos": precios[3],
        "Pizza": precios[4]
        }
print(menu)
#print(menu["Sushi"]);
platos_pares = (platos[0::2])
print(platos_pares)
