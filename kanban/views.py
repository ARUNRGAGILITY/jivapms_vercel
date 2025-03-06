from django.shortcuts import render
from django.http import HttpResponse
from kanban.models import *
import json
app_name = "kanban"
mod_name = ""
def kanban_home(request):
    message = "test"
    context = {
        'page': 'kanban_home',
        'page_title': 'Kanban Home Page'
    }
    template_file_url = f"{app_name}/kanban_home/kanban_home.html"
    return render(request, template_file_url, context)


# def cfd_chart_view(request):
#     """Fetch CFD data and pass it in the required format for Chart.js"""
#     template_file_url = f"{app_name}/kanban_home/cfd_chart.html"
#     project = Project.objects.first()
#     board = Board.objects.filter(project=project).first()

#     if not project or not board:
#         return render(request, template_file_url, {"error": "No project or board found."})

#     # Get CFD data sorted by timestamp
#     cfd_entries = CFD.objects.filter(project=project, board=board).order_by("data_timestamp")

#     if not cfd_entries.exists():
#         return render(request, template_file_url, {"error": "No CFD data available."})

#     # Prepare data in the required format
#     cfd_data = []
#     for entry in cfd_entries:
#         column_counts = json.loads(entry.column_card_counts)
#         cfd_data.append({
#             "date": entry.data_timestamp.strftime("%b %d"),
#             "to_do_data": column_counts.get("To Do", 0),
#             "wip_data": column_counts.get("WIP", 0),
#             "deploy_data": column_counts.get("Deploy", 0),
#             "done_data": column_counts.get("Done", 0),

#         })
#     normal_cfd_data = []
#     for entry in cfd_entries:
#         column_counts = json.loads(entry.column_card_counts)
#         normal_cfd_data.append({
#             "date": entry.data_timestamp.strftime("%b %d"),
#             "to_do_data": column_counts.get("To Do", 0),
#             "wip_data": column_counts.get("WIP", 0),
#             "deploy_data": column_counts.get("Deploy", 0),
#             "done_data": column_counts.get("Done", 0),
#         })
#     context = {"cfd_data": json.dumps(cfd_data), "normal_cfd_data": normal_cfd_data}
#     return render(request, template_file_url, context)

from django.shortcuts import render
import json

def cfd_chart_view(request):
    chart_data = {
        "chartData": {
            "labels": [
                "2025-03-01 10 AM", "2025-03-01 1 PM", "2025-03-01 4 PM",
                "2025-03-02 10 AM", "2025-03-02 1 PM", "2025-03-02 4 PM",
                "2025-03-03 10 AM", "2025-03-03 1 PM", "2025-03-03 4 PM",
                "2025-03-04 10 AM", "2025-03-04 1 PM", "2025-03-04 4 PM",
                "2025-03-05 10 AM", "2025-03-05 1 PM", "2025-03-05 4 PM",
                "2025-03-06 10 AM", "2025-03-06 1 PM", "2025-03-06 4 PM",
                "2025-03-07 10 AM", "2025-03-07 1 PM", "2025-03-07 4 PM",
                "2025-03-08 10 AM", "2025-03-08 1 PM", "2025-03-08 4 PM",
                "2025-03-09 10 AM", "2025-03-09 1 PM", "2025-03-09 4 PM",
                "2025-03-10 10 AM", "2025-03-10 1 PM", "2025-03-10 4 PM",
                "2025-03-11 10 AM", "2025-03-11 1 PM", "2025-03-11 4 PM",
                "2025-03-12 10 AM", "2025-03-12 1 PM", "2025-03-12 4 PM",
                "2025-03-13 10 AM", "2025-03-13 1 PM", "2025-03-13 4 PM",
                "2025-03-14 10 AM", "2025-03-14 1 PM", "2025-03-14 4 PM"
            ],
            "datasets": [
                {"label": "Backlog", "data": [5, 4, 3, 5, 3, 2, 3, 2, 2, 2, 2, 0, 2, 2, 1, 2, 0, 0, 3, 3, 1, 2, 0, 0, 3, 1, 0, 1, 1, 1, 4, 3, 1, 1, 0, 0, 3, 3, 3, 5, 3, 3]},
                {"label": "To Do", "data": [2, 1, 1, 2, 3, 2, 3, 2, 2, 3, 1, 3, 2, 0, 1, 2, 2, 0, 0, 0, 2, 2, 4, 3, 1, 2, 1, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 2, 1]},
                {"label": "WIP", "data": [0, 2, 2, 1, 2, 2, 3, 4, 2, 1, 3, 1, 1, 3, 2, 2, 3, 5, 3, 3, 2, 1, 1, 1, 3, 4, 4, 3, 1, 0, 0, 0, 1, 2, 3, 2, 1, 0, 0, 0, 0, 1]},
                {"label": "Done", "data": [0, 0, 1, 2, 2, 4, 4, 5, 7, 9, 9, 11, 12, 12, 13, 13, 14, 14, 16, 16, 17, 18, 18, 19, 19, 19, 21, 23, 25, 26, 26, 26, 26, 27, 27, 29, 30, 31, 31, 31, 31, 31]}
            ]
        }
    }
    context = {"chart_data": json.dumps(chart_data)}
    template_file_url = f"{app_name}/kanban_home/cfd_chart.html"    
    return render(request, template_file_url, context )




# template_file_url = f"{app_name}/kanban_home/cfd_chart.html"
# return render(request, template_file_url, context)
