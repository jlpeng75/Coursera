setwd("C:/Users/jpeng11/coursera")
course <- "Getting and Cleaning Data"
if(!file.exists(course)) {
    dir.create(course)
}

setwd(course)
fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv"
download.file(fileUrl, destfile = "IdahoHousing.csv")
dateDownloaded <- date()
dateDownloaded

dat <- read.csv("IdahoHousing.csv",header = T, stringsAsFactors = F)
names(dat)
head(dat$VAL); class(dat$VAL)
sum(dat$VAL==24, na.rm = T)

library(data.table)
library(xlsx)

sum(dat$VAL == 24, na.rm = T)

fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FDATA.gov_NGAP.xlsx"
download.file(fileUrl, destfile = "ngap2017.xlsx", mode = "wb" )
dat <- read.xlsx("ngap2017.xlsx", sheetIndex = 1, rowIndex=17:23, colIndex = 7:15)
sum(dat$Zip*dat$Ext,na.rm=T)

# Question 4
library(XML)
library(RCurl)

fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Frestaurants.xml"
xData <- getURL(fileUrl)
doc <- xmlTreeParse(xData, useInternalNodes =T)
rootNode <- xmlRoot(doc)
xmlName(rootNode)
names(rootNode)
xmlSApply(rootNode, xmlValue)
zip <- xpathSApply(rootNode, "//zipcode", xmlValue)
zip <- xpathSApply(doc, "//zipcode", xmlValue)

# question 5
library(data.table)
fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06pid.csv"
download.file(fileUrl, destfile = "IdahoHousing.csv")
DT <- fread("IdahoHousing.csv")
head(DT); class(DT)
mean(DT$pwgtp15,by=DT$SEX)
sapply(split(DT$pwgtp15,DT$SEX),mean)
system.time(mean(DT[DT$SEX==1,]$pwgtp15)); system.time(mean(DT[DT$SEX==2,]$pwgtp15))
system.time(tapply(DT$pwgtp15,DT$SEX,mean))
rowMeans(DT)[DT$SEX==1]; rowMeans(DT)[DT$SEX==2]
DT[,mean(pwgtp15),by=SEX]
