import os
from django.http import HttpResponse
import sys
import requests
from subprocess import run,PIPE
from django.shortcuts import render


    def external(request):
        inp = request.POST.get('param')
        out = run([sys.executable,'//home//sp//Desktop//web1//web1//run_cmd.py',inp],shell=False,stdout=PIPE)
        print(out)
        return render(request,'page1.html',{'data1':out.stdout})


    


