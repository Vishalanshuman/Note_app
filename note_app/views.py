from rest_framework.decorators import APIView
from .models import Note
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import NoteSerializer
from rest_framework import status

class NoteView(APIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    def get(self,request:Request, *args,**kwargs):
        notes =Note.objects.filter(owner = request.user)
        serializer = self.serializer_class(notes, many=True)

        if serializer:
            response={
            "message":str(request.user)+" notes",
            "data": serializer.data
            }
            return Response(data= response, status= status.HTTP_200_OK)
        return Response(data={"message":"No notes Found"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request:Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(owner=request.user)
            response = {
                "message":"Note saved Successfully.",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data= serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        

class NoteDeletePutGetView(APIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request:Request, id):
        
        note  = Note.objects.get(id = id)
        if note.owner==request.user:
            serializer = self.serializer_class(note, many=False)
  
            return Response(data=serializer.data , status=status.HTTP_200_OK)
        return Response(data={"message":"You are not owner of this note"}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request:Request, id):
        
        note  = Note.objects.get(id = id)
        if note.owner==request.user:
            serializer = self.serializer_class(note,data=request.data)
            if serializer.is_valid:
                serializer.save(owner = request.user)
                response = {
                        "message":"Note update successfully.",
                        "data":serializer.data
                    }
            return Response(data=response , status=status.HTTP_200_OK)
        return Response(data={"message":"You are not owner of this note"}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request:Request, id):
        note  = Note.objects.get(id = id)
        if note.owner==request.user:
            note.delete()
            response = {
                    "message":"note delete successfully.",
                }
            return Response(data=response , status=status.HTTP_200_OK)
        return Response(data={"message":"You are not owner of this note"}, status=status.HTTP_400_BAD_REQUEST)
    