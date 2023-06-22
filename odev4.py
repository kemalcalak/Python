#########
# Görev 1
#########

# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
import pandas as pd

pd.set_option("display.max_rows", None)
df = pd.read_csv(
    "Modül_1_Veri_Bilimi_için_Python_Programlama/Part_2_Veri_Bilimi_için_Python_Programlama/Kural_Tabanli_Siniflandirma/persona.csv"
)
df.head()
df.shape
df.info()

# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?
df["SOURCE"].nunique()
df["SOURCE"].value_counts()

# Soru 3: Kaç unique PRICE vardır?
df["PRICE"].nunique()

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
df["PRICE"].value_counts()

# Soru 5: Hangi ülkeden kaçar tane satış olmuş?
df["COUNTRY"].value_counts()
df.groupby("COUNTRY")["PRICE"].count()

df.pivot_table(values="PRICE", index="COUNTRY", aggfunc="count")

# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("COUNTRY")["PRICE"].sum()
df.groupby("COUNTRY").agg({"PRICE": "sum"})

df.pivot_table(values="PRICE", index="COUNTRY", aggfunc="sum")

# Soru 7: SOURCE türlerine göre göre satış sayıları nedir?
df["SOURCE"].value_counts()

# Soru 8: Ülkelere göre PRICE ortalamaları nedir?
df.groupby(by=["COUNTRY"]).agg({"PRICE": "mean"})

# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?
df.groupby(by=["SOURCE"]).agg({"PRICE": "mean"})

# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
df.groupby(by=["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})

#########
# GÖREV 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
#########

df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).head()

#########
# GÖREV 3: Çıktıyı PRICE'a göre sıralayınız.
#########

agg_df = (
    df.groupby(by=["COUNTRY", "SOURCE", "SEX", "AGE"])
    .agg({"PRICE": "mean"})
    .sort_values("PRICE", ascending=False)
)
agg_df.head()

##########
# GÖREV 4: Indekste yer alan isimleri değişken ismine çeviriniz.
##########

agg_df = agg_df.reset_index()
agg_df.head()

##########
# GÖREV 5: AGE değişkenini kategorik değişkene çeviriniz ve agg_df'e ekleyiniz.
##########

bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]
mylabels = ["0_18", "19_23", "24_30", "31_40", "41_" + str(agg_df["AGE"].max())]
agg_df["age_cat"] = pd.cut(agg_df["AGE"], bins, labels=mylabels)
agg_df.head()

###########
# GÖREV 6: Yeni level based müşterileri tanımlayınız ve veri setine değişken olarak ekleyiniz.
###########

agg_df.columns
for row in agg_df.values:
    print(row)
[
    row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper()
    for row in agg_df.values
]
agg_df["customers_level_based"] = [
    row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper()
    for row in agg_df.values
]
agg_df.head()
agg_df = agg_df[["customers_level_based", "PRICE"]]
agg_df.head()
for i in agg_df["customers_level_based"].values:
    print(i.split("_"))
agg_df["customers_level_based"].value_counts()
agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})
agg_df = agg_df.reset_index()
agg_df.head()
agg_df["customers_level_based"].value_counts()
agg_df.head()

############
# GÖREV 7: Yeni müşterileri (USA_ANDROID_MALE_0_18) segmentlere ayırınız.
############
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT").agg({"PRICE": "mean"})

############
# GÖREV 8: Yeni gelen müşterileri sınıflandırınız ne kadar gelir getirebileceğini tahmin ediniz.
############
new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]
new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]
