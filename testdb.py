import sqlite3
from time import timezone
from xlsxwriter import Workbook
from io import BytesIO
from django.utils.http import urlquote
from django.http import StreamingHttpResponse
def info_output(request):

    workbook = Workbook()
    worksheet = workbook.add_worksheet()
    # 传入数据库路径，db.s3db或者test.sqlite
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    my_data = c.execute("select * from question")
    for i, row in enumerate(my_data):
        for j, value in enumerate(row):
            worksheet.write(i, j, value)

    output = BytesIO()
    workbook.save(output)
    output.seek(0)
    response = StreamingHttpResponse(output)
    response['content_type'] = 'application/vnd.ms-excel'
    response['charset'] = 'utf-8'
    response['Content-Disposition'] = 'attachment; filename="{0}.xls"'.format(
    timezone.datetime.now().strftime('%Y%m%d%H%M'))
    return response

