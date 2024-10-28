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

        elif request.POST.get('action')  == 'delete':
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


def criteria_targeting(request):
    return render(request, 'app/criteria-targeting.html')
