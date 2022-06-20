from googleapiclient.discovery import build
from google.oauth2 import service_account
from pycbrf.toolbox import ExchangeRates
from datetime import datetime
from decimal import Decimal
from celery import shared_task

from api.models import Order


@shared_task
def get_data_from_googlesheet():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    SERVICE_ACCOUNT_FILE = 'api/keys.json'

    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1mAej2M-wIJL3wapBaFXy6QaafuH3U0QOLHRy75jLEzE'

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="Лист1!A1:E100").execute()
    values = result.get('values')
    
    Order.objects.all().delete()
    
    for value in values:
        try:
            dt = datetime.strptime(value[3], '%d.%m.%Y').strftime('%Y-%m-%d')
            rates = ExchangeRates(dt)
            price_rub = Decimal(value[2]) * rates['USD'].value
            order, created = Order.objects.update_or_create(id_num=value[0], order_num=value[1], price_dol=value[2], price_rub=price_rub, get_data=dt)
            order.save()
        except ValueError:
            continue
