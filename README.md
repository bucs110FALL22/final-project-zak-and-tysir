:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Daily News
## CS 110 Final Project
###  Fall, 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

https://replit.com/@tjurado1/final-project#main.py

<< [link to demo presentation slides](#) >>

### Team: Zak/ty
#### Zak and Tysir 

***

## Project Description

This program gives us 7 buttons to press and those buttons would give us different pop ups with information with the certain button that you pressed. These 7 buttons are weather, stocks, news, fun fact, Today in History, quote of the day, and sports. 

***    

## User Interface Design

- **Initial Concept**
  - << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components. >>
    
    
- **Final GUI**
  - << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design

* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. 
         For each additional module you should include
         - url for the module documentation
         - a short description of the module >>
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg) 
* Classes
    *  Jokes: This class allows us to get a random joke from the url posted in the file so we can display that joke onto the screen. 
    *  Quotes: This class allows us to get a random quote from the url posted in the file so we can display the quote onto the screen. 
    *  Weather: This class allows us to get weather updates from the url posted in the file so we can display the news about the weather onto the screen. 
    *  Fact: This class allows us to get a random fact from the url posted in the file so we can display the fact onto the screen. 

## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * weather.py
    * jokes.py
    * fact.py
    * quotes.py
    * brief.py
* assets
    * image.py
    * facts_button.png
    * joke.png
    * news2.png
    * quote_image.png
    * stocks2.png
    * weather.png
* etc
    * test.py

***

## Tasks and Responsibilities 

   Ty: worked on buttons, the source files, putting the buttons in the correct location. 
   Zak: worked on making the images for the buttons, making the buttons clickable. 
   Both: worked on making the text move across the screen wehen a button was clicked. 

## Testing

* What we did to efficiently complete this final project is we wrote down a check list with all the objectives we had to complete in order to complete this project. Next, we split up into to do different sections of the project. Along the way, we kept running the code to see what was wrong and debuggeed it so our project runs smoothly. 

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
