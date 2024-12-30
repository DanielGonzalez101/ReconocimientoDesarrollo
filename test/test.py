import ffmpeg

def convert_asf_to_mp4(input_path, output_path):
    try:
        # Convert ASF to MP4
        ffmpeg.input(input_path).output(output_path).run()
        print(f"Conversión completada: {output_path}")
    except ffmpeg.Error as e:
        print("Error durante la conversión:", e.stderr.decode())

# Ruta del archivo ASF de entrada
asf_file = "C:\Users\lozan\OneDrive\Escritorio\ASF"

# Ruta del archivo MP4 de salida
mp4_file = "C:\Users\lozan\OneDrive\Escritorio\Mp4"

convert_asf_to_mp4(asf_file, mp4_file)