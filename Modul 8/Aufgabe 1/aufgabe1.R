#Statische Datenanalyse von Mergelproben

#load libraries
library("e1071") #kurtosis

#read in data
setwd("C:/Users/selin/Desktop/uni/Modul 8/Aufgabe 1/ass1_geostat")

mergel_proben <- read.table("GeoChem_rev.dat", header = TRUE)



# Create a sample 7-column data frame
df <- mergel[, 1:7]  # just as an example

# Use sapply to compute basic stats
uebersicht_tabelle <- data.frame(
    Variable = colnames(df),
    Mean = sapply(df, mean),
    SD = sapply(df, sd),
    Min = sapply(df, min),
    Max = sapply(df, max),
    Median = sapply(df, median)
)

print(uebersicht_tabelle)