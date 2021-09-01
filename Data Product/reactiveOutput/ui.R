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
  titlePanel("censusVis"),
  
  # Sidebar with a slider input for number of bins 
  sidebarLayout(
    sidebarPanel(
       helpText("Create demographc maps with
                informaton from the 2010 US Census."),
       selectInput("var", 
                   label = "Choose a variable to display",
                   choices = c("Percent White",
                               "Percent Black",
                               "Percent Hispanic",
                               "Percent Asian"),
                   selected = "Percent White"),
       sliderInput("range",
                   label = "Range of interest:",
                   min = 0, max = 100, value = c(0,100))
    ),
    
    
    # Show a plot of the generated distribution
    mainPanel(
       textOutput("selected_var"),
       textOutput("selected_range")
    )
  )
))
