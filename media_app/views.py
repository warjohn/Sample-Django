import os
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .models import Video, Image
from .serializers import VideoSerializer, ImageSerializer
from PIL import Image as PILImage  # Для обработки изображений

class UploadVideo(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        video_file = request.FILES.get('video')
        if not video_file:
            return Response({'error': 'No video file provided'}, status=400)

        # Сохраняем видео на сервере
        video_instance = Video.objects.create(file=video_file)

        # Обработка видео (например, уменьшение размера)
        # ...

        # Сохраняем путь к обработанному видео
        video_instance.processed_file = f'processed_videos/processed_{video_file.name}'
        video_instance.save()

        # Возвращаем данные
        serializer = VideoSerializer(video_instance)
        return Response(serializer.data, status=201)


class UploadImage(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get('image')
        if not image_file:
            return Response({'error': 'No image file provided'}, status=400)

        # Сохраняем изображение на сервере
        image_instance = Image.objects.create(file=image_file)

        # Обработка изображения (например, конвертация в чёрно-белое)
        # ....

        # Сохраняем путь к обработанному изображению
        image_instance.processed_file = f'processed_images/processed_{image_file.name}'
        image_instance.save()

        # Возвращаем данные
        serializer = ImageSerializer(image_instance)
        return Response(serializer.data, status=201)