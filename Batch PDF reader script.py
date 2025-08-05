import os
import fitz

# Bucle principal continuo
while True:
    # Directorio de entrada
    while True:
        ruta_dir = input("Enter directory: ").strip('"\'')
    
        if os.path.exists(ruta_dir):
            break
    
        print("Wrong directory\n")
    
    print("\n------------------------------------")
    
    # Función para recorrer directorios de forma recursiva
    def procesar_directorio(ruta_dir):
        # Recorre todos los archivos y carpetas en la ruta actual
        for nombre_elemento in os.listdir(ruta_dir):
            # Construye la ruta completa del elemento
            ruta_completa = os.path.join(ruta_dir, nombre_elemento)
            
            # Si es un directorio, procesarlo recursivamente
            if os.path.isdir(ruta_completa):
                procesar_directorio(ruta_completa)
            # Si es un archivo PDF, procesarlo
            elif os.path.isfile(ruta_completa) and nombre_elemento.lower().endswith('.pdf'):
                try:
                    # Abre el archivo PDF
                    documento_pdf = fitz.open(ruta_completa)
                    texto_pdf = ""
                    
                    # Extrae texto de cada página del PDF
                    for pagina in documento_pdf:
                        texto_pdf += pagina.get_text()
                    
                    # Cierra el documento PDF
                    documento_pdf.close()
                    
                    # Si se extrajo texto, muestra el nombre y contenido del archivo
                    if texto_pdf.strip('"\''):
                        print(f"{nombre_elemento}\n")
                        print(texto_pdf)
                        print("------------------------------------\n")
                except (fitz.FileDataError, PermissionError, IOError) as error_pdf:
                    # Si ocurre un error, continúa con el siguiente archivo
                    continue
    
    # Inicia el procesamiento desde el directorio raíz
    procesar_directorio(ruta_dir)
