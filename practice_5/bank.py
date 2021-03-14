def sum_in_bank(size, percent, period):
    while period:
        size += size/100*percent
        period -= 1
    return size

print(sum_in_bank(1000, 10, 1))
