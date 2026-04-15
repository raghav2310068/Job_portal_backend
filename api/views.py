from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from .models import Job
from .serializer import JobSerializer
from accounts.models import Users
from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class JobViewSet(ModelViewSet):
    authentication_classes = [CsrfExemptSessionAuthentication]
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_user(self):
        user_id = self.request.session.get("user_id")
        print("SESSION USER ID:", user_id)
        if not user_id:
            raise NotAuthenticated("Login required")

        return Users.objects.get(id=user_id)

    def perform_create(self, serializer):
        user = self.get_user()

        if user.role.lower() != "recruiter":
            raise PermissionDenied("Only recruiter allowed")

        serializer.save(created_by=user)

    def perform_update(self, serializer):
        user = self.get_user()
        job = self.get_object()

        if job.created_by != user:
            raise PermissionDenied("Not allowed to edit")

        serializer.save()

    def perform_destroy(self, instance):
        user = self.get_user()

        if instance.created_by != user:
            raise PermissionDenied("Not allowed to delete")

        instance.delete()
