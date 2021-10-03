import os
import shutil

tipos = ['.jpg', '.jpeg', '.mxf', '.mp4', '.mp3']  # Tipos de arquivos procurados
pastas = ['Downloads', 'Documents', 'Music', 'Videos', 'Desktop']  # Diretorios escavados

"""Essa função realiza uma limpeza geral"""
def realizar_limpeza():

    #Renomea a pasta de link do Avid
    shutil.rmtree(f'C:\\Users\\Public\\Documents\\Avid Media Composer\\AMA Management', ignore_errors=True,
                      onerror=None)  # Apaga a pasta de AMA

    #Apaga os arquivos .mdb .pmr
    try:
        diretorios = os.listdir('V:\\Avid MediaFiles\\MXF\\')
        for indice in diretorios:
            try:
                os.remove(f'V:\\Avid MediaFiles\\MXF\\{indice}\\msmFMID.pmr')
                os.remove(f'V:\\Avid MediaFiles\\MXF\\{indice}\\msmMMOB.mdb')
            except:
                pass
    except:
        pass
    #Apaga as Temp's e os arquivos '.jpg', '.jpeg', '.mxf', '.mp4' das pastas 'Downloads', 'Documents', 'Music', 'Videos', 'Desktop'
    usuarios = os.listdir('C:/Users')
    for usua in usuarios:
        shutil.rmtree(f'C:\\Users\\{usua}\\AppData\\Local\\Temp', ignore_errors=True, onerror=None)  # Apaga todas as pastas 'Temps de cada usuario'
        for pasta in pastas:
            try:
                for arquivos in os.listdir(f'C:\\Users\\{usua}\\{pasta}\\'):
                    for tipo in tipos:
                        if tipo in arquivos.lower():
                            os.remove(f'C:\\Users\\{usua}\\{pasta}\\{arquivos}')
            except:
                pass

