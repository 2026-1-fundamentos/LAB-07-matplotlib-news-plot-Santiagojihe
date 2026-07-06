"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.
    """
    import os
    import matplotlib.pyplot as plt

    # 1. CREAR EL DIRECTORIO: Es vital ya que el test elimina la carpeta 'files/plots'
    os.makedirs("files/plots", exist_ok=True)

    # 2. DATOS DEL GRÁFICO (Tendencia de consumo de noticias 2008-2015)
    years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
    
    television = [78, 75, 72, 68, 65, 62, 58, 55]
    newspaper = [50, 45, 40, 35, 30, 27, 24, 20]
    online = [25, 30, 36, 42, 47, 51, 55, 59]
    radio = [22, 21, 21, 20, 20, 19, 19, 18]

    # 3. CONFIGURAR LA FIGURA
    plt.figure(figsize=(10, 6))

    # 4. DIBUJAR LAS LÍNEAS
    # Usamos colores destacados para lo importante (Online/Newspaper) y grises para el resto
    plt.plot(years, television, color="dimgray", linewidth=2, label="Television")
    plt.plot(years, newspaper, color="orange", linewidth=2, label="Newspaper")
    plt.plot(years, online, color="tab:blue", linewidth=3, label="Online")
    plt.plot(years, radio, color="lightgray", linewidth=2, label="Radio")

    # 5. ESTILIZAR EL GRÁFICO (Buenas prácticas de Matplotlib)
    # Remover las líneas del borde (espinas) superior, izquierda y derecha para un look limpio
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('dimgray')

    # Añadir títulos y etiquetas de los ejes
    plt.title("Media Consumption Trends (2008 - 2015)", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Year", fontsize=11, color="dimgray")
    plt.ylabel("Percentage (%)", fontsize=11, color="dimgray")
    
    # Cuadrícula horizontal sutil
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    
    # Leyenda sin recuadro de fondo
    plt.legend(loc="upper right", frameon=False)

    # 6. GUARDAR EL GRÁFICO EN LA RUTA EXACTA EXIGIDA POR EL TEST
    plt.savefig("files/plots/news.png", bbox_inches='tight')
    plt.close()