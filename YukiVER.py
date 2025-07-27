import fastf1
from fastf1.plotting import setup_mpl
import matplotlib.pyplot as plt
import os  

# Creamos manualmente el directorio si no existe
cache_dir = 'f1_cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

# Habilitamos la caché con método seguro
fastf1.Cache.enable_cache(cache_dir)

# Seleccionamos una carrera
session = fastf1.get_session(2024, 'Monza', 'Race')
session.load()  

# Pilotos a comparar
drivers = {
    'Yuki Tsunoda': 'TSU',
    'Max Verstappen': 'VER'
}

#Colores y estilos para cada piloto
colors = ['blue', 'orange']

# Bucle principal
for i, (name, code) in enumerate(drivers.items()):
    laps = session.laps.pick_drivers(code).reset_index(drop=True)
    fastest_lap = laps.loc[laps['LapTime'] == laps['LapTime'].min()]
    pit_laps = laps[laps['PitInTime'].notnull()]

    plt.plot(laps['LapNumber'], laps['LapTime'].dt.total_seconds(),
             label=f'{name}', color=colors[i])
    
    # Marca la vuelta más rápida
    plt.scatter(fastest_lap['LapNumber'], fastest_lap['LapTime'].dt.total_seconds(),
                color='red', label=f'{name} - Vuelta más rápida')

    # Marca pit stops
    plt.scatter(pit_laps['LapNumber'], pit_laps['LapTime'].dt.total_seconds(),
                color='purple', marker='x', label=f'{name} - Pit stop')
    
# Configuración de la gráfica
plt.xlabel("Número de vuelta")
plt.ylabel("Tiempo de vuelta (segundos)")
plt.title("Comparación de tiempos de vuelta en Monza 2024")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()