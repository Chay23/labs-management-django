from wsgiref.util import FileWrapper

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Submission
from .serializers import SubmissionSerializer, SubmissionSerializerUpdate


class SubmissionsByAssignmentList(APIView):
    def get(self, request, *args, **kwargs):
        assignment_id = kwargs.get("id", "")
        submissions = Submission.objects.filter(assignment=assignment_id)
        serializer = SubmissionSerializer(submissions, many=True)
        return Response(serializer.data)


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
        submission = Submission.objects.get(id=assignment_id)
        serializer = SubmissionSerializerUpdate(submission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileDownloadAPIView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        filename = kwargs.get("filename", "")
        queryset = get_object_or_404(Submission, attached_file__contains=filename)
        document = queryset.attached_file.open()
        response = HttpResponse(
            FileWrapper(document), content_type="application/msword"
        )
        response["Content-Disposition"] = f"attachment; filename={filename}"
        return response


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
