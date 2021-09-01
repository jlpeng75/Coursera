setwd("C:/Users/jpeng11/coursera/Getting and Cleaning Data")
library(stringr)
fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv"
download.file(fileUrl, destfile = "IdahoHousing.csv")
dat <- read.csv("IdahoHousing.csv", header = T, stringsAsFactors = F)
strsplit(names(dat), split = "wgtp")[123]


# Question 2

fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FGDP.csv"
download.file(fileUrl, destfile = "gdp.csv")
dat <- read.csv("gdp.csv", header = T, stringsAsFactors = F, skip = 4)
dat <- 
    dat %>% filter(as.numeric(X.1) %in% 1:190)

names(dat); head(dat); dat$X.1
gdp <- gsub(",", "", dat$X.4)
length(gdp)
dim(dat)
mean(as.numeric(gdp), na.rm = T)

grep("^United", dat$X.3)

# Question 4

fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FEDSTATS_Country.csv"
download.file(fileUrl, destfile = "education.csv")
edu <- read.csv("education.csv", stringsAsFactors = F, header = T )
head(edu); names(edu)
dat2 <- merge(dat, edu, by.x = "X", by.y = "CountryCode", all.x = F)
sum(grepl("Fiscal year end:( )* June", dat2$Special.Notes))
dat2[grepl("Fiscal year end:( )* June", dat2$Special.Notes), ]


# Question 4

library(quantmod)
amzn = getSymbols("AMZN",auto.assign=FALSE)
sampleTimes = index(amzn)

library(lubridate)

class(sampleTimes)
sum(year(sampleTimes)== 2012); sum(year(sampleTimes)== 2012 & wday(sampleTimes, label = T) == "Mon")