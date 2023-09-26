from celery import shared_task
from file_api.uploadfile_api_.models import File

@shared_task
def process_file(file_id):
  file = File.objects.get(id=file_id)
  file.processed = True
  file.save()
