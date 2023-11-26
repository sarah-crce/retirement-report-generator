from inflation_model.inflation_prediction import inflation_predict
import matplotlib.pyplot as plt
import numpy as np
from expense_scenarios.expense_calculator import living_expense, health_expense, misc_expense


lng_year = []
lng_sc_liv_list = []
lng_sc_health_list = []
lng_sc_misc_list = []
lng_exp_text = []




def longetivity_scenario(sc_year,liv_exp,health_exp,misc_exp):
    n = sc_year[-1]
    print(n)
    for i in range(n+1,n+21):
        lng_year.append(i)
        inflation_rate = inflation_predict(i)
        lng_sc_liv_list.append(living_expense(inflation_rate,liv_exp))
        lng_sc_health_list.append(health_expense(inflation_rate,health_exp))
        lng_sc_misc_list.append(misc_expense(inflation_rate,misc_exp))
    lng_exp_text.append(plot_longetivity_liv_scenario(lng_year, lng_sc_liv_list))
    lng_exp_text.append(plot_longetivity_health_scenario(lng_year, lng_sc_health_list))
    lng_exp_text.append(plot_longetivity_misc_scenario(lng_year, lng_sc_misc_list))
    return lng_exp_text

    
def plot_longetivity_liv_scenario(year, liv_exp_list):
    plt.figure(figsize=(10, 6))
    plt.plot(year, liv_exp_list, label='Living Expenses', marker='o')
    plt.xlabel('Year')
    plt.xticks(year)
    plt.ylabel('Expense Amount')
    plt.title('Longetivity Living Expenses')
    plt.legend()
    plt.grid(True)
    plt.savefig('graphs/lng_liv_expenses_plot.png')
    

    liv_avg_exp = np.mean(liv_exp_list)
    liv_perc_change = np.diff(liv_exp_list) / liv_exp_list[:-1] * 100
    liv_max_exp_year = year[np.argmax(liv_exp_list)]
    liv_min_exp_year = year[np.argmin(liv_exp_list)]
    liv_avg_percent_change = np.mean(liv_perc_change)


    liv_text = "The graph illustrates the anticipated variations in living expenses (if a person lives longer) over the years based on fluctuations in inflation, assuming that the existing household expenditure remains constant."
    liv_text += f"The average expense over the period is {liv_avg_exp:.2f} units. "
    liv_text += f"The year where there is maximum expense is the year {liv_max_exp_year}."
    liv_text += f"The year where there is minimum expense is the year {liv_min_exp_year}."
    liv_text += f"The average percentage change between consecutive years is {liv_avg_percent_change}%, indicating the growth rate of expense. "

    return liv_text

    

def plot_longetivity_health_scenario(year, health_exp_list):
    plt.figure(figsize=(10, 6))
    plt.plot(year, health_exp_list, label='Health Expenses', marker='o', color='#FFD700')
    plt.xlabel('Year')
    plt.xticks(year)
    plt.ylabel('Expense Amount')
    plt.title('Longetivity Health Expenses')
    plt.legend()
    plt.grid(True)
    plt.savefig('graphs/lng_health_expenses_plot.png')
    

    health_avg_exp = np.mean(health_exp_list)
    health_perc_change = np.diff(health_exp_list) / health_exp_list[:-1] * 100
    health_max_exp_year = year[np.argmax(health_exp_list)]
    health_min_exp_year = year[np.argmin(health_exp_list)]
    health_avg_percent_change = np.mean(health_perc_change)


    health_text = "The graph illustrates the anticipated variations in healthcare expenses (if a person lives longer) over the years based on fluctuations in inflation, assuming that the existing healthcare expenditure remains constant."
    health_text += f"The average expense over the period is {health_avg_exp:.2f} units. "
    health_text += f"The year where there is maximum expense is the year {health_max_exp_year}."
    health_text += f"The year where there is minimum expense is the year {health_min_exp_year}."
    health_text += f"The average percentage change between consecutive years is {health_avg_percent_change}%, indicating the growth rate of expense. "

    return health_text

def plot_longetivity_misc_scenario(year, misc_exp_list):
    plt.figure(figsize=(10, 6))
    plt.plot(year, misc_exp_list, label='Miscellaneous Expenses', marker='o', color='green')
    plt.xlabel('Year')
    plt.xticks(year)
    plt.ylabel('Expense Amount')
    plt.title('Longetivity Miscellaneous Expenses')
    plt.legend()
    plt.grid(True)
    plt.savefig('graphs/lng_misc_expenses_plot.png')


    misc_avg_exp = np.mean(misc_exp_list)
    misc_perc_change = np.diff(misc_exp_list) / misc_exp_list[:-1] * 100
    misc_max_exp_year = year[np.argmax(misc_exp_list)]
    misc_min_exp_year = year[np.argmin(misc_exp_list)]
    misc_avg_percent_change = np.mean(misc_perc_change)


    misc_text = "The graph illustrates the anticipated variations in miscellaneous expenses (if a person lives longer) over the years based on fluctuations in inflation, assuming that the existing miscellaneous expenditure remains constant."
    misc_text += f"The average expense over the period is {misc_avg_exp:.2f} units. "
    misc_text += f"The year where there is maximum expense is the year {misc_max_exp_year}."
    misc_text += f"The year where there is minimum expense is the year {misc_min_exp_year}."
    misc_text += f"The average percentage change between consecutive years is {misc_avg_percent_change}%, indicating the growth rate of expense. "

    return misc_text
# longetivity_scenario([2057,2048],300000,500000,300000)

