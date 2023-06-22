notlar = [90, 80, 70, 50]
type(notlar)

liste = ["a", 19.3, 90]
list_genis = ["a", 19.3, 90, notlar]

len(list_genis)

list_genis[0]
list_genis[1]
list_genis[3]

type(list_genis[3])

tum_liste = [liste, list_genis]

# del tum_liste

# Listeler - Eleman Islemleri


liste = [10, 20, 30, 40, 50]

liste[0]
liste[1]

liste[6]

liste[0:2]

liste[:2]

liste[2:]

yeni_liste = ["a", 10, [20, 30, 40, 50]]
yeni_liste

yeni_liste[2]

yeni_liste[0:2]

yeni_liste[2][1]

# Listeler - Eleman Degistirme

liste = ["ali", "veli", "berkcan", "ayse"]
liste

liste[1] = "velinin_babasi"

liste

liste[1] = "veli"

liste[0:3] = "alinin_babasi", "velinin_babasi", "berkcanin_babasi"

liste

liste = ["ali", "veli", "berkcan", "ayse"]
liste

liste = liste + ["kemal"]
liste

# del liste[2]
liste

# Listeler - Liste Metodları

liste = ["ali", "veli", "isik"]

dir(liste)

liste

# append & remove

liste.append("berkcan")

liste

liste.remove("berkcan")
liste

# insert

liste = ["ali", "veli", "isik"]

liste

liste.insert(0, "ayse")

liste

liste = ["ali", "veli", "isik"]

liste[0] = "ayse"

liste

liste.insert(0, "ayse")
liste

liste[1] = "ali"

liste

liste.insert(2, "mehmet")
liste

liste.insert(5, "berk")
liste

len(liste)


liste.insert(len(liste), "beren")
liste

# pop


liste.pop(0)
liste

liste.pop(4)
liste

# count

liste = ["ali", "veli", "isik", "ali", "veli"]

liste.count("ali")
liste.count("veli")
liste.count("isik")

# copy

liste_yedek = liste.copy()

# extend

liste.extend(["a", "b", 10])
liste

# index()

liste.index("ali")

# reverse()

liste.reverse()
liste

# sort()

liste = [10, 40, 5, 90]
liste.sort()
liste

# clear

liste.clear()
liste
