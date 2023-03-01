import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

path = "/Users/adam/Desktop/DataSci/Portfolio-v1/SATACT_Analysis/"
#---------------------------------- Data Import & Cleaning ----------------------------------
# 2017 SAT & ACT Data
act2017 = pd.read_csv(f"{path}data/act_2017.csv", encoding = "ISO-8859-1")
sat2017 = pd.read_csv(f"{path}data/sat_2017.csv", encoding = "ISO-8859-1")


# act2017.head(10)
# sat2017.head(10)
# act2017.tail(10)
# sat2017.tail(10)
# sat2017.info()
# act2017.info()
# sat2017.describe() 
# act2017.describe()
# sat2017.dtypes
# act2017.dtypes


def convert_participation_rate(rate_string):
    return float(rate_string[:-1])/100

act2017.Participation = act2017.Participation.apply(convert_participation_rate)
sat2017.Participation = sat2017.Participation.apply(convert_participation_rate)

act2017.loc[act2017.State == "Wyoming", "Composite"] = "20.2"
act2017.Composite = act2017.Composite.astype(float)


sat2017.rename(columns = {'State': 'state', 'Participation':'sat_participation_2017', 'Evidence-Based Reading and Writing': 'sat_reading_score_2017', 'Math':'sat_math_score_2017',
       'Total':'sat_total_2017'}, inplace=True)
act2017.rename(columns = {'State': 'state', 'Participation':'act_participation_2017', 'English': 'act_english_score_2017', 'Math':'act_math_score_2017','Reading':'act_reading_score_2017', 'Science':'act_science_score_2017', 'Composite':'act_composite_score_2017'}, inplace=True)
act2017.columns


act2017.drop(0, axis=0, inplace=True)
df = act2017.merge(sat2017, on="state")

df.to_csv("data\\combined_2017.csv")


#2018 SAT & ACT Data
act = pd.read_csv(f"{path}data/act_2017.csv", encoding = "ISO-8859-1")
sat = pd.read_csv(f"{path}data/sat_2018.csv", encoding = "ISO-8859-1")
act.drop_duplicates(inplace=True)
sat.describe()



act.Participation = act.Participation.apply(convert_participation_rate)
sat.Participation = sat.Participation.apply(convert_participation_rate)

sat.rename(columns = {'State': 'state', 'Participation':'sat_participation_2018', 'Evidence-Based Reading and Writing': 'sat_reading_score_2018', 'Math':'sat_math_score_2018',
       'Total':'sat_total_2018'}, inplace=True)
act.rename(columns = {'State': 'state', 'Participation':'act_participation_2018', 'English': 'act_english_score_2018', 'Math':'act_math_score_2018','Reading':'act_reading_score_2018', 'Science':'act_science_score_2018', 'Composite':'act_composite_score_2018'}, inplace=True)

df2018 = act.merge(sat, on="state")


# Combine  2017 & 2018 data into single dataframe 
final = df.merge(df2018, on="state")
final.to_csv("data\\final.csv")



# ---------------------------------- Exploratory Data Analysis (EDA) ----------------------------------

final.describe().T

#Calculate standard deviation

#def calc_std(arr):
   # return np.sqrt((1/len(arr)) * (arr-arr.mean())**2).sum()

#col_std = { col: calc_std(final[col]) for col in final.columns if col != 'state'}

#Investigating data trends
final.columns
for year in ["2017", "2018"]:
    for exam in ["sat_total_","act_composite_score_"]:
        col = exam + year
        print("#"+col)
        print(f"final.sort_values('{col}').head()")
        print(f"final.sort_values('{col}').tail()")
        print()

#final.sort_values('sat_participation_2017').head()
#final.sort_values('sat_participation_2017').tail()
#final.sort_values('act_participation_2017').head()
#final.sort_values('act_participation_2017').tail()
#final.sort_values('sat_participation_2018').head()
#final.sort_values('sat_participation_2018').tail()
#final.sort_values('act_participation_2018').head()
#final.sort_values('act_participation_2018').tail()

final.sort_values('sat_total_2017').head()
final.sort_values('sat_total_2017').tail()
final.sort_values('act_composite_score_2017').head()
final.sort_values('act_composite_score_2017').tail()

final.sort_values('sat_total_2018').head()
final.sort_values('sat_total_2018').tail()
final.sort_values('act_composite_score_2018').head()
final.sort_values('act_composite_score_2018').tail()

#Yr-to-yr rate change for states with 100% participation
high_participation = final[ ((final.act_participation_2017 == 1) & (final.act_participation_2018 != 1)) | 
                            ((final.act_participation_2017 != 1) & (final.act_participation_2018 == 1)) | 
                            ((final.sat_participation_2017 == 1) & (final.sat_participation_2018 != 1)) | 
                            ((final.sat_participation_2017 != 1) & (final.sat_participation_2018 == 1))]
#States with >50% participation on both tests either year?
final[  ((final.sat_participation_2017 > 0.5) & (final.sat_participation_2018 > 0.5)) | 
        ((final.act_participation_2017 > 0.5) & (final.act_participation_2018 > 0.5))]

final = final.apply(pd.to_numeric, errors='coerce')


# ---------------------------------- Data Visualization ----------------------------------

    # Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(final.corr())
plt.title("Correlation Matrix of ACT and SAT data: 2017 and 2018")
plt.show()

    # Histogram
def subplot_histograms(dataframe, list_of_columns, list_of_titles, list_of_xlabels):
    nrows = int(np.ceil(len(list_of_columns)/2)) # Makes sure you have enough rows
    fig, ax = plt.subplots(nrows=nrows, ncols=2) # You'll want to specify your figsize
    ax = ax.ravel() # Ravel turns a matrix into a vector, which is easier to iterate
    for i, column in enumerate(list_of_columns): # Gives us an index value to get into all our lists
        ax[i].hist(dataframe[column]) # feel free to add more settings
        ax[i].set_title(list_of_titles[i])
        ax[i].set_xlabel(list_of_xlabels[i])

    fig.tight_layout()

subplot_histograms( final, ["sat_participation_2017", "sat_participation_2018","act_participation_2017", "act_participation_2018"],                             ["SAT 2017", "SAT 2018","ACT 2017", "ACT 2018"], ["Participation", "Participation", "Particiaption", "Participation"])


subplot_histograms( final, ["sat_reading_score_2017", "sat_reading_score_2018","act_reading_score_2017"],                             ["SAT reading 2017", "SAT reading 2018", "ACT reading"], ["Score", "Score", "Score"])

subplot_histograms( final, ["sat_math_score_2017", "sat_math_score_2018","act_math_score_2017"],                             ["SAT Math 2017", "SAT Math 2018", "ACT Math"], ["Score", "Score", "Score"])


    # Scatterplots
#final.columns
plots = [   ("sat_math_score_2017", "act_math_score_2017", "SAT vs ACT: math 2017"),
            ("sat_reading_score_2017", 'act_reading_score_2017', "SAT vs ACT: reading 2017"),
            ("sat_total_2017", "act_composite_score_2017", "SAT vs. ACT total/composite scores for 2017"),
            ("sat_total_2017", "sat_total_2018", "Total scores for SAT 2017 vs. 2018"),
            ("act_composite_score_2017", "act_composite_score_2018", "Composite scores for ACT 2017 vs. 2018")]

fig, ax = plt.subplots(nrows=5, ncols=1, figsize=(6,24))
for i, (x,y,title) in enumerate(plots):
    final.plot.scatter(x,y, title=title, ax=ax[i])


fig.tight_layout()


    # Boxplots
plots = [   ("sat_math_score_2017", "act_math_score_2017", "SAT vs ACT: math 2017"),
            ("sat_reading_score_2017", 'act_reading_score_2017', "SAT vs ACT: reading 2017"),
            ("sat_total_2017", "act_composite_score_2017", "SAT vs. ACT total/composite scores for 2017"),
            ("sat_total_2017", "sat_total_2018", "Total scores for SAT 2017 vs. 2018"),
            ("act_composite_score_2017", "act_composite_score_2018", "Composite scores for ACT 2017 vs. 2018")]

fig, ax = plt.subplots(nrows=5, ncols=1, figsize=(6,24))
for i, (x,y,title) in enumerate(plots):
    final.plot.scatter(x,y, title=title, ax=ax[i])


fig.tight_layout()


# ---------------------------------- Summarizing Distributions ----------------------------------
for col in final.drop('state', axis=1).columns:
    output = f"""
    Stats for column: {col}
n = {len(final[col])}
---Central Tendency---
Mean: {final[col].mean()}
Median: {final[col].median()}
Mode(s)...
Value:  Occurances:
{final[col].value_counts()[final[col].value_counts().index.isin(final[col].mode())]}

---Spread---
Standard Deviation: {final[col].std()}

---Skew---
Skew: {final[col].skew()}"""
    
    print(output)