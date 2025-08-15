niveles_amenaza = ('bajo', 'moderado', 'alto', 'crítico')
amenaza_actual = 'bajo'

if amenaza_actual not in niveles_amenaza :
    print('Selecciona un nivel de amenaza adecuado (bajo, moderado, alto, crítico)')
elif amenaza_actual == 'bajo':
    print("Nivel de amenaza actual:",amenaza_actual)
    print('Actividad recomendada: Realizar auditorías de seguridad regulares.')
elif amenaza_actual == 'moderado':
    print('Actividad recomendada: Reforzar la concienciación de los empleados sobre riesgos de Ciberseguridad.')
elif amenaza_actual == 'alto' :
    print('Actividad recomendada: Implementar medidas de seguridad adicionales y revisar accesos.')
elif amenaza_actual == 'crítico' :
    print('Actividad recomendada: Activar el protocolo de respuesta a incidentes.')
else :
    print('Selecciona un nivel de amenaza adecuado (bajo, moderado, alto, crítico)')
