import random
import itertools

def generar_combinaciones(palabras):
    combinaciones = []
    
    # Combinaciones básicas
    for i in range(1, len(palabras) + 1):
        for combo in itertools.permutations(palabras, i):
            combinaciones.append(''.join(combo))
            combinaciones.append('_'.join(combo))
            combinaciones.append('-'.join(combo))
            combinaciones.append('.'.join(combo))
    
    return combinaciones

def generar_variaciones_numericas(base, fecha):
    #Genera variaciones numéricas basadas en la fechas
    variaciones = []
    dia, mes, año = fecha.split('/')
    año_completa = año
    año_corta = año[2:]
    
    # Combinaciones de números comunes
    numeros_comunes = ['123', '1234', '12345', '123456', '111', '222', '333', '777', '000', '007', '69', '420']
    
    # Añadir números basados en la fecha
    numeros_fecha = [dia, mes, año_completa, año_corta, 
                    dia + mes, mes + año_corta, dia + año_corta,
                    año_corta + dia, año_corta + mes]
    
    todos_numeros = numeros_comunes + numeros_fecha
    
    for num in todos_numeros:
        variaciones.append(base + num)
        variaciones.append(num + base)
        variaciones.append(base.capitalize() + num)
        variaciones.append(base.upper() + num)
    
    return variaciones

def main():
    print("=== Generador de Contraseñas para Ethical Hacking ===\n")
    
    # Capturar información básica
    name = input("Ingrese el nombre del objetivo: ").strip()
    surname = input("Ingrese el apellido del objetivo: ").strip()
    birthday = input("Ingrese la fecha de nacimiento del objetivo (DD/MM/YYYY): ").strip()

    palabras_base = [name.lower(), surname.lower(),
                    name.lower()[:3], surname.lower()[:3],
                    name.lower()[:1] + surname.lower()]
    
    contraseñas = set()
    
    # Generar combinaciones básicas
    combinaciones_basicas = generar_combinaciones(palabras_base)
    contraseñas.update(combinaciones_basicas)
    
    # Generar variaciones con números
    for base in [name.lower(), surname.lower()]:
        variaciones = generar_variaciones_numericas(base, birthday)
        contraseñas.update(variaciones)
    
    # Información adicional
    bonus = input("¿Desea agregar información adicional? (y/n): ").strip().lower()
    
    if bonus == 'y':
        bonus_palabras = []

        pet_name = input("Ingrese el nombre de la mascota o los nombres de las mascotas separados por ',': ").strip()
        if pet_name:
            #Dividir los nombres con ',' en caso de diferentes nombres de mascotas
            bonus_palabras.extend([p.strip().lower() for p in pet_name.split(',')])
        
        fav_color = input("Ingrese el color favorito: ").strip().lower()
        if fav_color:
            bonus_palabras.append(fav_color)
        
        fav_band = input("Ingrese la banda favorita: ").strip().lower()
        if fav_band:
            bonus_palabras.append(fav_band)
            # Añadir variaciones de bandas (sin espacios)
            bonus_palabras.append(fav_band.replace(' ', ''))

        fav_series = input("Ingrese la serie favorita: ").strip().lower()
        if fav_series:
            bonus_palabras.append(fav_series)
            bonus_palabras.append(fav_series.replace(' ', ''))

        fav_movie = input("Ingrese la película favorita: ").strip().lower()
        if fav_movie:
            bonus_palabras.append(fav_movie)
            bonus_palabras.append(fav_movie.replace(' ', ''))

        couple = input("Ingrese el nombre de la pareja (si aplica): ").strip().lower()
        if couple:
            bonus_palabras.append(couple)

        bonus_date = input("Ingrese otra fecha importante para el objetivo (DD/MM/YYYY): ").strip()
        if bonus_date:
            dia_b, mes_b, año_b = bonus_date.split('/')
            bonus_palabras.extend([dia_b, mes_b, año_b, año_b[2:]])
        
        # Combinar palabras base con bonus
        todas_palabras = palabras_base + bonus_palabras
        combinaciones_completas = generar_combinaciones(todas_palabras)
        contraseñas.update(combinaciones_completas)
        
        # Variaciones con información bonus
        for palabra in bonus_palabras:
            if len(palabra) > 2:  # Solo palabras significativas
                variaciones_bonus = generar_variaciones_numericas(palabra, birthday)
                contraseñas.update(variaciones_bonus)
    
    # Filtrar contraseñas muy cortas
    contraseñas_filtradas = [pwd for pwd in contraseñas if len(pwd) >= 4 and len(pwd) <= 20]
    
    # Mostrar resultados
    print(f"\n=== {len(contraseñas_filtradas)} Contraseñas Generadas ===")
    for i, pwd in enumerate(contraseñas_filtradas[:50], 1):  # Solo muestra las primeras 50
        print(f"{i:2d}. {pwd}")
    
    if len(contraseñas_filtradas) > 50:
        print(f"... y {len(contraseñas_filtradas) - 50} más")
    
    # Guardar en archivo
    guardar = input("\n¿Desea guardar en un archivo? (y/n): ").strip().lower()
    if guardar == 'y':
        filename = input("Ingrese el nombre del archivo (por defecto: passwords.txt): ").strip()
        if not filename:
            filename = "passwords.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            for pwd in contraseñas_filtradas:
                f.write(pwd + '\n')
        print(f"Contraseñas guardadas en {filename}")

if __name__ == "__main__":
    main()