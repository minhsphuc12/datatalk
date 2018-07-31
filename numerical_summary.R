library(tidyverse)

data_folder = 'C:\\Users\\Nasdap\\Documents\\git\\datatalk\\titanic'

train = as.tibble(import(paste0(data_folder,'\\train.csv')))
test = as.tibble(import(paste0(data_folder,'\\test.csv')))
gender_class = as.tibble(import(paste0(data_folder,'\\gender_submission.csv')))

train

test

gender_class

#test and gender_class have same length. So they probably belong together.

# Kaggle description also confirmed that.
# We also include gender_submission.csv, a set of predictions that assume all and only female passengers survive, as an example of what a submission file should look like.

# if you haven't already know what train and test is, don't be worry. At this point, you only need to know that the whole data at hand is splitted into train and test set. 

# for the sake of EDA, we will combine two data frame.

test_full = test %>% left_join(gender_class)
data_full = union_all(train, test_full)

data_full

# >>>>>>> SOLVE Structure: a simple process to explore a dataset numerically. 
## 1. Size (S)
## 2. Key Observation (O)
## 3. Length (L)
## 4. Distribution along Variables (V)
## 5. Question Data Validity (E)

# Numerical Summary Structure
## 1. Size (S)
## 1. First, check how many variables exists?
str(data_full)
colnames(data_full)

## 2. Key Observation (O)
## 2. Second, is there any variable serving as observation key? Quickest way is finding any variable with name contains "ID".

colnames(data_full)[grepl('id', tolower(colnames(data_full)))]

length(unique(data_full$PassengerId)) == length(data_full$PassengerId)

## 3. Length (L)
## 3. Third, check how many observation in the set. Is that all? Check the source manually so there is no data has not been read yet.

# our dataset has 1309 observations, is this whole passenger count?
# https://titanicfacts.net/titanic-passengers/
# 1,317 – the approximate number of passengers actually on board.
# 324 – the number of first class passengers on board.
# 284 – the number of second class passengers.
# 709 – the number of third class passengers.
# 107 – the number of children travelling, mainly travelling in third class

first_class = data_full %>% filter(Pclass == 1)
# 323 passengers in dataset, vs. 324 in the source, not bad.

## 4. Distribution along Variables (V)
## 4. Forth, for categorical, check count for each category; for continuous, check distribution parameters.
summary(data_full)

table(data_full$Pclass)
table(data_full$Sex)
table(data_full$SibSp)
table(data_full$Parch)
table(data_full$Embarked)

table(data_full$Cabin)
# this Cabin variable has a lot of value in raw form, so it need to be recoded somehow to be informative. 
# This is what called "FEATURE ENGINEERING" later.

## 5. Question Data Validity (E)
## 5. Last, ae doubtful, as data can be missing / wrong input / cooked / etc.
table(data_full$Pclass, useNA = 'ifany')
table(data_full$Sex, useNA = 'ifany')
table(data_full$SibSp, useNA = 'ifany')
table(data_full$Parch, useNA = 'ifany')
table(data_full$Embarked, useNA = 'ifany')

# we see that Age variable has 263 missing observations, let's find out if Age has been systematically missing, or by random chance.

data_full_age = data_full %>%
  mutate(age_missing = is.na(Age))

table(data_full_age$age_missing, data_full_age$Pclass)
# missing age happens at high percentag of 3rd class, but also happens in small percentage of 1st and 2nd classes. 
# Pclass is both categorical and numerical 
table(data_full_age$age_missing, data_full_age$Embarked)
# missing age has no clear correlation with departure location, so it has nothing to do with recording system.
cor(data_full_age %>% select(c(age_missing, Fare, Pclass, SibSp, Parch, Survived)), method = "pearson", use = "complete.obs")
# age missing change increase when Fare decrease, higher class (lower class quality), and no significant correlation with number of relatives and survival chance.


