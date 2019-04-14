# In many of the cases I assume that the input contains only a single portfolio as in the example file. A solution that
# works with multiple portfolios in the input could be created with some effort from the current solution.


def perform_tasks(instruments):
    portfolio_value_usd = perform_task_1(instruments)
    perform_task_2(instruments, portfolio_value_usd)
    # perform_task_3(instruments)
    # perform_task_4(instruments)


def perform_task_1(instruments):
    portfolio_value_usd = perform_task_1_b(instruments)
    perform_task_1_a(instruments, portfolio_value_usd)
    return portfolio_value_usd


def perform_task_1_a(instruments, sum_usd):
    # a) The following columns of the report were deleted:
    # 5_Portfolio-TotalNetAssets
    # 8b_Portfolio-ShareClass-TotalNumberOfShares
    # Calculate the missing values.
    number_of_shares = sum_usd / instruments[0].Portfolio_SharePrice_8
    for instrument in instruments:
        # even though we know that portfolio currency is USD, this would convert it if was different
        instrument.Portfolio_TotalNetAssets_5_output = convert_value_to_other_currency(sum_usd, "USD",
                                                                                       instrument.PortfolioCurrency_4)
        instrument.Portfolio_TotalNumberOfShares_8b_output = number_of_shares


def perform_task_1_b(instruments):
    # 1 b) Calculate the total portfolio value in CHF.
    sum_usd = 0.0
    for instrument in instruments:
        fx_rate = get_fx_rate(instrument.QuotationCurrency_21, "USD")
        sum_usd += fx_rate * instrument.PositionValueQc_22
    sum_in_chf = convert_value_to_other_currency(sum_usd, "USD", "CHF")
    print("Total value in portfolio %s CHF: %f" % (instruments[0].PortfolioID_1, sum_in_chf))
    return sum_usd


def perform_task_2(instruments, portfolio_value_usd):
    cash_value_usd = perform_task_2_a(instruments)
    perform_task_2_b(instruments)
    portfolio_cash_percentage = cash_value_usd / portfolio_value_usd * 100
    perform_task_2_c(instruments, portfolio_cash_percentage)


def perform_task_2_a(instruments):
    # 2 a) What is the total value of the cash items in USD?
    sum_usd = 0.0
    for instrument in instruments:
        if instrument.PositionInstrumentCIC_12 == "XT71":
            position_value = instrument.PositionValueQc_22
            sum_usd += convert_value_to_other_currency(position_value, instrument.QuotationCurrency_21, "USD")
    print("Cash instrument value in portfolio %s is %f USD" % (instruments[0].PortfolioID_1, sum_usd))
    return sum_usd


def perform_task_2_b(instruments):
    # 2 b) What is the currency distribution in the portfolio in percentage?
    # Here we assume that the task is to calculate the currency distribution of CASH instruments
    sum_of_chf = collect_cash_values_of_same_currency(instruments, "CHF")
    sum_of_usd = collect_cash_values_of_same_currency(instruments, "USD")

    # To be able to compare, we convert both sums to the same currency
    currency_of_portfolio = instruments[0].PortfolioCurrency_4
    chf_in_portfolio_currency = convert_value_to_other_currency(sum_of_chf, "CHF", currency_of_portfolio)
    usd_in_portfolio_currency = convert_value_to_other_currency(sum_of_usd, "USD", currency_of_portfolio)
    chf_percentage = chf_in_portfolio_currency / (chf_in_portfolio_currency + usd_in_portfolio_currency) * 100
    usd_percentage = usd_in_portfolio_currency / (chf_in_portfolio_currency + usd_in_portfolio_currency) * 100
    print("CHF-USD percentage for cash instruments in portfolio %s is CHF: %f%% USD: %f%%"
          % (instruments[0].PortfolioID_1, chf_percentage, usd_percentage))


def perform_task_2_c(instruments, portfolio_cash_percentage):
    # 2 c) Please also fill the 9_Portfolio-CashPercentage column!
    # Instrument object is filled with the required data which is later written to the excel file
    for instrument in instruments:
        instrument.PortfolioCashPercentage_9_output = portfolio_cash_percentage


def perform_task_3(instruments):
    pass


def perform_task_4(instruments):
    pass


def collect_cash_values_of_same_currency(instruments, currency):
    result = 0.0
    for instrument in instruments:
        if (instrument.QuotationCurrency_21 == currency) & (instrument.PositionInstrumentCIC_12 == "XT71"):
            result += instrument.PositionValueQc_22
    return result


def convert_value_to_other_currency(original_amount, original_currency, target_currency):
    return get_fx_rate(original_currency, target_currency) * original_amount


# Minimalistic currency converter method for the sake of simplicity
# Also, using enums would be a nice feature
def get_fx_rate(from_currency, to_currency):
    if (from_currency == "USD") & (to_currency == "USD"):
        return 1.0
    if (from_currency == "CHF") & (to_currency == "CHF"):
        return 1.0
    if (from_currency == "CHF") & (to_currency == "USD"):
        # Using some recent spot rates
        return 0.99726
    if (from_currency == "USD") & (to_currency == "CHF"):
        return 1.00238
    raise ValueError("One of these currencies are unknown: %s, %s" % from_currency % to_currency)
