def caltotal(marks):
    return sum(marks)

def calpercentage(total):
    return (total / 500) * 100

def calgrade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"

def highest(marks):
    return max(marks)

def lowest(marks):
    return min(marks)