from django import http
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
import time
from django.core.exceptions import ValidationError
from django.http import HttpResponse
import pandas as pd
def CalculateView(request):
    if request.method == 'POST':
        distance=request.POST.get("distance")
        input_time=request.POST.get("appt")
        if input_time =='':
            messages.error(request,'Please enter a valid date ')
            return  render(request, 'newFile.html')
        t = time.strptime(input_time, "%H:%M")
        timevalue_12hour = time.strftime( "%I:%M %p", t )
        df1=pd.read_csv('user_file.csv')
        list_of_time = df1['Time'].tolist()
        list_of_service_charge = df1['ServiceCharge(%)'].tolist()
        list_of_surge_charge = df1['SurgeCharge(%)'].tolist()
        list_of_initial_rate = df1['InitialFare'].tolist()
        list_of_kn_rate=df1['KmRate'].tolist()
        
        for i in range(30):
            if timevalue_12hour[:2]==list_of_time[i][:2] and timevalue_12hour[3:5] >= list_of_time[i][3:5] and timevalue_12hour[-2:]==list_of_time[i][-2:]:
                initial_fare=list_of_initial_rate[i]
                km_fare=int(distance) * list_of_kn_rate[i]
                net_total_charge=initial_fare + km_fare 
                surge_charge= int(list_of_surge_charge[i]) * 0.01 * int(net_total_charge)
                service_charge= int(list_of_service_charge[i]) * 0.01 * int(net_total_charge)
                total_charge=int(net_total_charge) + surge_charge +service_charge
        return render(request, 'result.html',{'context':total_charge}) 

         
            
    return render(request, 'newFile.html')


        