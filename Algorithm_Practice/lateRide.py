def lateRide(n):
    hours = n // 60
    minutes = n - (hours * 60)
    new_string = "{}{}".format(hours, minutes)
    total = [int(num) for num in new_string]
    return sum(total)
