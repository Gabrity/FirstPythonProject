# In many of the cases I assume that the input contains only a single portfolio as in the example file. A solution that
# works with multiple portfolios in the input could be created with smaller effort from the current solution.

def perform_tasks(instruments):
    perform_task_1(instruments)
    #perform_task_2(instruments)
    #perform_task_3(instruments)
    #perform_task_4(instruments)


def perform_task_1(instruments):
    perform_task_1_b(instruments)


def perform_task_1_b(instruments):
    # b) Calculate the total portfolio value in CHF.
    sum = 0.0
    for instrument in instruments:
        fx_rate = get_fx_rate(instrument.QuotationCurrency_21, "CHF")
        sum += fx_rate * instrument.PositionValueQc_22
    print("Total portfolio value in CHF: %f" % sum)



def perform_task_2(instruments):
    pass


def perform_task_3(instruments):
    pass


def perform_task_4(instruments):
    pass

# Minimalistic currency converter method for the sake of simplicity
# Also, using enums would be a nice feature
def get_fx_rate(from_currency, to_currency):
    if (from_currency == "USD") & (to_currency == "USD"):
        return 1.0
    if (from_currency == "CHF") & (to_currency == "CHF"):
        return 1.0
    if (from_currency == "CHF") & (to_currency == "USD"):
        return 0.99726
    if (from_currency == "USD") & (to_currency == "CHF"):
        return 1.00238
    raise ValueError("One of these currencies are unknown: %s, %s" % from_currency % to_currency)
