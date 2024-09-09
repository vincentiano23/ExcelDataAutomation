from django.shortcuts import render
from .forms import ExcelUploadForm
import pandas as pd

def upload_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
           
            excel_file = request.FILES['file']
            
           
            df = pd.read_excel(excel_file, engine='openpyxl', header=0)
            
        
            print(df.head()) 
            print(df.columns)
            
            
            filtered_df = df[df['NAME'].notnull()] 

           
            processed_file = 'studentDetails_filtered.xlsx'
            
            
            filtered_df.to_excel(processed_file, engine='openpyxl', index=False)
            
        
            return render(request, 'automation/upload_success.html', {'processed_file': processed_file})
    else:
        form = ExcelUploadForm()

    return render(request, 'automation/upload.html', {'form': form})
