#############
# GÖREV 1
#############

# Soru 1: miuul_gezinomi.xlsx dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
import pandas as pd

pd.set_option("display.max_columns", None)
df = pd.read_excel("dataset/miuul_gezinomi.xlsx")
pd.set_option("display.float_format", lambda x: "%.2f" % x)
print(df.head())
print(df.shape)
print(df.info())

# Soru 2: Kaç unique şehir vardır? Frekansları nedir?
print(df["SaleCityName"].nunique())
print(df["SaleCityName"].value_counts())

# Soru 3: Kaç unique Concept vardır?
df["ConceptName"].nunique()

# Soru 4: Hangi Concept'dan kaçar tane satış gerçekleşmiş?k
df["ConceptName"].value_counts()

# Soru 5: Şehirlere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("SaleCityName").agg({"Price": "sum"})

# Soru 6: Concept türlerine göre göre ne kadar kazanılmış?
df.groupby("ConceptName").agg({"Price": "sum"})

# Soru 7: Şehirlere göre PRICE ortalamaları nedir?
df.groupby(by=["SaleCityName"]).agg({"Price": "mean"})

# Soru 8: Conceptlere  göre PRICE ortalamaları nedir?
df.groupby(by=["ConceptName"]).agg({"Price": "mean"})

# Soru 9: Şehir-Concept kırılımında PRICE ortalamaları nedir?
df.groupby(by=["SaleCityName", "ConceptName"]).agg({"Price": "mean"})

#############
# GÖREV 2: satis_checkin_day_diff değişkenini EB_Score adında yeni bir kategorik değişkene çeviriniz.
#############

bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=labels)
df.head(50).to_excel("eb_scorew.xlsx", index=False)

#############
# GÖREV 3:Şehir,Concept, [EB_Score,Sezon,CInday] kırılımında ücret ortalamalarına ve frekanslarına bakınız
#############

df.groupby(by=["SaleCityName", "ConceptName", "EB_Score"]).agg(
    {"Price": ["mean", "count"]}
)
df.groupby(by=["SaleCityName", "ConceptName", "Seasons"]).agg(
    {"Price": ["mean", "count"]}
)
df.groupby(by=["SaleCityName", "ConceptName", "CInDay"]).agg(
    {"Price": ["mean", "count"]}
)

#############
# GÖREV 4:City-Concept-Season kırılımın çıktısını PRICE'a göre sıralayınız.
#############

agg_df = (
    df.groupby(["SaleCityName", "ConceptName", "Seasons"])
    .agg({"Price": "mean"})
    .sort_values("Price", ascending=False)
)
agg_df.head(20)

#############
# GÖREV 5: Indekste yer alan isimleri değişken ismine çeviriniz.
#############

agg_df.reset_index(inplace=True)
agg_df.head()

#############
# GÖREV 6:Yeni level based satışları tanımlayınız ve veri setine değişken olarak ekleyiniz.
#############

agg_df["sales_level_based"] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(
    lambda x: "_".join(x).upper(), axis=1
)

#############
# GÖREV 7:Personaları segmentlere ayırınız.
#############

agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], 4, labels=["D", "C", "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT").agg({"Price": ["mean", "max", "sum"]})

#############
# GÖREV 8: Oluşan son df'i price değişkenine göre sıralayınız.
#############

agg_df.sort_values(by="Price")
new_user = "ANTALYA_HERŞEY DAHIL_HIGH"
agg_df[agg_df["sales_level_based"] == new_user]
