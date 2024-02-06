setwd("N:/Projects/Spring2024Datathon")
starbucks <- read.csv("StarbucksDatathonFile.csv")
head(starbucks)
summary(starbucks)
unique(starbucks$Beverage_category)
unique(starbucks$Beverage)

dunkin <- read.csv("Dunkin.csv")
head(dunkin)
summary(dunkin)
unique(dunkin$Item.Category)

hotcoffee <- dunkin[dunkin$Item.Category=="Hot Coffee", ]
head(hotcoffee)

coffee <- starbucks[starbucks$Beverage_category=="Coffee", ]
head(coffee)

# Numbers of rows
nrow(coffee)
nrow(hotcoffee)

nrow(dunkin)
nrow(dunkin[dunkin$Item.Category=="Hot Espresso", ])
nrow(dunkin[dunkin$Item.Category=="Hot Cappuccino", ])
nrow(dunkin[dunkin$Item.Category=="Hot Latte", ])
nrow(dunkin[dunkin$Item.Category=="Hot Macchiato", ])
nrow(dunkin[dunkin$Item.Category=="Hot Americano", ])
nrow(starbucks)
nrow(starbucks[starbucks$Beverage_category=="Classic Espresso Drinks", ])
nrow(starbucks[starbucks$Beverage_category=="Signature Espresso Drinks", ])


mean(coffee$Total.Fat..g.)

# Hypothesis, what has lower fat, a Dunkin Cappuchino or a Starbucks Classic Espresso

starbucks_espresso = starbucks[starbucks$Beverage_category=="Signature Espresso Drinks", ]
dunkin_cappu = dunkin[dunkin$Item.Category=="Hot Cappuccino", ]


colors_vector <- c("#1f78b4", "#33a02c", "#e31a1c", "#ff7f00", "#6a3d9a",
                   "#b15928", "#a6cee3", "#b2df8a", "#fb9a99", "#fdbf6f",
                   "#cab2d6", "#ffff99", "#b15928", "#8dd3c7", "#bebada")


install.packages("devtools")
library(devtools)
devtools::install_github("janish-parikh/ZTest")
library(HypothesisTesting)

head(dunkin_cappu)
summary(dunkin_cappu)

tapply(dunkin_cappu$Total.Sugars..g., dunkin_cappu$Serving.Size, mean)
barplot(tapply(dunkin_cappu$Total.Sugars..g., dunkin_cappu$Serving.Size, mean), main = "Mean sugar of different serving sizes in Dunkin Cappuchinos", xlab = "Serving Sizes", ylab = "Mean Sugar", col = colors_vector )

head(starbucks_espresso)
summary(starbucks_espresso)
tapply(starbucks_espresso$Sugars..g., starbucks_espresso$Beverage_prep, mean)
barplot(tapply(starbucks_espresso$Sugars..g., starbucks_espresso$Beverage_prep, mean)
, main = "Mean sugar of different serving preparation in Starbucks Classic Espressos", xlab = "Serving Sizes", ylab = "Mean Sugar", col = colors_vector )
