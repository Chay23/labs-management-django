from wsgiref.util import FileWrapper

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import FileResponse

from .models import Submission
from .serializers import SubmissionSerializer


@permission_classes([IsAuthenticated])
class SubmissionsByAssignmentList(APIView):
    def get(self, request, *args, **kwargs):
        assignment_id = kwargs.get("assignment_id", "")
        submissions = Submission.objects.filter(assignment=assignment_id)
        serializer = SubmissionSerializer(submissions, many=True)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class SubmissionByUserId(APIView):
    def get(self, request, *args, **kwargs):
        assignment_id = int(kwargs.get("assignment_id", ""))
        user_id = int(kwargs.get("user_id", ""))
        submission = Submission.objects.get(assignment=assignment_id, created_by=user_id)
        serializer = SubmissionSerializer(submission)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        assignment_id = int(kwargs.get("assignment_id", ""))
        user_id = int(kwargs.get("user_id", ""))
        submission = Submission.objects.get(id=assignment_id, created_by=user_id)
        serializer = SubmissionSerializer(submission, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
class FileDownloadAPIView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        filename = kwargs.get("filename", "")
        queryset = get_object_or_404(Submission, attached_file__contains=filename)
        print("FILENAME", filename)
        document = queryset.attached_file.open()
        response = FileResponse(document, as_attachment=True)
        return response


@permission_classes([IsAuthenticated])
class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
