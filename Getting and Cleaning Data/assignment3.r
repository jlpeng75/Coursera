setwd("C:/Users/jpeng11/coursera/Getting and Cleaning Data")
library(dplyr); library(tidyr)
# Question 1:
fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv"
download.file(fileUrl, destfile = "IdahoHousing.csv")
dat <- read.csv("IdahoHousing.csv", header = T, stringsAsFactors = F)
dat1 <- tbl_df(dat)
class(dat); class(dat1)
q1 <- dat1 %>% 
    mutate(agricultureLogical = ifelse(AGS == 6 & ACR == 3, TRUE, FALSE))
    
which(q1$agricultureLogical)

# Question 2

fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fjeff.jpg"
download.file(fileUrl, destfile = "Jeff.jpg", mode = 'wb')
dat <- readJPEG("Jeff.jpg", native = T)
quantile(dat, probs = c(0.3, 0.8))

# Question 3:

fileUrl1 <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FGDP.csv"
fileUrl2 <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FEDSTATS_Country.csv"
download.file(fileUrl1, destfile = "GDP.csv")
download.file(fileUrl2, destfile = "Education.csv")
dat1 <- read.csv("GDP.csv", header = T, stringsAsFactors = F, skip = 4)
dat2 <- read.csv("Education.csv", header = T, stringsAsFactors = F)
names(dat1) ; names(dat2)
head(dat1); head(dat2)

dat <- merge(dat1, dat2, by.x = "X", by.y = "CountryCode" )
summary(dat); head(dat)

dim(dat)
dat <- tbl_df(dat)
dat <- dat[dat$X.1 != "",]
dat
dat <- dat %>%
    filter(dat$X.1 != "") %>%
    arrange(desc(as.numeric(X.1)))
dat[1:13, 1:10]
dat$X.4 <- as.numeric(gsub("[,]", "", dat$X.1))
# Question 5

dat$X.1 <- as.numeric(dat$X.1)

GDP_group <- dat %>%
    group_by(Income.Group) %>%
    summarise(mean(X.1))

# Question 5

dat_cut <- cut2(dat$X.1, g = 5 )

table(dat_cut, dat$Income.Group)