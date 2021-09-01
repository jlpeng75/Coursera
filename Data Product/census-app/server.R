#
# This is the server logic of a Shiny web application. You can run the 
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)
source("helpers.R")
counties <- readRDS("data/counties.rds")
library(maps)
library(mapproj)
# Define server logic required to draw a histogram
shinyServer(function(input, output) {
  
  output$map <- renderPlot({
      
      data <- switch(input$var,
                     "Percent White" = counties$white,
                     "Percent Black" = counties$black,
                     "Percent Hispanic" = counties$hispanic,
                     "Percent Asian" = counties$asian)
      color <- switch(input$var,
                      "Percent White" = "darkgreen",
                      "Percent Black" = "black",
                      "Percent Hispanic" = "darkorange",
                      "Percent Asian" = "darkviolet")
      legend <- switch(input$var,
                       "Percent White" = "% White",
                       "Percent Black" = "% Black",
                       "Percent Hispanic" = "% Hispanic",
                       "Percent Asian" = "% Asian")
      
      percent_map(data, color, legend, input$range[1], input$range[2])
     
     
    
  })
  
})
