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
