# Tuple Olusturma

t = ("ali", "veli", 1, 2, 3.2, [1, 2, 3, 4])

t = "ali", "veli", 1, 2, 3.2, [1, 2, 3, 4]

# tuple()

t = ("eleman",)
type(t)

# Tuple Eleman Islemleri

t = ("ali", "veli", 1, 2, 3, [1, 2, 3, 4])
t

t[1]
t[0:3]

t[2] = 99

# Veri Yapıları - Dictionary (Sözlük)


# Sozluk Olusturma
sozluk = {
    "REG": "Regresyon Modeli",
    "LOJ": "Lojistik Regresyon",
    "CART": "Classification and Reg",
}

sozluk

len(sozluk)


sozluk = {"REG": 10, "LOJ": 20, "CART": 30}

sozluk


sozluk = {"REG": ["RMSE", 10], "LOJ": ["MSE", 20], "CART": ["SSE", 30]}

sozluk

# Sozluk Eleman Islemleri

sozluk = {
    "REG": "Regresyon Modeli",
    "LOJ": "Lojistik Regresyon",
    "CART": "Classification and Reg",
}


sozluk[0]

sozluk["REG"]
sozluk["LOJ"]

sozluk = {"REG": ["RMSE", 10], "LOJ": ["MSE", 20], "CART": ["SSE", 30]}


sozluk["REG"]

sozluk = {
    "REG": {"RMSE": 10, "MSE": 20, "SSE": 30},
    "LOJ": {"RMSE": 10, "MSE": 20, "SSE": 30},
    "CART": {"RMSE": 10, "MSE": 20, "SSE": 30},
}

sozluk
sozluk["REG"]["SSE"]

# Sozluk - Eleman Eklemek & Degistirmek

sozluk = {
    "REG": "Regresyon Modeli",
    "LOJ": "Lojistik Regresyon",
    "CART": "Classification and Reg",
}

sozluk["GBM"] = "Gradient Boosting Mac"
sozluk

sozluk["REG"] = "Coklu Dogrusal Regresyon"
sozluk

sozluk[1] = "Yapay Sinir Aglari"

sozluk

l = [1]
l

sozluk[l] = "yeni bir sey"

t = ("tuple",)

sozluk[t] = "yeni bir sey"
sozluk

# Veri Yapilari - Setler

# Set olusturmak

s = set()
s

l = [1, "a", "ali", 123]
s = set(l)
s


t = ("a", "ali")

s = set(t)
s

ali = "lutfen_ata_bak ma_uza ya_git"
type(ali)

s = set(ali)
s

l = ["ali", "lutfen", "ata", "bakma", "uzaya", "git", "git", "ali", "git"]

l

s = set(l)
s

len(s)

l[0]

s[0]


# Eleman ekleme & cikarma

l = ["gelecegi", "yazanlar"]

s = set(l)

s

dir(s)

s.add("ile")
s

s.add("gelecege_git")
s

s.add("ile")
s

s.remove("ali")
s

s.discard("ali")
