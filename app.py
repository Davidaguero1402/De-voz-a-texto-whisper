import os
import whisper

# Rutas relativas de las carpetas
rawmp3_folder = "rawmp3"
transcriptions_folder = "transcripciones"

# Cargar el modelo de Whisper
model = whisper.load_model("medium")

# Asegurarse de que la carpeta de transcripciones existe
os.makedirs(transcriptions_folder, exist_ok=True)

# Iterar sobre los archivos en la carpeta rawmp3
for filename in os.listdir(rawmp3_folder):
    if filename.endswith(".mp3"):
        # Ruta completa del archivo mp3
        filepath = os.path.join(rawmp3_folder, filename)
        
        # Realizar la transcripción
        result = model.transcribe(filepath)
        
        # Nombre del archivo de transcripción
        transcription_filename = os.path.splitext(filename)[0] + ".txt"
        transcription_filepath = os.path.join(transcriptions_folder, transcription_filename)
        
        # Guardar la transcripción en un archivo de texto
        with open(transcription_filepath, "w", encoding="utf-8") as f:
            f.write(result["text"])

        print(f"Transcripción de {filename} guardada en {transcription_filepath}")
