##################################
# Görev 1
##################################
import seaborn as sns
import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()


["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]


[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]


og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()


df = sns.load_dataset("titanic")
df.head()
df.shape


df["sex"].value_counts()

df.nunique()

df["pclass"].unique()

df[["pclass", "parch"]].nunique()

df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype
df.info()

df[df["embarked"] == "C"].head(10)

df[df["embarked"] != "S"].head(10)


df[df["embarked"] != "S"]["embarked"].unique()

df[~(df["embarked"] == "S")]["embarked"].unique()

df[(df["age"] < 30) & (df["sex"] == "female")].head()

df[(df["fare"] > 500) | (df["age"] > 70)].head()

df.isnull().sum()

df.drop("who", axis=1, inplace=True)

type(df["deck"].mode())
df["deck"].mode()[0]
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df["deck"].isnull().sum()

df["age"].fillna(df["age"].median(), inplace=True)
df.isnull().sum()

df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]})


def age_30(age):
    if age < 30:
        return 1
    else:
        return 0


df["age_flag"] = df["age"].apply(lambda x: age_30(x))


df["age_flag"] = df["age"].apply(lambda x: 1 if x < 30 else 0)

df = sns.load_dataset("tips")
df.head()
df.shape

df.groupby("time").agg({"total_bill": ["sum", "min", "mean", "max"]})

df.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "mean", "max"]})

df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg(
    {
        "total_bill": ["sum", "min", "max", "mean"],
        "tip": ["sum", "min", "max", "mean"],
        "Lunch": lambda x: x.nunqiue(),
    }
)

df.loc[(df["size"] < 3) & (df["total_bill"] > 10), "total_bill"].mean()

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head()

new_df = df.sort_values("total_bill_tip_sum", ascending=False)[:30]
new_df.shape
