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
        # Windows: %APPDATA% (Roaming)
        if os.name == 'nt':
            appdata = os.getenv('APPDATA')
            if appdata:
                return os.path.join(appdata, 'Pyng')
            # fallback
            return os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Pyng')
        else:
            # Linux/Unix: $XDG_CONFIG_HOME or ~/.config
            xdg = os.getenv('XDG_CONFIG_HOME')
            if xdg:
                return os.path.join(xdg, 'Pyng')
            return os.path.join(os.path.expanduser('~'), '.local', 'share', 'Pyng')
    
    def obter_caminho_config(self):
        if os.name == 'nt':
            appdata = os.getenv('APPDATA')
            if appdata:
                return os.path.join(appdata, 'Pyng', 'configs')
            # fallback
            return os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Pyng', 'configs')
        else:
            xdg = os.getenv('XDG_CONFIG_HOME')
            if xdg:
                return os.path.join(xdg, 'Pyng', 'configs')
            return os.path.join(os.path.expanduser('~'), '.config', 'Pyng', 'configs')