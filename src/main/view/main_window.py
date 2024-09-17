import tkinter as tk

from tkinter import ttk
from tkinter import filedialog

from src.main.app.youtube_downloader import youtube_downloader

# Main Window

class main_window(tk.Tk) :
    def __init__(self):
        super().__init__()
        self.title("Youtube Downloader")
        self.iconbitmap("res/icons/youtube.ico")
        self.geometry("550x300")  # Window size can be adjusted as needed
        self.resizable(False, False)

        # Url de Youtube
        self.url_label = tk.Label(self, text="Url de Youtube")
        self.url_label.grid(row=0, column=0, columnspan=2, padx=(100, 50), pady=(20, 0), sticky="w")

        self.url_entry = tk.Entry(self, width=40)
        self.url_entry.grid(row=1, column=0, columnspan=2, padx=(100, 50), pady=(0, 10), sticky="w")

        # Destino de guardado
        self.destination_label = tk.Label(self, text="Destino")
        self.destination_label.grid(row=2, column=0, columnspan=2, padx=(100, 50), pady=(10, 0), sticky="w")

        self.destination_entry = tk.Entry(self, width=40)
        self.destination_entry.grid(row=3, column=0, columnspan=2, padx=(100, 50), pady=(0, 10), sticky="w")

        self.browse_button = tk.Button(self, text="Examinar", command=self.browse_folder)
        self.browse_button.grid(row=3, column=1, columnspan=2, padx=(165, 50), pady=(0, 10), sticky="w")

        # ComboBox para seleccionar la resolución:
        self.resolution_label = tk.Label(self, text="Resolución:")
        self.resolution_label.grid(row=4, column=0, columnspan=2, padx=(100, 50), pady=(10, 0), sticky="w")
        
        self.resolution_combo = ttk.Combobox(self, width=47, state="readonly")
        self.resolution_combo.grid(row=5, column=0, columnspan=2, padx=(100, 50), pady=(0, 10), sticky="w")

        # Botón para cargar las resoluciones disponibles
        self.load_button = tk.Button(self, text="Cargar", command=self.update_resolutions)
        self.load_button.grid(row=5, column=1, columnspan=2, padx=(180, 50), pady=(0, 10), sticky="w")

        # Botones de descarga:
        self.download_audio_button = tk.Button(self, text="Descargar Audio", command=self.download_audio)
        self.download_audio_button.grid(row=6, column=0, padx=(100, 50), pady=(20, 10), sticky="w")

        self.download_video_button = tk.Button(self, text="Descargar Video", command=self.download_video)
        self.download_video_button.grid(row=6, column=1, padx=(50, 100), pady=(20, 10), sticky="w")


    def browse_folder(self):
        # Open a dialog to select a folder and update the destination entry with the selected path
        folder_selected = filedialog.askdirectory()
        self.destination_entry.delete(0, tk.END)
        self.destination_entry.insert(0, folder_selected)

    def download_audio(self):
        # Placeholder function for the audio download logic
        print("Audio download logic goes here.")
        youtube_downloader.audio(self.url_entry.get(), self.destination_entry.get())


    def download_video(self):
        # Placeholder function for the video download logic
        print("Video download logic goes here.")
        youtube_downloader.video(self.url_entry.get(), self.destination_entry.get(), self.resolution_combo.get())

    def update_resolutions(self):
        print("Carga de resoluciones para la url: " + self.url_entry.get())
        youtube_downloader.resolutions(self.url_entry.get(), self.resolution_combo)
       

