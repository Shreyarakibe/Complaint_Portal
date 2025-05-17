# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .models import Complaint
# from .forms import ComplaintForm

# # @login_required
# # def dashboard(request):
# #     complaints = Complaint.objects.filter(user=request.user).order_by('-date_submitted')
# #     context = {
# #         'complaints': complaints,
# #         'pending_count': complaints.filter(status='pending').count(),
# #         'inprogress_count': complaints.filter(status='in_progress').count(),
# #         'resolved_count': complaints.filter(status='resolved').count(),
# #         'closed_count': complaints.filter(status='closed').count(),
# #     }
# #     return render(request, 'complaints/dashboard.html', context)

# # def dashboard(request):
# #     complaints = Complaint.objects.filter(user=request.user)
# #     pending_count = complaints.filter(status='pending').count()
# #     inprogress_count = complaints.filter(status='in_progress').count()  # Make sure this line exists
# #     resolved_count = complaints.filter(status='resolved').count()
    
# #     context = {
# #         'complaints': complaints,
# #         'pending_count': pending_count,
# #         'inprogress_count': inprogress_count,  # Make sure this is passed to the template
# #         'resolved_count': resolved_count,
# #     }
    
# #     return render(request, 'complaints/dashboard.html', context)

# def dashboard(request):
#     complaints = Complaint.objects.filter(user=request.user)
#     pending_count = complaints.filter(status='pending').count()
#     inprogress_count = complaints.filter(status='in_progress').count()
#     resolved_count = complaints.filter(status='resolved').count()
#     closed_count = complaints.filter(status='closed').count()
    
#     context = {
#         'complaints': complaints,
#         'pending_count': pending_count,
#         'inprogress_count': inprogress_count,
#         'resolved_count': resolved_count,
#         'closed_count': closed_count,
#     }
    
#     return render(request, 'complaints/dashboard.html', context)

# @login_required
# def add_complaint(request):
#     if request.method == 'POST':
#         form = ComplaintForm(request.POST)
#         if form.is_valid():
#             complaint = form.save(commit=False)
#             complaint.user = request.user
#             complaint.save()
#             messages.success(request, 'Your complaint has been submitted successfully!')
#             return redirect('dashboard')
#     else:
#         form = ComplaintForm()
#     return render(request, 'complaints/add_complaint.html', {'form': form})

# @login_required
# # def view_complaint(request, pk):
# #     complaint = get_object_or_404(Complaint, pk=pk, user=request.user)
# #     return render(request, 'complaints/view_complaint.html', {'complaint': complaint})

# # from django.shortcuts import render, redirect, get_object_or_404
# # from .models import Complaint
# # from .forms import ComplaintForm

# # def edit_complaint(request, pk):
# #     complaint = get_object_or_404(Complaint, pk=pk, user=request.user)
    
# #     if request.method == 'POST':
# #         form = ComplaintForm(request.POST, instance=complaint)
# #         if form.is_valid():
# #             form.save()
# #             messages.success(request, 'Your complaint has been updated!')
# #             return redirect('view_complaint', pk=complaint.pk)
# #     else:
# #         form = ComplaintForm(instance=complaint)
    
# #     return render(request, 'complaints/edit_complaint.html', {'form': form, 'complaint': complaint})

# def edit_complaint(request, pk):
#     complaint = get_object_or_404(Complaint, pk=pk, user=request.user)
    
#     if request.method == 'POST':
#         form = ComplaintForm(request.POST, instance=complaint)
#         if form.is_valid():
#             complaint = form.save(commit=False)
#             # Update the status from the form
#             complaint.status = request.POST.get('status')
#             complaint.save()
#             messages.success(request, 'Your complaint has been updated!')
#             return redirect('view_complaint', pk=complaint.pk)
#     else:
#         form = ComplaintForm(instance=complaint)
    
#     return render(request, 'complaints/edit_complaint.html', {'form': form, 'complaint': complaint})

# def update_status(request, pk):
#     complaint = get_object_or_404(Complaint, pk=pk)
    
#     # Check if the user is allowed to update status
#     if request.user.is_staff or request.user.is_superuser:
#         if request.method == 'POST':
#             new_status = request.POST.get('status')
#             complaint.status = new_status
#             complaint.save()
#             messages.success(request, f'Status updated to {dict(Complaint.STATUS_CHOICES).get(new_status)}')
    
#     return redirect('view_complaint', pk=complaint.pk)

#Your Django views are well-structured, and they follow best practices for handling user complaints. Below is a breakdown of key points and some minor improvements:


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Complaint
from .forms import ComplaintForm
@login_required 
def dashboard(request):
    complaints = Complaint.objects.filter(user=request.user)
    pending_count = complaints.filter(status='pending').count()
    inprogress_count = complaints.filter(status='in_progress').count()
    resolved_count = complaints.filter(status='resolved').count()
    closed_count = complaints.filter(status='closed').count()
    
    context = {
        'complaints': complaints,
        'pending_count': pending_count,
        'inprogress_count': inprogress_count,
        'resolved_count': resolved_count,
        'closed_count': closed_count,
    }
    
    return render(request, 'complaints/dashboard.html', context)

@login_required
def add_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            messages.success(request, 'Your complaint has been submitted successfully!')
            return redirect('dashboard')
    else:
        form = ComplaintForm()
    return render(request, 'complaints/add_complaint.html', {'form': form})

@login_required
def view_complaint(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk, user=request.user)
    return render(request, 'complaints/view_complaint.html', {'complaint': complaint})

# @login_required
# def edit_complaint(request, pk):
#     complaint = get_object_or_404(Complaint, pk=pk, user=request.user)
    
#     if request.method == 'POST':
#         form = ComplaintForm(request.POST, instance=complaint)
#         if form.is_valid():
#             complaint = form.save(commit=False)
#             # Update the status from the form
#             complaint.status = request.POST.get('status')
#             complaint.save()
#             messages.success(request, 'Your complaint has been updated!')
#             return redirect('view_complaint', pk=complaint.pk)
#     else:
#         form = ComplaintForm(instance=complaint)
    
#     return render(request, 'complaints/edit_complaint.html', {'form': form, 'complaint': complaint})

@login_required
def edit_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id, user=request.user)
    
    if request.method == 'POST':
        form = ComplaintForm(request.POST, instance=complaint)
        if form.is_valid():
            complaint = form.save(commit=False)
            # Still get the status from the dropdown if needed
            status = request.POST.get('status')
            if status:
                complaint.status = status
            complaint.save()
            messages.success(request, 'Your complaint has been updated!')
            return redirect('view_complaint', pk=complaint.id)
    else:
        form = ComplaintForm(instance=complaint)
    
    return render(request, 'complaints/edit_complaint.html', {'form': form, 'complaint': complaint})


def update_status(request, complaint_id):
    if request.method == 'POST':
        complaint = get_object_or_404(Complaint, id=complaint_id)
        new_status = request.POST.get('status')
        if new_status in ['pending', 'in_progress', 'resolved', 'closed']:
            complaint.status = new_status
            complaint.save()
        return redirect('view_complaint', complaint_id)
    return redirect('view_complaint', complaint_id)