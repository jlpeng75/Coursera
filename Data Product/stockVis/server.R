#
# This is the server logic of a Shiny web application. You can run the 
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)
library(quantmod)

source("helpers.R")
# Define server logic required to draw a graph
shinyServer(function(input, output) {
     dataInput <- reactive({
          getSymbols(input$symbol, src = "yahoo",
                     from = input$range[1],
                     to = input$range[2],
                     auto.assign = FALSE)
      })
     
     finalInput <- reactive({
         if (!input$adjust)
             return(dataInput())
         adjust(dataInput())
         
     })
        
      
     output$price <- renderPlot({
         chartSeries(finalInput(), theme = chartTheme("white"),
                  type = "line", log.scale = input$log, TA = NULL)
    
  })
  
})
