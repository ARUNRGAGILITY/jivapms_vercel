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


# version1
# from django.shortcuts import render
# import json

# def cfd_chart_view(request):
#     chart_data = {
#         "chartData": {
#             "labels": [
#                 "2025-03-01 10 AM", "2025-03-01 1 PM", "2025-03-01 4 PM",
#                 "2025-03-02 10 AM", "2025-03-02 1 PM", "2025-03-02 4 PM",
#                 "2025-03-03 10 AM", "2025-03-03 1 PM", "2025-03-03 4 PM",
#                 "2025-03-04 10 AM", "2025-03-04 1 PM", "2025-03-04 4 PM",
#                 "2025-03-05 10 AM", "2025-03-05 1 PM", "2025-03-05 4 PM",
#                 "2025-03-06 10 AM", "2025-03-06 1 PM", "2025-03-06 4 PM",
#                 "2025-03-07 10 AM", "2025-03-07 1 PM", "2025-03-07 4 PM",
#                 "2025-03-08 10 AM", "2025-03-08 1 PM", "2025-03-08 4 PM",
#                 "2025-03-09 10 AM", "2025-03-09 1 PM", "2025-03-09 4 PM",
#                 "2025-03-10 10 AM", "2025-03-10 1 PM", "2025-03-10 4 PM",
#                 "2025-03-11 10 AM", "2025-03-11 1 PM", "2025-03-11 4 PM",
#                 "2025-03-12 10 AM", "2025-03-12 1 PM", "2025-03-12 4 PM",
#                 "2025-03-13 10 AM", "2025-03-13 1 PM", "2025-03-13 4 PM",
#                 "2025-03-14 10 AM", "2025-03-14 1 PM", "2025-03-14 4 PM"
#             ],
#             "datasets": [
#                 {"label": "Backlog", "data": [5, 4, 3, 5, 3, 2, 3, 2, 2, 2, 2, 0, 2, 2, 1, 2, 0, 0, 3, 3, 1, 2, 0, 0, 3, 1, 0, 1, 1, 1, 4, 3, 1, 1, 0, 0, 3, 3, 3, 5, 3, 3]},
#                 {"label": "To Do", "data": [2, 1, 1, 2, 3, 2, 3, 2, 2, 3, 1, 3, 2, 0, 1, 2, 2, 0, 0, 0, 2, 2, 4, 3, 1, 2, 1, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 2, 1]},
#                 {"label": "WIP", "data": [0, 2, 2, 1, 2, 2, 3, 4, 2, 1, 3, 1, 1, 3, 2, 2, 3, 5, 3, 3, 2, 1, 1, 1, 3, 4, 4, 3, 1, 0, 0, 0, 1, 2, 3, 2, 1, 0, 0, 0, 0, 1]},
#                 {"label": "Done", "data": [0, 0, 1, 2, 2, 4, 4, 5, 7, 9, 9, 11, 12, 12, 13, 13, 14, 14, 16, 16, 17, 18, 18, 19, 19, 19, 21, 23, 25, 26, 26, 26, 26, 27, 27, 29, 30, 31, 31, 31, 31, 31]}
#             ]
#         }
#     }
#     context = {"chart_data": json.dumps(chart_data)}
#     template_file_url = f"{app_name}/kanban_home/cfd_chart.html"    
#     return render(request, template_file_url, context )

# version2
# from django.shortcuts import render
# import json

# def cfd_chart_view(request):
   

#     # Given data for Backlog, To Do, WIP, Done
#     backlog_data = [5, 4, 3, 5, 3, 2, 3, 2, 2, 2, 2, 0, 2, 2, 1, 2, 0, 0, 3, 3, 1, 2, 0, 0, 3, 1, 0, 1, 1, 1, 4, 3, 1, 1, 0, 0, 3, 3, 3, 5, 3, 3]
#     todo_data = [2, 1, 1, 2, 3, 2, 3, 2, 2, 3, 1, 3, 2, 0, 1, 2, 2, 0, 0, 0, 2, 2, 4, 3, 1, 2, 1, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 2, 1]
#     wip_data = [0, 2, 2, 1, 2, 2, 3, 4, 2, 1, 3, 1, 1, 3, 2, 2, 3, 5, 3, 3, 2, 1, 1, 1, 3, 4, 4, 3, 1, 0, 0, 0, 1, 2, 3, 2, 1, 0, 0, 0, 0, 1]
#     done_data = [0, 0, 1, 2, 2, 4, 4, 5, 7, 9, 9, 11, 12, 12, 13, 13, 14, 14, 16, 16, 17, 18, 18, 19, 19, 19, 21, 23, 25, 26, 26, 26, 26, 27, 27, 29, 30, 31, 31, 31, 31, 31]

#     # Calculate total count at each timestamp
#     total_data = [b + t + w + d for b, t, w, d in zip(backlog_data, todo_data, wip_data, done_data)]

#     # Define labels (timestamps)
#     labels = [
#         "2025-03-01 10 AM", "2025-03-01 1 PM", "2025-03-01 4 PM",
#         "2025-03-02 10 AM", "2025-03-02 1 PM", "2025-03-02 4 PM",
#         "2025-03-03 10 AM", "2025-03-03 1 PM", "2025-03-03 4 PM",
#         "2025-03-04 10 AM", "2025-03-04 1 PM", "2025-03-04 4 PM",
#         "2025-03-05 10 AM", "2025-03-05 1 PM", "2025-03-05 4 PM",
#         "2025-03-06 10 AM", "2025-03-06 1 PM", "2025-03-06 4 PM",
#         "2025-03-07 10 AM", "2025-03-07 1 PM", "2025-03-07 4 PM",
#         "2025-03-08 10 AM", "2025-03-08 1 PM", "2025-03-08 4 PM",
#         "2025-03-09 10 AM", "2025-03-09 1 PM", "2025-03-09 4 PM",
#         "2025-03-10 10 AM", "2025-03-10 1 PM", "2025-03-10 4 PM",
#         "2025-03-11 10 AM", "2025-03-11 1 PM", "2025-03-11 4 PM",
#         "2025-03-12 10 AM", "2025-03-12 1 PM", "2025-03-12 4 PM",
#         "2025-03-13 10 AM", "2025-03-13 1 PM", "2025-03-13 4 PM",
#         "2025-03-14 10 AM", "2025-03-14 1 PM", "2025-03-14 4 PM"
#     ]

#     # Create chart data dictionary
#     chart_data = {
#         "chartData": {
#             "labels": labels,
#             "datasets": [
#                 {"label": "Backlog", "data": backlog_data},
#                 {"label": "To Do", "data": todo_data},
#                 {"label": "WIP", "data": wip_data},
#                 {"label": "Done", "data": done_data},
#                 {"label": "Total", "data": total_data}  # Add total count to the chart
#             ]
#         }
#     }

#     context = {"chart_data": json.dumps(chart_data)}
#     template_file_url = f"{app_name}/kanban_home/cfd_chart.html"    
#     return render(request, template_file_url, context)

# version3
# from django.shortcuts import render
# import json

# def cfd_chart_view(request):

#     # Given raw data (non-cumulative)
#     backlog_data = [5, 4, 3, 5, 3, 2, 3, 2, 2, 2, 2, 0, 2, 2, 1, 2, 0, 0, 3, 3, 1, 2, 0, 0, 3, 1, 0, 1, 1, 1, 4, 3, 1, 1, 0, 0, 3, 3, 3, 5, 3, 3]
#     todo_data = [2, 1, 1, 2, 3, 2, 3, 2, 2, 3, 1, 3, 2, 0, 1, 2, 2, 0, 0, 0, 2, 2, 4, 3, 1, 2, 1, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 2, 1]
#     wip_data = [0, 2, 2, 1, 2, 2, 3, 4, 2, 1, 3, 1, 1, 3, 2, 2, 3, 5, 3, 3, 2, 1, 1, 1, 3, 4, 4, 3, 1, 0, 0, 0, 1, 2, 3, 2, 1, 0, 0, 0, 0, 1]
#     done_data = [0, 0, 1, 2, 2, 4, 4, 5, 7, 9, 9, 11, 12, 12, 13, 13, 14, 14, 16, 16, 17, 18, 18, 19, 19, 19, 21, 23, 25, 26, 26, 26, 26, 27, 27, 29, 30, 31, 31, 31, 31, 31]

#     # Convert To Do and WIP to cumulative values
#     def make_cumulative(data):
#         cumulative = []
#         total = 0
#         for value in data:
#             total += value
#             cumulative.append(total)
#         return cumulative

#     todo_cumulative = make_cumulative(todo_data)
#     wip_cumulative = make_cumulative(wip_data)


#     # Calculate total count at each timestamp
#     total_data = [b + t + w + d for b, t, w, d in zip(backlog_data, todo_cumulative, wip_cumulative, done_data)]

#     # Define labels (timestamps)
#     labels = [
#         "2025-03-01 10 AM", "2025-03-01 1 PM", "2025-03-01 4 PM",
#         "2025-03-02 10 AM", "2025-03-02 1 PM", "2025-03-02 4 PM",
#         "2025-03-03 10 AM", "2025-03-03 1 PM", "2025-03-03 4 PM",
#         "2025-03-04 10 AM", "2025-03-04 1 PM", "2025-03-04 4 PM",
#         "2025-03-05 10 AM", "2025-03-05 1 PM", "2025-03-05 4 PM",
#         "2025-03-06 10 AM", "2025-03-06 1 PM", "2025-03-06 4 PM",
#         "2025-03-07 10 AM", "2025-03-07 1 PM", "2025-03-07 4 PM",
#         "2025-03-08 10 AM", "2025-03-08 1 PM", "2025-03-08 4 PM",
#         "2025-03-09 10 AM", "2025-03-09 1 PM", "2025-03-09 4 PM",
#         "2025-03-10 10 AM", "2025-03-10 1 PM", "2025-03-10 4 PM",
#         "2025-03-11 10 AM", "2025-03-11 1 PM", "2025-03-11 4 PM",
#         "2025-03-12 10 AM", "2025-03-12 1 PM", "2025-03-12 4 PM",
#         "2025-03-13 10 AM", "2025-03-13 1 PM", "2025-03-13 4 PM",
#         "2025-03-14 10 AM", "2025-03-14 1 PM", "2025-03-14 4 PM"
#     ]

#     # Create chart data dictionary
#     chart_data = {
#         "chartData": {
#             "labels": labels,
#             "datasets": [
#                 {"label": "Backlog", "data": backlog_data},
#                 {"label": "To Do", "data": todo_cumulative},  # Fixed to be cumulative
#                 {"label": "WIP", "data": wip_cumulative},  # Fixed to be cumulative
#                 {"label": "Done", "data": done_data},  # Ensured cumulative consistency
#                 {"label": "Total", "data": total_data}  # Added total count dataset
#             ]
#         }
#     }

#     context = {"chart_data": json.dumps(chart_data)}
#     template_file_url = f"{app_name}/kanban_home/cfd_chart.html"    
#     return render(request, template_file_url, context)

# version4

from django.shortcuts import render
import json

def cfd_chart_view(request):

    # Given raw data (non-cumulative)
    backlog_data = [5, 4, 3, 5, 3, 2, 3, 2, 2, 2, 2, 0, 2, 2, 1, 2, 0, 0, 3, 3, 1, 2, 0, 0, 3, 1, 0, 1, 1, 1, 4, 3, 1, 1, 0, 0, 3, 3, 3, 5, 3, 3]
    todo_delta = [2, 1, 1, 2, 3, 2, 3, 2, 2, 3, 1, 3, 2, 0, 1, 2, 2, 0, 0, 0, 2, 2, 4, 3, 1, 2, 1, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 2, 1]  # Represents movement, not total
    wip_delta = [0, 2, 2, 1, 2, 2, 3, 4, 2, 1, 3, 1, 1, 3, 2, 2, 3, 5, 3, 3, 2, 1, 1, 1, 3, 4, 4, 3, 1, 0, 0, 0, 1, 2, 3, 2, 1, 0, 0, 0, 0, 1]
    done_cumulative = [0, 0, 1, 2, 2, 4, 4, 5, 7, 9, 9, 11, 12, 12, 13, 13, 14, 14, 16, 16, 17, 18, 18, 19, 19, 19, 21, 23, 25, 26, 26, 26, 26, 27, 27, 29, 30, 31, 31, 31, 31, 31]

    # Compute actual cumulative To Do and WIP correctly
    todo_cumulative = []
    wip_cumulative = []
    
    current_todo = 0
    current_wip = 0

    for i in range(len(todo_delta)):
        # To Do accumulates from Backlog, but decreases when moving to WIP
        current_todo += todo_delta[i]
        if i > 0:
            current_todo -= wip_delta[i-1]  # Remove items that moved to WIP
        todo_cumulative.append(max(0, current_todo))  # Ensure no negatives

        # WIP accumulates from To Do, but decreases when moving to Done
        current_wip += wip_delta[i]
        if i > 0:
            current_wip -= (done_cumulative[i] - done_cumulative[i-1])  # Remove items moved to Done
        wip_cumulative.append(max(0, current_wip))  # Ensure no negatives

    # Calculate total count at each timestamp
    total_data = [b + t + w + d for b, t, w, d in zip(backlog_data, todo_cumulative, wip_cumulative, done_cumulative)]

    # Define labels (timestamps)
    labels = [
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
    ]

    # Create chart data dictionary
    chart_data = {
        "chartData": {
            "labels": labels,
            "datasets": [
                {"label": "Backlog", "data": backlog_data},
                {"label": "To Do", "data": todo_cumulative},  # Now correctly cumulative
                {"label": "WIP", "data": wip_cumulative},  # Now correctly cumulative
                {"label": "Done", "data": done_cumulative},  # Done is cumulative
                {"label": "Total", "data": total_data}  # Added total count dataset
            ]
        }
    }

    context = {"chart_data": json.dumps(chart_data)}
    template_file_url = f"{app_name}/kanban_home/cfd_chart.html"
    return render(request, template_file_url, context)

# template_file_url = f"{app_name}/kanban_home/cfd_chart.html"
# return render(request, template_file_url, context)
