# yt_fb_join_and_download
FastAPI com uma funcionalidade que permita o envio do link de vários vídeos (facebook, youtube,etc) e que faça o download desses videos e faça a junção dos mesmos num só e guarde em um local especifico no servidor. A junção dos vídeos deve ser feita pela ordem de upload dos link , numa lista de links 0 com o 1 depois com o 2 , etc.


 - pytube para baixar vídeos do YouTube.
 - yt_dlp (sucessor do youtube-dl) para baixar vídeos de outras plataformas como Facebook.
 - moviepy para unir os vídeos.

pip install fastapi uvicorn pytube yt_dlp moviepy

main.py define a rota /merge_videos/ que recebe uma lista de links e chama a função download_and_merge_videos.
download_videos.py contém as funções assíncronas para baixar vídeos e uni-los.
download_video utiliza yt_dlp para baixar o vídeo de qualquer link fornecido.
download_and_merge_videos chama download_video para cada link, junta todos os vídeos baixados usando moviepy, e salva o vídeo final no caminho especificado.