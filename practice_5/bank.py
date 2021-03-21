def sum_in_bank(size, percent, period):
    """Функция расчета денежных средств в банке

    Keyword arguments:
    size -- размер взноса
    percent -- банковский процент
    period -- срок накоплений
    """
    while period:
        size += size / 100*percent
        period -= 1
    return size

print(sum_in_bank(1000, 10, 1))
