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
  titlePanel("Basic widgets"),
  
  #
  fluidRow(
      
      column(3,
             h3("Buttons"),
             actionButton("action", "Action"),
             br(),
             br(),
             submitButton("Submit")),
      column(3,
             h3("Single checkbox"),
             checkboxInput("checkbox", "Choice A", value = TRUE)),
      column(3,
             checkboxGroupInput("checkGroup",
                                h3("Checkbox group"),
                                choices = list("Choice 1" = 1,
                                               "Choice 2" = 2,
                                               "Choice 3" = 3),
                                selected = 1)),
      column(3, dateInput("date",
                          h3("Date input"),
                          value = "2014-01-01"))
  ),
  
  fluidRow(
      
      column(3, 
             dateRangeInput("dates", h3("Date range"))),
      column(3,
             fileInput("file", h2("File input"))),
      column(3,
             h3("Help text"),
             helpText("Note: help text isn't a true widget,",
                      "but it provides an easy way to add text to",
                      "accompany other widgets.")),
      column(3,
             numericInput("num",
                          h3("Numeric Input"),
                          value = 1))
  ),
  
  fluidRow(
      
      column(3, 
             radioButtons("radio", h3("Radio buttons"),
                          choices = list("Choice 1" = 1, "Choice 2" = 2,
                                         "Choice 3" = 3), 
                          selected = 1)),
      column(3,
             selectInput("select", h3("Select box"),
                         choices = list("Choice 1" = 1, "Choice 2" = 2,
                                        "Choice 3" = 3),
                         selected = 1)),
      column(3,
             sliderInput("slider1", h3("Sliders"),
                         min = 0, max = 100, value = 50),
             sliderInput("slider2", "",
                         min = 0, max = 100, value = c(25, 75))
      ),
      
      column(3,
             textInput("text", h3("Text input"),
                       value = "Enter text..."))
  )
  
))