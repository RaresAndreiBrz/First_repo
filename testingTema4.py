from datetime import datetime, timedelta

def zilepanalaziuata(data_urmatoarei_sarbatori):
    azi = datetime.today()
    data_urmatoarei_sarbatori = datetime.strptime(data_urmatoarei_sarbatori, '%Y/%m/%d')
    zileramase = data_urmatoarei_sarbatori - azi
    return zileramase.days

print(zilepanalaziuata('2023/04/28'))
