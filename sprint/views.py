import csv
from django.http import HttpResponse
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from fyp_management.permission import IsFYPPanel, IsStudent, IsSupervisor
from core.models import User, project, supervisor, teamMember

from .models import Sprint, Ticket, TicketLog
from .serializers import sprintSerializer, ticketSerializer

# Create your views here.

class createsprintAPI(APIView):
    permission_classes = [IsAuthenticated & IsSupervisor]
    def post(self, request):
        try:
            serialize = sprintSerializer(data=request.data)
            if serialize.is_valid():
                serialize.save()
                return Response(
                {
                "status": 200,
                "message": "Success",
                "body": {},
                "exception": None
                }
            )
            else:
                return Response(
                {
                "status": 422,
                "message": serialize.errors,
                "body": {},
                "exception": "some exception"
                }
            )
        except Exception as e:
            return Response(       
                {
                "status": 404,
                "message": "some exception",
                "body": {},
                "exception": str(e) 
                }
            )

class getspecificsprintAPI(APIView):
        permission_classes = [IsAuthenticated & (IsSupervisor | IsStudent)] 
        def get(self, request):
            try:
                if request.user.role == User.SUPERVISOR:
                    sup = supervisor.objects.get(user=request.user, deleted_at=None)
                    pro = project.objects.filter(supervisor=sup, deleted_at=None)
                    sp = Sprint.objects.filter(project__in=pro, deleted_at=None)
                    serialize = sprintSerializer(sp, many=True)
                    return Response(       
                    {
                    "data": serialize.data,
                    "status": 200,
                    "message": "Success",
                    "body": {},
                    "exception": None 
                    }
                )    
                elif request.user.role == User.STUDENT:
                    tm = teamMember.objects.get(user=request.user, deleted_at=None)
                    sp = Sprint.objects.filter(project__in=[tm.project], deleted_at=None)
                    serialize = sprintSerializer(sp, many=True)
                    return Response(       
                    {
                    "data": serialize.data,
                    "status": 200,
                    "message": "Success",
                    "body": {},
                    "exception": None 
                    }
                )

            except Exception as e:
                return Response(       
                    {
                    "status": 404,
                    "message": serialize.errors,
                    "body": {},
                    "exception": str(e) 
                    }
                )


class updatesprintAPI(APIView):
    permission_classes = [IsAuthenticated & IsSupervisor]
    def patch(self, request):
        try:
            sp = Sprint.objects.get(id=request.data.get("id"), deleted_at=None)
            serialize = sprintSerializer(sp,data=request.data)
            if serialize.is_valid():
                serialize.save()
                return Response(       
                        {
                        "data": serialize.data,
                        "status": 200,
                        "message": "Success",
                        "body": {},
                        "exception": None 
                        }
                        )
            else:
                return Response(
                        {
                        "status": 422,
                        "message": serialize.errors,
                        "body": {},
                        "exception": "some exception" 
                        }
                    )
                
        except Exception as e:
            return Response(       
                    {
                    "status": 404,
                    "message": "some exception",
                    "body": {},
                    "exception": str(e) 
                    }
                )

class deletesprintAPI(APIView):
    permission_classes = [IsAuthenticated & IsSupervisor]
    def delete(self, request, pk):
        try:
            my_object = Sprint.objects.get(pk=pk, deleted_at=None)
            my_object.deleted_at = timezone.now()
            my_object.save()
        except Sprint.DoesNotExist:
            return Response(
                        {
                        "status": 404,
                        "message": "Not Found",
                        "body": {},
                        "exception": None 
                        }
                    )
        return Response(
                        {
                        "status": 200,
                        "message": "Successfuly deleted",
                        "body": {},
                        "exception": None 
                        }
                    )

class allsprintAPI(APIView):
    permission_classes = [IsAuthenticated & IsFYPPanel]
    def get(self, request):
        try:
            sp = Sprint.objects.filter(project=request.data.get("pro_id"), deleted_at=None)
            serialize = sprintSerializer(sp, many=True)
            return Response(       
                {
                "data": serialize.data,
                "status": 200,
                "message": "Success",
                "body": {},
                "exception": None 
                }
            )
        except Exception as e:
            return Response(       
                    {
                    "status": 404,
                    "message": serialize.errors,
                    "body": {},
                    "exception": str(e) 
                    }
                )
        
class createticketAPI(APIView):
    permission_classes = [IsAuthenticated & (IsStudent | IsSupervisor)]
    def post(self, request):
        try:
            serialize = ticketSerializer(data=request.data)
            if serialize.is_valid():
                serialize.save()
                return Response(
                {
                "status": 200,
                "message": "Success",
                "body": {},
                "exception": None
                }
            )
            else:
                return Response(
                {
                "status": 422,
                "message": serialize.errors,
                "body": {},
                "exception": "some exception"
                }
            )
        except Exception as e:
            return Response(       
                {
                "status": 404,
                "message": "some exception",
                "body": {},
                "exception": str(e) 
                }
            )


class allticketAPI(APIView):
    permission_classes = [IsAuthenticated & IsFYPPanel]
    def get(self, request):
        try:
            if request.GET.get("sp_id") != None:
                tickets = Ticket.objects.filter(sprint=request.GET.get("sp_id"), deleted_at=None)
                serialize = ticketSerializer(tickets, many=True)
                return Response(       
                    {
                    "data": serialize.data,
                    "status": 200,
                    "message": "Success",
                    "body": {},
                    "exception": None 
                    }
                )
            else:
                sp = Sprint.objects.filter(project=project.objects.get(id = request.GET.get("pro_id")), deleted_at=None)
                tc = Ticket.objects.filter(sprint__in=sp, deleted_at=None)
                serialize = ticketSerializer(tc, many=True)
                data = serialize.data
                response = {"todo": [], "inprogress": [], "review":[], "completed":[]}
                for item in data:
                    ticket = {"ticket_id":item["id"],"ticket_name": item["title"], "start_date": item["start_date"], "end_date": item["end_date"], "creator": item["creator"], "assignee": item["assignee"], "sprint": item["sprint"], "description": item["description"], "status": item["status"], 'assignee_name':item['assignee_name'], 'creator_name':item['creator_name']}
                    if item["status"] == "todo":
                        response["todo"].append(ticket)
                    elif item["status"] == "inprogress":
                        response["inprogress"].append(ticket)
                    elif item["status"] == "review":
                        response["review"].append(ticket)
                    elif item["status"] == "completed":
                        response["completed"].append(ticket)
                return Response(       
                    {
                    "data": response,#serialize.data
                    "status": 200,
                    "message": "Success",
                    "body": {},
                    "exception": None 
                    }
                )
        except Exception as e:
            return Response(       
                    {
                    "status": 404,
                    "message": "some exception",
                    "body": {},
                    "exception": str(e) 
                    }
                )

class deleteticketAPI(APIView):
    permission_classes = [IsAuthenticated & (IsSupervisor | IsStudent)]
    def delete(self, request, pk):
        try:
            tc = Ticket.objects.get(id=pk, deleted_at=None)
            if request.user == tc.creator:
                tc.deleted_at = timezone.now()
                tc.save()
            else:
                return Response(
                        {
                        "status": 400,
                        "message": "You are not allowed to delete this ticket",
                        "body": {},
                        "exception": None 
                        }
                    )
        except Ticket.DoesNotExist:
            return Response(
                        {
                        "status": 404,
                        "message": "Not Found",
                        "body": {},
                        "exception": None 
                        }
                    )
        return Response(
                        {
                        "status": 200,
                        "message": "Successfuly deleted",
                        "body": {},
                        "exception": None 
                        }
                    )                    

class updateticketAPI(APIView):
    permission_classes = [IsAuthenticated & (IsSupervisor | IsStudent)]
    def patch(self, request):
        try:
            tc = Ticket.objects.get(id=request.data.get("id"), deleted_at=None)
            serialize = ticketSerializer(tc,data=request.data)
            if serialize.is_valid():
                serialize.save()
                return Response(       
                    {
                    "data": serialize.data,
                    "status": 200,
                    "message": "Success",
                    "body": {},
                    "exception": None 
                    }
                )
            else:
                return Response(
                    {
                    "status": 422,
                    "message": serialize.errors,
                    "body": {},
                    "exception": "some exception" 
                    }
                )
                
        except Exception as e:
            return Response(       
                    {
                    "status": 404,
                    "message": "Not Found",
                    "body": {},
                    "exception": str(e) 
                    }
                )

class getspecificticketAPI(APIView):
    permission_classes = [IsAuthenticated & (IsSupervisor | IsStudent)]
    def get(self, request):
        try:
            if request.user.role == User.SUPERVISOR:
                sup = supervisor.objects.get(user=request.user, deleted_at=None)
                pro = project.objects.filter(supervisor=sup, deleted_at=None)
                sp = Sprint.objects.filter(project__in=pro, deleted_at=None)
                tc = Ticket.objects.filter(sprint__in=sp, deleted_at=None)
                serialize = ticketSerializer(tc, many=True)
                return Response(       
                    {
                    "data": serialize.data,
                    "status": 200,
                    "message": "Success",
                    "body": {},
                    "exception": None 
                    }
                )    
            elif request.user.role == User.STUDENT:
                tm = teamMember.objects.get(user=request.user, deleted_at=None)
                sp = Sprint.objects.filter(project__in=[tm.project], deleted_at=None)
                tc = Ticket.objects.filter(sprint__in=sp, deleted_at=None)
                serialize = ticketSerializer(tc, many=True)
                return Response(       
                    {
                    "data": serialize.data,
                    "status": 200,
                    "message": "Success",
                    "body": {},
                    "exception": None 
                    }
                )

        except Exception as e:
            return Response(       
                {
                "status": 404,
                "message": serialize.errors,
                "body": {},
                "exception": str(e) 
                }
            )

class ticketlogAPI(APIView):
    def get(self, request):
        try:
            pro = project.objects.get(id=request.GET.get('id'))
            sp = Sprint.objects.filter(project=pro, deleted_at=None)
            ticket = Ticket.objects.filter(sprint=sp, deleted_at=None)
            ticket_log = TicketLog.objects.filter(ticket=ticket,deleted_at=None)
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="ticket_log.csv"'

            # Write data to the CSV file
            writer = csv.writer(response)
            writer.writerow(['id','Ticket', 'To Status', 'From Status', 'Mover'])  # Write header row
            id = 0
            for log in ticket_log:
                id += 1 
                writer.writerow([id, log.ticket.title, log.to_status, log.from_status, log.mover])  # Write data rows

            return response        
        except Exception as e:
            return Response(       
                {
                "status": 404,
                "message": "some errors",
                "body": {},
                "exception": str(e) 
                }
            )