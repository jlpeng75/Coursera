# question 1:
library(httr)
library(jsonlite)
fileUrl <- "https://api.github.com/users/jtleek/repos"
oauth_endpoints("github")

myapp <- oauth_app("github",
                   key = "90c3666056c30c2b03d7",
                   secret = "ff49760b9f7aa5a1d2a690a27de468e34eeddc3b"
)

github_token <- oauth2.0_token(oauth_endpoints("github"), myapp)

gtoken <- config(token = github_token)
req <- GET("https://api.github.com/users/jtleek/repos", gtoken)
stop_for_status(req)
content(req)
dat <- fromJSON(content(req))
names(content(req))
content(req)[[1]]
names(content(req)[[1]])
class(content(req)[[1]])
content(req)[[1]]$name
xpathSApply(content(req), "//name", xmlValue)
json2 = jsonlite::fromJSON(toJSON(content(req)))
json2
names(json2)
json2[json2$name == "datasharing",]$created_at

# question 2:
library(data.table); library(sqldf)
fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06pid.csv"
download.file(fileUrl, destfile = "acs.csv")
acs <- fread("acs.csv")
sqldf("select pwgtp1 from acs where AGEP < 50")

sqldf("select distinct AGEP from acs")

# question 4:

con <- "http://biostat.jhsph.edu/~jleek/contact.html"
    

doc <- readLines(con)

class(doc)
nchar(doc)

# question 5:

fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fwksst8110.for"

dat <- read.fwf("https://d396qusza40orc.cloudfront.net/getdata%2Fwksst8110.for", 
                c(12, 7, 4, 9, 4, 9, 4, 9, 4), skip = 4)
head(dat)
sum(dat$V4, na.rm = T)

