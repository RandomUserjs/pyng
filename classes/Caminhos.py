import os 
import sys

class Caminho():
    def obter_caminho(self, caminho_relativo):
        self.caminho_relativo = caminho_relativo
        """Obtém o caminho absoluto para recursos, compatível com PyInstaller."""
        try:
            # Caminho gerado pelo PyInstaller em tempo de execução
            caminho_base = sys._MEIPASS # type: ignore
        except AttributeError:
            # Caminho padrão (desenvolvimento)
            caminho_base = os.path.abspath(".")
        # É importante usar os.path.join para construir o caminho
        return os.path.join(caminho_base, caminho_relativo)
    
    def obter_caminho_data(self):
        # Lógica para determinar o caminho do diretório de dados da aplicação
        if os.name == 'nt':
            appdata = os.getenv('APPDATA')
            caminho_base = os.path.join(appdata, 'Pyng') if appdata else os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Pyng')
        else:
            xdg = os.getenv('XDG_CONFIG_HOME')
            caminho_base = os.path.join(xdg, 'Pyng') if xdg else os.path.join(os.path.expanduser('~'), '.local', 'share', 'Pyng')
        
        # Cria o diretório de dados se ele não existir
        os.makedirs(caminho_base, exist_ok=True)
        
        return caminho_base
    
    def obter_caminho_config(self):
        # Lógica para determinar o caminho do DIRETÓRIO BASE da configuração (ex: .../Pyng)
        if os.name == 'nt':
            appdata_local = os.getenv('LOCALAPPDATA')
            if not appdata_local:
                appdata_local = os.path.join(os.path.expanduser('~'), 'AppData', 'Local')
            
            caminho_config_dir = os.path.join(appdata_local, 'Pyng')

        else:
            xdg = os.getenv('XDG_CONFIG_HOME')
            caminho_config_dir = os.path.join(xdg, 'Pyng') if xdg else os.path.join(os.path.expanduser('~'), '.config', 'Pyng')

        # Cria o DIRETÓRIO BASE da configuração (se não existir)
        os.makedirs(caminho_config_dir, exist_ok=True)

        # Retorna o caminho completo, incluindo o nome do arquivo "configs"
        caminho_completo_arquivo = os.path.join(caminho_config_dir, 'configs')
        
        return caminho_completo_arquivo