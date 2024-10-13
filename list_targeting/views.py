from django.shortcuts import render, redirect

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
        
        # Retrieving the radio button selection
        media_selection_pdf = request.POST.get('radio__pdf')
        media_selection_billmessage = request.POST.get('radio__billmessage')

        # Handling file uploads (for multiple files use 'getlist')
        uploaded_file = request.FILES.get('csvUpload')
        # if uploaded_file:
            # fs = FileSystemStorage()
            # filename = fs.save(uploaded_file.name, uploaded_file)
            # file_url = fs.url(filename)
        # else:
            # file_url = None



        if request.POST.get('action') == 'save':
            # Handle the save action
            response = {
                "message_id": request_id,
                "message_format":  "MESSAGE",
                "target_format": "LIST",
                "category_ind": customer_type,
                "start_date": start_date,
                "end_date": end_date,   
                "status_ind": "SUBMITTED",
                "priority_ind": 1,
                # Populate the cust_ids by extracting from the csv file,
                "cust_bill_acc_id_list": "csv_file",
                "message_text": bill_message
            }

        elif request.POST.get('action') == 'submit':
            response = {
                "message_id": request_id,
                "message_format":  "MESSAGE",
                "target_format": "LIST",
                "category_ind": customer_type,
                "start_date": start_date,
                "end_date": end_date,
                "status_ind": "SUBMITTED",
                "priority_ind": 1,
                "cust_bill_acc_id_list": "csv_file", # Populate the cust_ids by extracting from the csv file,
                "message_text": bill_message
            }
        

        return redirect('list_targeting:list_targeting')

    return render(request, 'app/list-targeting.html')


def criteria_targeting(request):
    return render(request, 'app/criteria-targeting.html')