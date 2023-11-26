def living_expense(inflation_rate,liv_exp):
    liv_inf = inflation_rate/100
    liv_amt =  liv_exp * (1+liv_inf)
    return liv_amt
    

def health_expense(inflation_rate,health_exp):
    health_inf = inflation_rate/100
    health_amt =  health_exp * (1+health_inf)
    return health_amt

def misc_expense(inflation_rate,misc_exp):
    misc_inf = inflation_rate/100
    misc_amt =  misc_exp * (1+misc_inf)
    return misc_amt