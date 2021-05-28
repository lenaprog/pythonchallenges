def wash_hands(N, nM):
    wash_per_day_sec = N*21
    wash_total_month = 30*wash_per_day_sec*nM
    wash_total_month_minutes = wash_total_month//60
    wash_total_month_sec = wash_total_month%60

    print(f"{wash_total_month_minutes} minutes and {wash_total_month_sec} seconds.")

wash_hands(5, 3)