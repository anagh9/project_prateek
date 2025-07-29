from django.http import JsonResponse
from django.shortcuts import render, redirect
from datetime import datetime
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import csv
from django.contrib import messages
# Create your views here.


def redirection(request):
    return redirect('list_targeting:index')


def index(request):
    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        print(f"Request ID: {request_id}")
        return redirect('list_targeting:list_targetin_request_id', request_id=request_id)
    return render(request, 'app/home.html')


def list_targeting(request):

    if request.method == 'POST':
        request_id = request.POST.get('requestID')
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')
        customer_type = request.POST.get('customerType')
        bill_message = request.POST.get('bill_message')

        uploaded_file = request.FILES.get('csvUpload')
        printed_pdf = request.FILES.get('printedPdf')
        e_bill = request.FILES.get('eBillPdf')

        fs = FileSystemStorage()

        if not os.path.exists(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT)

        first_column_data = []
        message = None
        if uploaded_file and uploaded_file.name.endswith('.csv'):
            uploaded_file_name = fs.save(uploaded_file.name, uploaded_file)
            uploaded_file_url = fs.url(uploaded_file_name)
            print(f'CSV File saved at: {uploaded_file_url}')
            csv_file_path = os.path.join(
                settings.MEDIA_ROOT, uploaded_file_name)

            with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    if row:  # Ensure the row is not empty
                        first_column_data.append(row[0])

        if printed_pdf:
            printed_pdf_name = fs.save(printed_pdf.name, printed_pdf)
            printed_pdf_url = fs.url(printed_pdf_name)
            print(f'Printed PDF saved at: {printed_pdf_url}')

        if e_bill:
            e_bill_name = fs.save(e_bill.name, e_bill)
            e_bill_url = fs.url(e_bill_name)
            print(f'E-bill saved at: {e_bill_url}')

        if request.POST.get('action') == 'save':
            # Handle the save action
            message = "Request is saved successfully"
            messages.success(request, message)
            response = {
                "message_id": request_id,
                "message_format":  "MESSAGE",
                "target_format": "LIST",
                "category_ind": customer_type,
                # "start_date": datetime.strptime(start_date, "%d-%m-%Y"),
                # "end_date": datetime.strptime(end_date, "%d-%m-%Y"),
                "start_date": start_date,
                "end_date": end_date,
                "status_ind": "SAVED",
                "priority_ind": 1,
                # Populate the cust_ids by extracting from the csv file,
                "cust_bill_acc_id_list": first_column_data,
                "message_text": bill_message
            }

            print("#50", response)

        elif request.POST.get('action') == 'submit':
            message = "Request is submitted successfully"
            messages.success(request, message)

            response = {
                "message_id": request_id,
                "message_format":  "MESSAGE",
                "target_format": "LIST",
                "category_ind": customer_type,
                # "start_date": datetime.strptime(start_date, "%d-%m-%Y"),
                # "end_date": datetime.strptime(end_date, "%d-%m-%Y"),
                "start_date": start_date,
                "end_date": end_date,
                "status_ind": "SUBMITTED",
                "priority_ind": 1,
                # Populate the cust_ids by extracting from the csv file,
                "cust_bill_acc_id_list": first_column_data,
                "message_text": bill_message
            }
            print("#65", response)

        elif request.POST.get('action') == 'delete':
            message = "Request is deleted successfully"
            messages.success(request, message)

            response = {
                "message_id": request_id,
                "message_format":  "MESSAGE",
                "target_format": "LIST",
                "category_ind": customer_type,
                # "start_date": datetime.strptime(start_date, "%d-%m-%Y"),
                # "end_date": datetime.strptime(end_date, "%d-%m-%Y"),
                "start_date": start_date,
                "end_date": end_date,
                "status_ind": "DELETE",
                "priority_ind": 1,
                # Populate the cust_ids by extracting from the csv file,
                "cust_bill_acc_id_list": first_column_data,
                "message_text": bill_message
            }
            print("#65", response)

        return redirect('list_targeting:list_targeting', message=message)

    return render(request, 'app/list-targeting.html')


def list_targetin_request_id(request, request_id):

    # function to get the request details from the database
    # call from oracle db
    # get instance
    # example_response
    example_response = {
        'cust_bill_acc_id_list': '1234567890, 0987654321',
        'error_date': '2021-09-01',
        'media_selection': 'MESSAGE',
        'message_text': 'hi',
        'mrm_request_id': '1234567890',
        # other fields

    }

    if request.method == 'POST':
        request_id = request.POST.get('requestID')
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')
        customer_type = request.POST.get('customerType')
        bill_message = request.POST.get('bill_message')

        uploaded_file = request.FILES.get('csvUpload')
        printed_pdf = request.FILES.get('printedPdf')
        e_bill = request.FILES.get('eBillPdf')

        fs = FileSystemStorage()

        if not os.path.exists(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT)

        first_column_data = []
        message = None
        if uploaded_file and uploaded_file.name.endswith('.csv'):
            uploaded_file_name = fs.save(uploaded_file.name, uploaded_file)
            uploaded_file_url = fs.url(uploaded_file_name)
            print(f'CSV File saved at: {uploaded_file_url}')
            csv_file_path = os.path.join(
                settings.MEDIA_ROOT, uploaded_file_name)

            with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    if row:  # Ensure the row is not empty
                        first_column_data.append(row[0])

        if printed_pdf:
            printed_pdf_name = fs.save(printed_pdf.name, printed_pdf)
            printed_pdf_url = fs.url(printed_pdf_name)
            print(f'Printed PDF saved at: {printed_pdf_url}')

        if e_bill:
            e_bill_name = fs.save(e_bill.name, e_bill)
            e_bill_url = fs.url(e_bill_name)
            print(f'E-bill saved at: {e_bill_url}')

        if request.POST.get('action') == 'save':
            # Handle the save action
            message = "Request is saved successfully"
            messages.success(request, message)
            response = {
                "message_id": request_id,
                "message_format":  "MESSAGE",
                "target_format": "LIST",
                "category_ind": customer_type,
                # "start_date": datetime.strptime(start_date, "%d-%m-%Y"),
                # "end_date": datetime.strptime(end_date, "%d-%m-%Y"),
                "start_date": start_date,
                "end_date": end_date,
                "status_ind": "SAVED",
                "priority_ind": 1,
                # Populate the cust_ids by extracting from the csv file,
                "cust_bill_acc_id_list": first_column_data,
                "message_text": bill_message
            }

            print("#50", response)

        elif request.POST.get('action') == 'submit':
            message = "Request is submitted successfully"
            messages.success(request, message)

            response = {
                "message_id": request_id,
                "message_format":  "MESSAGE",
                "target_format": "LIST",
                "category_ind": customer_type,
                # "start_date": datetime.strptime(start_date, "%d-%m-%Y"),
                # "end_date": datetime.strptime(end_date, "%d-%m-%Y"),
                "start_date": start_date,
                "end_date": end_date,
                "status_ind": "SUBMITTED",
                "priority_ind": 1,
                # Populate the cust_ids by extracting from the csv file,
                "cust_bill_acc_id_list": first_column_data,
                "message_text": bill_message
            }
            print("#65", response)

        elif request.POST.get('action') == 'delete':
            message = "Request is deleted successfully"
            messages.success(request, message)

            response = {
                "message_id": request_id,
                "message_format":  "MESSAGE",
                "target_format": "LIST",
                "category_ind": customer_type,
                # "start_date": datetime.strptime(start_date, "%d-%m-%Y"),
                # "end_date": datetime.strptime(end_date, "%d-%m-%Y"),
                "start_date": start_date,
                "end_date": end_date,
                "status_ind": "DELETE",
                "priority_ind": 1,
                # Populate the cust_ids by extracting from the csv file,
                "cust_bill_acc_id_list": first_column_data,
                "message_text": bill_message
            }
            print("#65", response)

        return redirect('list_targeting:list_targeting', message=message)

    return render(request, 'app/list-targeting.html', context={'example_response': example_response})


def criteria_targeting(request):
    return render(request, 'app/criteria-targeting.html')


def reporting_dashboard(request):
    return render(request, 'app/reporting-dashboard.html')


def reporting_dashboard2(request):
    return render(request, 'app/reportingdashboard.html')


def get_report_data(request):
    """
    API endpoint to fetch report data from an Oracle package.
    This view expects GET parameters for filtering (e.g., start_date, end_date, bill_cycle).
    """
    if request.method == 'GET':
        # 'dateRange' or 'billCycle'
        report_type = request.GET.get('report_type')
        data = []  # This will hold the data fetched from Oracle

        if report_type == 'dateRange':
            start_date_str = request.GET.get('start_date')
            end_date_str = request.GET.get('end_date')

            if not all([start_date_str, end_date_str]):
                return JsonResponse({'error': 'Start date and end date are required for date range search.'}, status=400)

            try:
                # --- Oracle Package Call for Date Range (Conceptual) ---
                # Replace with your actual Oracle connection details and package call
                # Example using cx_Oracle (requires setup):
                # connection = cx_Oracle.connect("your_user/your_password@your_host:your_port/your_service_name")
                # cursor = connection.cursor()
                #
                # # Assuming your Oracle package has a function like GET_DATA_BY_DATE_RANGE
                # # that returns a REF CURSOR or similar.
                # output_cursor = connection.cursor()
                # cursor.callproc("YOUR_ORACLE_PACKAGE.GET_DATA_BY_DATE_RANGE", [start_date_str, end_date_str, output_cursor])
                #
                # # Fetch all rows from the output cursor
                # for row in output_cursor:
                #     # Map Oracle row data to a dictionary that matches your JavaScript 'tableData' structure
                #     data.append({
                #         'messageRequestId': row[0],
                #         'status': row[1],
                #         'projectTitle': row[2],
                #         'projectOwner': row[3],
                #         'projectType': row[4],
                #         'category': row[5],
                #         'startDate': row[6].strftime('%Y-%m-%d') if row[6] else None, # Format date
                #         'endDate': row[7].strftime('%Y-%m-%d') if row[7] else None,   # Format date
                #         'targetingType': row[8],
                #         # Include other fields if your Oracle package returns them for this mode
                #     })
                #
                # cursor.close()
                # connection.close()
                # --- End Oracle Package Call ---

                # Dummy data for date range (replace with actual Oracle data)
                data = [
                    {'messageRequestId': '111111', 'status': 'Submitted', 'projectTitle': 'Consumer - Bend Notice (Fake)', 'projectOwner': 'John Smith',
                     'projectType': 'Bill Message', 'category': 'GRA', 'startDate': '2025-06-01', 'endDate': '2025-07-01', 'targetingType': 'Criteria Targeting'},
                    {'messageRequestId': '222222', 'status': 'Submitted', 'projectTitle': 'Commercial - Customer Notice (Fake)', 'projectOwner': 'Jane Smith',
                     'projectType': 'Bill Onsert', 'category': 'Customer', 'startDate': '2025-05-01', 'endDate': '2025-07-01', 'targetingType': 'List Targeting'},
                    {'messageRequestId': '333333', 'status': 'Saved', 'projectTitle': 'Consumer - St George - Mobile Rollout (Fake)', 'projectOwner': 'Jackie Smith',
                     'projectType': 'Bill Onsert', 'category': 'Marketing', 'startDate': '2025-07-01', 'endDate': '2025-09-01', 'targetingType': 'List Targeting'},
                    {'messageRequestId': '444444', 'status': 'Pending', 'projectTitle': 'Internal - System Update (Fake)', 'projectOwner': 'Alice Brown',
                     'projectType': 'System Alert', 'category': 'IT', 'startDate': '2025-08-15', 'endDate': '2025-08-30', 'targetingType': 'All Users'},
                    {'messageRequestId': '555555', 'status': 'Approved', 'projectTitle': 'Holiday Promotion (Fake)', 'projectOwner': 'Bob Johnson', 'projectType': 'Marketing Campaign',
                     'category': 'Sales', 'startDate': '2025-09-01', 'endDate': '2025-10-15', 'targetingType': 'Customer Segment'}
                ]
                # Filter dummy data by date for demonstration
                data = [row for row in data if row['startDate'] >=
                        start_date_str and row['endDate'] <= end_date_str]

            except Exception as e:
                return JsonResponse({'error': f'Error fetching date range data: {str(e)}'}, status=500)

        elif report_type == 'billCycle':
            bill_cycle = request.GET.get('bill_cycle')

            if not bill_cycle:
                return JsonResponse({'error': 'Bill cycle is required for bill cycle prioritization.'}, status=400)

            try:
                # --- Oracle Package Call for Bill Cycle (Conceptual) ---
                # connection = cx_Oracle.connect("your_user/your_password@your_host:your_port/your_service_name")
                # cursor = connection.cursor()
                # output_cursor = connection.cursor()
                # cursor.callproc("YOUR_ORACLE_PACKAGE.GET_DATA_BY_BILL_CYCLE", [bill_cycle, output_cursor])
                #
                # for row in output_cursor:
                #     data.append({
                #         'projectPlacement': row[0],
                #         'categoryRank': row[1],
                #         'priority': bool(row[2]), # Convert 0/1 to boolean
                #         'messageRequestId': row[3], # Project ID
                #         'projectTitle': row[4],
                #         'projectOwner': row[5],
                #         'projectType': row[6],
                #         'category': row[7],
                #         'startDate': row[8].strftime('%Y-%m-%d') if row[8] else None,
                #         'endDate': row[9].strftime('%Y-%m-%d') if row[9] else None,
                #         'lastModifiedBy': row[10],
                #     })
                #
                # cursor.close()
                # connection.close()
                # --- End Oracle Package Call ---

                # Dummy data for bill cycle (replace with actual Oracle data)
                # For simplicity, we'll return all dummy data for any selected bill cycle.
                # In a real scenario, your Oracle package would filter by bill_cycle.
                data = [
                    {'messageRequestId': '111111', 'status': 'Submitted', 'projectTitle': 'Consumer - Bend Notice (Fake)', 'projectOwner': 'John Smith', 'projectType': 'Bill Message', 'category': 'GRA',
                     'startDate': '2025-06-01', 'endDate': '2025-07-01', 'targetingType': 'Criteria Targeting', 'projectPlacement': 'Top', 'categoryRank': 1, 'priority': True, 'lastModifiedBy': 'Admin A'},
                    {'messageRequestId': '222222', 'status': 'Submitted', 'projectTitle': 'Commercial - Customer Notice (Fake)', 'projectOwner': 'Jane Smith', 'projectType': 'Bill Onsert', 'category': 'Customer',
                     'startDate': '2025-05-01', 'endDate': '2025-07-01', 'targetingType': 'List Targeting', 'projectPlacement': 'Middle', 'categoryRank': 2, 'priority': False, 'lastModifiedBy': 'Admin B'},
                    {'messageRequestId': '333333', 'status': 'Saved', 'projectTitle': 'Consumer - St George - Mobile Rollout (Fake)', 'projectOwner': 'Jackie Smith', 'projectType': 'Bill Onsert', 'category': 'Marketing',
                     'startDate': '2025-07-01', 'endDate': '2025-09-01', 'targetingType': 'List Targeting', 'projectPlacement': 'Bottom', 'categoryRank': 3, 'priority': True, 'lastModifiedBy': 'Admin C'},
                    {'messageRequestId': '444444', 'status': 'Pending', 'projectTitle': 'Internal - System Update (Fake)', 'projectOwner': 'Alice Brown', 'projectType': 'System Alert', 'category': 'IT',
                     'startDate': '2025-08-15', 'endDate': '2025-08-30', 'targetingType': 'All Users', 'projectPlacement': 'Middle', 'categoryRank': 4, 'priority': False, 'lastModifiedBy': 'Admin A'},
                    {'messageRequestId': '555555', 'status': 'Approved', 'projectTitle': 'Holiday Promotion (Fake)', 'projectOwner': 'Bob Johnson', 'projectType': 'Marketing Campaign', 'category': 'Sales',
                     'startDate': '2025-09-01', 'endDate': '2025-10-15', 'targetingType': 'Customer Segment', 'projectPlacement': 'Top', 'categoryRank': 1, 'priority': True, 'lastModifiedBy': 'Admin B'}
                ]
                # In a real scenario, you'd filter this dummy data by bill_cycle if it was relevant
                # For now, it just returns all of it.
            except Exception as e:
                return JsonResponse({'error': f'Error fetching bill cycle data: {str(e)}'}, status=500)
        else:
            return JsonResponse({'error': 'Invalid report type.'}, status=400)

        # safe=False is needed when returning a list/array
        return JsonResponse(data, safe=False)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)
