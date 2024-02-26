from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Compete, ApplyCompete
from .form import CreateCompeteForm, UpdateCompeteForm


# Create a job

def create_compete(request):
    if request.user.is_recruiter and request.user.has_company:
        if request.method == 'POST':
            form = CreateCompeteForm(request.POST)
            if form.is_valid():
                var = form.save(commit=False)
                var.user = request.user
                var.company =  request.user.company
                var.save()
                messages.info(request,'New Competition has been created')
                return redirect('dashboard')
            
            else:
                messages.warning(request,'Something went wrong')
                return redirect('create-compete')
            
        else:
            form = CreateCompeteForm()
            context = {'form': form}
            return render(request, 'compete/create_compete.html',context)
    else:
        messages.warning(request,'You must be a registered company to perform this action')
        return redirect('dashboard')    
        
def update_compete (request,pk):
    compete = Compete.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateCompeteForm(request.POST, instance = compete)
        if form.is_valid():
            form.save()
            messages.info(request,'Competition info has been updated')
            return redirect('dashboard')
        
        else:
            messages.warning(request,'Something went wrong')
        
    else:
        form = UpdateCompeteForm(instance=compete)
        context = {'form': form}
        return render(request, 'compete/update_compete.html',context)
   
   
def manage_compete(request):
    compete = Compete.objects.filter(user=request.user, company = request.user.company)
    context = {'compete':compete}
    return render(request, 'compete/manage_compete.html',context)

def apply_to_compete(request,pk):
    if request.user.is_authenticated and request.user.is_applicant:
        compete = Compete.objects.get(pk=pk)
        if ApplyCompete.objects.filter(user=request.user,compete=pk).exists():
            messages.warning(request,'Permission Denied')
            return redirect('dashboard')
        else:
            ApplyCompete.objects.create(
                compete = compete,
                user  = request.user,
                status = 'Pending'
            )
            messages.info(request, 'You have successfully applied! Please see dashboard')
            return redirect('dashboard')
    else:
        messages.info(request, 'Please log in to continue')
        return redirect('login')
    
def all_applicants(request,pk):
    compete = Compete.objects.get(pk=pk)
    applicants = Compete.applycompete_set.all()
    context ={'Compete':compete, 'applicants':applicants}
    return render(request, 'compete/all_applicants.html',context)
 
def applied_compete(request):
    compete = ApplyCompete.objects.filter(user = request.user)
    context ={'compete':compete}
    return render(request,'compete/applied_compete.html',context)

def delete_compete(request, pk):
    compete = Compete.objects.get(pk=pk)
    
    # Check if the logged-in user is the owner of the competition
    if request.user == compete.user:
        compete.delete()
        messages.info(request, 'Competition has been deleted')
    else:
        messages.warning(request, 'You do not have permission to delete this competition')
    
    return redirect('manage-compete')