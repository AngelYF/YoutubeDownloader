from pytube import YouTube

# Youtube downloader

class youtube_downloader() :

    @staticmethod
    def video(url, destino, selected_resolution):
        """Descarga un video de YouTube en la ruta especificada."""
        try:
            yt = YouTube(url)
            video = yt.streams.filter(res=selected_resolution, progressive=True, file_extension='mp4').first()

            if video:
                video.download(destino)
                print(f"El vídeo ha sido descargado en: {destino}")
            else:
                print("No se encontró un vídeo compatible.")
        except Exception as e:
            print(f"Ha ocurrido un error al descargar el vídeo: {e}")

    @staticmethod
    def audio(url, destino):
        """Descarga el audio de un video de YouTube en la ruta especificada."""
        try:
            yt = YouTube(url)
            audio = yt.streams.filter(only_audio=True).first()
            if audio:
                audio.download(destino)
                print(f"El audio ha sido descargado en: {destino}")
            else:
                print("No se encontró un audio compatible.")
        except Exception as e:
            print(f"Ha ocurrido un error al descargar el audio: {e}")

    @staticmethod
    def resolutions(url, combo):
        """Comprobación de resoluciones disponibles para la url dada"""
        if url != "":
            try:
                yt = YouTube(url)
                # Obtiene las resoluciones únicas disponibles para el video
                resolutions = list({stream.resolution for stream in yt.streams.filter(progressive=True)})
                # Actualiza las opciones del ComboBox
                combo['values'] = resolutions
                if resolutions:
                    combo.current(0)  # Establece por defecto la primera resolución disponible
            except Exception as e:
                print(f"Ha ocurrido un error al descargar el audio: {e}")
            