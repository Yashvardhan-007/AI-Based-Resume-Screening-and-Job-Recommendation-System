from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Resume, Job
from .serializers import ResumeSerializer, JobSerializer
from .nlp import match

@api_view(['POST'])
def add_resume(request):
    ser = ResumeSerializer(data=request.data)
    ser.is_valid(raise_exception=True)
    ser.save()
    return Response(ser.data)

@api_view(['POST'])
def add_job(request):
    ser = JobSerializer(data=request.data)
    ser.is_valid(raise_exception=True)
    ser.save()
    return Response(ser.data)

@api_view(['GET'])
def match_view(request, rid, jid):
    r = Resume.objects.get(id=rid)
    j = Job.objects.get(id=jid)
    score = match(r.text, j.description)
    return Response({"match_percentage": score})
