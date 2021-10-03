## superclear

### Proposta

O programa foi escrito em python e seu objetivo é realizar uma limpeza nas pastas: 
> 'Downloads', 
> 'Documents', 
> 'Music', 
> 'Videos' e 'Desktop'

de cada usuário. Os arquivos procurados são:

> '.jpg', 
> '.jpeg', 
> '.mxf', 
> '.mp4', 
> '.mp3'

a aplicação também apaga a pasta de link do Avid para melhorar o desempenho da edição.

* shutil.rmtree(f'C:\\Users\\Public\\Documents\\Avid Media Composer\\AMA Management', ignore_errors=True, onerror=None)

por ultimo apaga os metadados forçando o Avid realizar uma nova varredura na pasta 'MXF':

* os.remove(f'V:\\Avid MediaFiles\\MXF\\{indice}\\msmFMID.pmr')
* os.remove(f'V:\\Avid MediaFiles\\MXF\\{indice}\\msmMMOB.mdb')

