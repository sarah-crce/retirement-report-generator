from expense_scenarios import expense_calculator as calc
from inflation_model import inflation_prediction as inf
import matplotlib.pyplot as plt
import numpy as np
from expense_scenarios import longetivity_scenario as lng_sc



year = []
liv_exp_list = []
health_exp_list = []
misc_exp_list = []
exp_text= []


def expense_projector(name,age,retirement_age,life_span,savings,income,liv_exp,health_exp,misc_exp):
    global lng_exp_text
    n = life_span - age
    life_span_year = 2023+n
    for i in range(2024,life_span_year):
        year.append(i)
        inflation_rate = inf.inflation_predict(i)
        liv_exp_list.append(calc.living_expense(inflation_rate,liv_exp))
        health_exp_list.append(calc.health_expense(inflation_rate,health_exp))
        misc_exp_list.append(calc.misc_expense(inflation_rate,misc_exp))
    exp_text.append(plot_living_expense(year, liv_exp_list))
    exp_text.append(plot_health_expense(year, health_exp_list))
    exp_text.append(plot_misc_expense(year, misc_exp_list))
    lng_exp_text = lng_sc.longetivity_scenario(year, liv_exp_list[-1], health_exp_list[-1], misc_exp_list[-1])



def plot_living_expense(year, liv_exp_list):
    plt.figure(figsize=(10, 6))
    plt.plot(year, liv_exp_list, label='Living Expenses', marker='o')
    plt.xlabel('Year')
    plt.ylabel('Expense Amount')
    plt.title('Projected Living Expenses Over Time')
    plt.legend()
    plt.grid(True)
    plt.savefig('graphs/living_expenses_plot.png')


    liv_avg_exp = np.mean(liv_exp_list)
    liv_perc_change = np.diff(liv_exp_list) / liv_exp_list[:-1] * 100
    liv_max_exp_year = year[np.argmax(liv_exp_list)]
    liv_min_exp_year = year[np.argmin(liv_exp_list)]
    liv_avg_percent_change = np.mean(liv_perc_change)


    liv_text = "The graph illustrates the anticipated variations in living expenses over the years based on fluctuations in inflation, assuming that the existing household expenditure remains constant."
    liv_text += f"The average expense over the period is {liv_avg_exp:.2f} units. "
    liv_text += f"The year where there is maximum expense is the year {liv_max_exp_year}."
    liv_text += f"The year where there is minimum expense is the year {liv_min_exp_year}."
    liv_text += f"The average percentage change between consecutive years is {liv_avg_percent_change}%, indicating the growth rate of expense. "

    return liv_text

    

def plot_health_expense(year, health_exp_list):
    plt.figure(figsize=(10, 6))
    plt.plot(year, health_exp_list, label='Health Expenses', marker='o', color='#FFD700')
    plt.xlabel('Year')
    plt.ylabel('Expense Amount')
    plt.title('Projected Health Expenses Over Time')
    plt.legend()
    plt.grid(True)
    plt.savefig('graphs/health_expenses_plot.png')


    health_avg_exp = np.mean(health_exp_list)
    health_perc_change = np.diff(health_exp_list) / health_exp_list[:-1] * 100
    health_max_exp_year = year[np.argmax(health_exp_list)]
    health_min_exp_year = year[np.argmin(health_exp_list)]
    health_avg_percent_change = np.mean(health_perc_change)


    health_text = "The graph illustrates the anticipated variations in healthcare expenses over the years based on fluctuations in inflation, assuming that the existing healthcare expenditure remains constant."
    health_text += f"The average expense over the period is {health_avg_exp:.2f} units. "
    health_text += f"The year where there is maximum expense is the year {health_max_exp_year}."
    health_text += f"The year where there is minimum expense is the year {health_min_exp_year}."
    health_text += f"The average percentage change between consecutive years is {health_avg_percent_change}%, indicating the growth rate of expense. "

    return health_text

def plot_misc_expense(year, misc_exp_list):
    plt.figure(figsize=(10, 6))
    plt.plot(year, misc_exp_list, label='Miscellaneous Expenses', marker='o', color='green')
    plt.xlabel('Year')
    plt.ylabel('Expense Amount')
    plt.title('Projected Miscellaneous Expenses Over Time')
    plt.legend()
    plt.grid(True)
    plt.savefig('graphs/misc_expenses_plot.png')
    
    misc_avg_exp = np.mean(misc_exp_list)
    misc_perc_change = np.diff(misc_exp_list) / misc_exp_list[:-1] * 100
    misc_max_exp_year = year[np.argmax(misc_exp_list)]
    misc_min_exp_year = year[np.argmin(misc_exp_list)]
    misc_avg_percent_change = np.mean(misc_perc_change)


    misc_text = "The graph illustrates the anticipated variations in miscellaneous expenses over the years based on fluctuations in inflation, assuming that the existing miscellaneous expenditure remains constant."
    misc_text += f"The average expense over the period is {misc_avg_exp:.2f} units. "
    misc_text += f"The year where there is maximum expense is the year {misc_max_exp_year}."
    misc_text += f"The year where there is minimum expense is the year {misc_min_exp_year}."
    misc_text += f"The average percentage change between consecutive years is {misc_avg_percent_change}%, indicating the growth rate of expense. "

    return misc_text




