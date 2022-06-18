from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
import csv
import time
import datetime
from .forms import DistanceForm
import pandas as pd
def CalculateView(request):
    if request.method == 'POST':
        distance=request.POST.get("distance")
        input_time=request.POST.get("appt")
        t = time.strptime(input_time, "%H:%M")
        timevalue_12hour = time.strftime( "%I:%M %p", t )
        # print(timevalue_12hour)
        df1=pd.read_csv('user_file.csv')
        list_of_time = df1['Time'].tolist()
        list_of_service_charge = df1['ServiceCharge(%)'].tolist()
        list_of_surge_charge = df1['SurgeCharge(%)'].tolist()
        list_of_initial_rate = df1['InitialFare'].tolist()
        
        list_of_kn_rate=df1['KmRate'].tolist()
        
        for i in range(30):
            if timevalue_12hour[:2]==list_of_time[i][:2] and timevalue_12hour[3:5] >= list_of_time[i][3:5] and timevalue_12hour[-2:]==list_of_time[i][-2:]:
                initial_fare=list_of_initial_rate[i]
                print(initial_fare)
                km_fare=int(distance) * list_of_kn_rate[i]
                print(km_fare)
                net_total_charge=initial_fare + km_fare 
                surge_charge= int(list_of_surge_charge[i]) * 0.01 * int(net_total_charge)
                print(surge_charge)
                service_charge= int(list_of_service_charge[i]) * 0.01 * int(net_total_charge)
                print(service_charge)
                total_charge=int(net_total_charge) + surge_charge +service_charge
                return render(request, 'result.html',{'context':total_charge})

            
            
            
    return render(request, 'newFile.html')


        # print(list_of_single_column)
        # with open('user_file.csv') as csvfile:
        #     reader = csv.DictReader(csvfile)
        #     for col in reader:
        #         print(col[0][1])
            # for i in range (20):
            #     for i, row in enumerate(reader):
                    # print(row[i]['Time'])
                    # if (row['Time'][i] == timevalue_12hour):
                    # if timevalue_12hour >= row['Time'][i] and timevalue_12hour < row['Time'][i+1]:
                    # # if  time_in_range(start, end, datetime.time(23, 30, 0))
                    #     initial_fare=row["InitialFare"][i]
                    #     print(initial_fare)
                    #     km_fare=int(distance) * row["KmRate"][i]
                    #     net_total_charge=initial_fare + km_fare 
                    #     surge_charge= int(row["SurgeCharge(%)"][i]) * 0.01 * int(net_total_charge)
                    #     service_charge= int(row["ServiceCharge(%)"][i]) * 0.01 * int(net_total_charge)
                    #     total_charge=int(net_total_charge) + surge_charge +service_charge
                        # break
                    # return render(request, 'result.html',{'context':total_charge})
        




# def CalculateView(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = DistanceForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             distance=form.cleaned_data.get("distance")
#             time=form.cleaned_data.get("time")
#             print(distance)
#             print(time)
#             with open('user_file.csv') as csvfile:
#                 reader = csv.DictReader(csvfile)
#                 print(reader)
#                 for row in reader:
#                     print(row["Time"])
#                     print(time)
#                     if (row['Time'] == time):
#                         initial_fare=row["Initial Fare"]
#                         km_fare=distance * row["Km rate"]
#                         net_total_charge=initial_fare + km_fare 
#                         surge_charge= int(row["Surge Charge"]) * 0.01 * net_total_charge
#                         service_charge= int(row["Service charge"]) * 0.01 * net_total_charge
#                         total_charge=net_total_charge + surge_charge +service_charge
#                         print("The total fair is",{total_charge})
#                         return HttpResponseRedirect('/thanks/')
#                     else:
#                         print("error")

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = DistanceForm

#     return render(request, 'new.html', {'form': form})
# Create your views here.
