from django.apps import AppConfig
from faster_whisper import WhisperModel


class EdtechConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'edtech'
    
    # def ready(self):
    #     # Initialize the Whisper model when the app is ready
    #     self.model = WhisperModel(
    #         "medium",
    #         device="cuda" if self.is_cuda_available() else "cpu",
    #         compute_type="float16" if self.is_cuda_available() else "int8"
    #     )
