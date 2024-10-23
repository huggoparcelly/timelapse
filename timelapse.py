import cv2

def create_timelapse(input_video: str, output_video: str, frame_skip: int):
    # Carregar o vídeo de entrada
    cap = cv2.VideoCapture(input_video)
    
    # Obter as propriedades do vídeo original
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Criar o vídeo de saída
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Adicionar apenas um frame a cada 'frame_skip'
        if frame_count % frame_skip == 0:
            out.write(frame)
        
        frame_count += 1

    # Liberar o vídeo de entrada e saída
    cap.release()
    out.release()
    print(f"Timelapse criado com sucesso: {output_video}")

# Configurações
input_video_path = '2024-10-16 07-33-22.mkv'  # Substitua pelo caminho do seu vídeo
output_video_path = '2024-10-16 07-33-22-timelapse_video.avi'  # Saída desejada
frame_skip_value = 30  # A cada quantos frames o timelapse deve pular (ajustar conforme necessário)

create_timelapse(input_video_path, output_video_path, frame_skip_value)
