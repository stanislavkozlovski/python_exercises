"""
Реализирайте програма, която да конвертира сума от подадена валута към български лева (BGN). Резултатите трябва да се закръглят до втория знак след десетичната запетая.

Входни данни:

име на файл, съдържащ обменни курсове на различни валути към BGN; Празните редове във файла не бива да се обработват;
име на файл, съдържащ на всеки ред сума и валута, в която е сумата; Празните редове във файла не бива да се обработват; Имайте предвид, че в този файл ще има по няколко суми от една и съща валута;
Очакван изход: За всеки ред от файла със сумите, трябва да бъде изведена на отделен ред съответната сума в български лева.

Ако в някой от двата файла има невалидни данни, трябва да изведете като резултат само INVALID INPUT.
"""
try:
    INDEX_ER_CURRENCY_NAME = 0
    INDEX_ER_EXCHANGE_RATE = 1
    INDEX_AR_AMOUNT = 0
    INDEX_AR_NAME = 1

    exchange_rates_file_name = input()
    amounts_file_name = input()

    # get exchange rates first, store them in a dictionary ex: {key:USD, value: 0.542}
    exchange_rates = {}  # type: dict

    with open(exchange_rates_file_name) as er_reader:
        for line in er_reader:
            line_info = line.split()

            if line_info:
                currency_name = line_info[INDEX_ER_CURRENCY_NAME]
                ex_rate = float(line_info[INDEX_ER_EXCHANGE_RATE])

                exchange_rates[currency_name] = ex_rate

    with open(amounts_file_name) as amount_reader:
        for line in amount_reader:
            line_info = line.split()

            if line_info:
                amount = float(line_info[INDEX_AR_AMOUNT])
                cur_name = line_info[INDEX_AR_NAME]

                print("{:.2f}".format(amount/exchange_rates[cur_name]))
except Exception:
    print("INVALID INPUT")




