from datetime import datetime, timedelta

def get_end_of_month(date):
    if date.month == 12:
        next_month = date.replace(year=date.year + 1, month=1, day=1)
    else:
        next_month = date.replace(month=date.month + 1, day=1)
    
    return next_month - timedelta(days=1)