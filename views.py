from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum, Avg, Min, Max
from .models import UploadedFile, CSVRow
import csv
def upload_csv(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        if not file.name.endswith('.csv'):
            return JsonResponse({'error': 'Invalid file format. Please upload a CSV file.'}, status=400)

        uploaded_file = UploadedFile.objects.create(name=file.name)
        csv_reader = csv.reader(file.read().decode('utf-8').splitlines())
        headers = next(csv_reader)

        for row in csv_reader:
            CSVRow.objects.create(
                file=uploaded_file,
                column1=float(row[0]) if row[0] else None,
                column2=float(row[1]) if row[1] else None
            )
        return JsonResponse({'message': 'File uploaded successfully!'}, status=201)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def aggregate(request):
    column = request.GET.get('column')
    agg_type = request.GET.get('agg_type')

    if not column or not agg_type:
        return JsonResponse({'error': 'Invalid parameters'}, status=400)

    if column not in ['column1', 'column2']:
        return JsonResponse({'error': 'Invalid column'}, status=400)

    agg_map = {
        'sum': Sum(column),
        'avg': Avg(column),
        'min': Min(column),
        'max': Max(column),
    }

    if agg_type not in agg_map:
        return JsonResponse({'error': 'Invalid aggregation type'}, status=400)

    result = CSVRow.objects.aggregate(result=agg_map[agg_type])
    return JsonResponse({'result': result['result']}, status=200)
