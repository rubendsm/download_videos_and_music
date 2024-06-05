import sys
from cx_Freeze import setup, Executable

# Lista de pacotes a serem incluídos
packages = ['asyncio', 'yt_dlp']

# Lista de módulos adicionais a serem incluídos
additional_mods = ['tkinter', 'tkinter.ttk', 'tkinter.filedialog', 'tkinter.messagebox']

# Dependências excluídas, se houver
excludes = []

# Opções para a construção do executável
build_exe_options = {
    'packages': packages,
    'includes': additional_mods,
    'excludes': excludes,
    'include_files': ['download_videos.py']  # Se houver outros arquivos a serem incluídos
}

# Define o executável a ser construído
exe = Executable(
    script="main.py",  # Nome do script principal
    base=None,
    icon="icone.ico"  # Se desejar incluir um ícone para o executável
)

# Configuração do setup
setup(
    name="Download music and video from youtube/facebook",
    version="1.0",
    description="Download music and video from youtube/facebook",
    options={"build_exe": build_exe_options},
    executables=[exe]
)
