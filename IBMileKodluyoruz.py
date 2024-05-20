import math

noktalar = [(1, 2), (3, 4), (5, 6), (7, 8)]  

def oklid_mesafesi(nokta1, nokta2):
    x1, y1 = nokta1
    x2, y2 = nokta2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

mesafeler = []
for i in range(len(noktalar)):
    for j in range(i + 1, len(noktalar)):
        mesafe = oklid_mesafesi(noktalar[i], noktalar[j])
        mesafeler.append(mesafe)

min_mesafe = min(mesafeler)
print("Minimum mesafe:", min_mesafe)
