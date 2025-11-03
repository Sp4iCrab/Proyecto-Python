import requests
import os

results = []
dominio = input("Ingrese el dominio objetivo (ejemplo: target.com): ").strip()

def subdomains():
    subdominios = []
    
    while True:
        lista = input("Ingrese la ruta del archivo de subdominios o el nombre de la lista si se encuentra en el mismo directorio que el codigo: ").strip()
        
        # Expandir la ruta para manejar ~ y rutas relativas
        lista = os.path.expanduser(lista)
        lista = os.path.abspath(lista)
        
        print(f"Buscando archivo en: {lista}")
        
        if not os.path.exists(lista):
            print(f"Error: No se encontró el archivo '{lista}'")
            print("Asegúrate de que la ruta sea correcta")
            continue
            
        if not os.path.isfile(lista):
            print(f"Error: '{lista}' no es un archivo válido")
            continue
            
        try:
            with open(lista, 'r', encoding='utf-8') as file:
                for line in file:
                    words = line.strip().split()
                    subdominios.extend(words)
                
            if not subdominios:
                print("El archivo está vacío o no contiene subdominios válidos")
                continue
                
            print(f"Se cargaron {len(subdominios)} subdominios")
            return subdominios
            
        except FileNotFoundError:
            print(f"Error: Archivo no encontrado - {lista}")
        except PermissionError:
            print(f"Error: Sin permisos para leer el archivo - {lista}")
        except UnicodeDecodeError:
            print(f"Error: Problema de codificación. Intenta guardar el archivo como UTF-8")
        except Exception as e:
            print(f"Error inesperado: {e}")


print("Protocolo a utilizar, HTTPS o HTTP:")
protocolo = input().lower().strip()

while protocolo not in ['https', 'http']:
    print("Protocolo no válido. Ingresa 'HTTPS' o 'HTTP':")
    protocolo = input().lower().strip()

print(f"\nIniciando búsqueda con protocolo {protocolo.upper()}...")

subdominios_lista = subdomains()

if subdominios_lista:
    for sub in subdominios_lista:
        if protocolo == "https":
            url = f'https://{sub}.{dominio}'
        else:
            url = f'http://{sub}.{dominio}'
            
        try:
            response = requests.get(url, timeout=3)
            if response.status_code in [200, 301, 302, 401, 403, 405]:
                print(f'[-]Subdominio válido encontrado: {url} - Status: {response.status_code}')
                results.append(url)

        except requests.RequestException:
            continue

    # Mostrar resultados finales
    print(f"\nESCANEO COMPLETADO")
    print(f"Total de subdominios encontrados: {len(results)}")
    print("=" * 50)
    
    if results:
        for r in results:
            print(r)
    else:
        print("No se encontraron subdominios activos")
else:
    print("No se pudieron cargar subdominios. Saliendo...")