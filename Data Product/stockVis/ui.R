#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)

# Define UI for application that draws a histogram
shinyUI(fluidPage(
  
  # Application title
  titlePanel("stockVis"),
  
  # Sidebar with a slider input for number of bins 
  sidebarLayout(
    sidebarPanel(
       helpText("Select a stock to examine. Information
                will be collected from Yahoo finance."),
       textInput("symbol",
                   "Symbol", value = "SPY"),
       dateRangeInput("range", "Date Range",
                      start= "2013-01-01",
                      end = Sys.Date()),
       checkboxInput("log", "Plot y axis on log scale"),
       checkboxInput("adjust", "Adjust prices for inflation")
    ),
    
    # Show a plot of selected stock
    mainPanel(
       plotOutput("price") 
      # plotOutput("price")
    )
  )
))
