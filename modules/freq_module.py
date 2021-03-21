def freq(str):
    freq_obj = {}

    for i in str:
        if i in freq_obj:
            freq_obj[i] += 1
        else:
            freq_obj[i] = 1

    return freq_obj