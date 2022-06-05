# Cooking Conversion Tool
## By David Prestage
### Video demo: https://www.youtube.com/watch?v=SnPm2hJfqo4

#### Introduction:
This is a cooking conversion tool that I designed for the web before studying my Masters. It allows the user to convert between standard measurements of liquid, flour, butter and temperature. This was written in Python and Flask was used to tie this in to the HTML. I used a MySQL database to store the values for the various measurements, I recognise that I could have implemented this in a simpler manner but wanted to familiarise myself with this approach for future projects. The necessary calculations are done in Python. CSS was used for the website design and Flexbox was used for much of the layout. 

#### Use case:
I felt that this tool was useful, as many of the converters online were quite complex and did not specify where their measurements were sourced from. My tool aims to provide information on the most commonly needed conversions quickly and easily, while providing clarity on my sources. 

#### Conciseness of code:
I've tried to keep the Python code as concise as possible by using the variables 'measure' and 'substance'. These change based on what substance the user selects to convert and allowed me to avoid duplicating the code for the different substances. When it came to the HTML, I went in a different direction and had different sections for each substance. I found that there were a lot of variables that would need to be substituted using Flask to tighten up the HTML and I wanted to have different measurements selected by default for each of the substances. I thought that bringing these all into one section like I did for Python could make the code overly confusing, so I decided against it.

#### File structure:
I laid out the file structure of this project in a way that would allow it to be built into a larger project. I split ‘app.py’ into ‘__init__.py’, ‘views.py’ and ‘webbapp.py’ and did my best to follow best practise in the folder structure. Fonts and images were placed under static and you can find the SQL that was used to create my MySQL database under 'SQL backups and instructions'. In the template folder, you can find the HTML files for the website. 

#### Design choices:
I chose to keep the website on one page, using Flask to insert the HTML that is required on the ‘cooking.html’ page. This was done to make it look more modern and to give the impression of an app rather than a traditional website. The 'layout.html' page provides the layout for flask, imports the CSS and outlines the necessary viewport settings that I needed for the website to display correctly. 

I created the website primarily for the mobile viewport and then set up media queries for tablets and for a full-sized PC screen. I did this as I felt this would be the primary use case for my website, with people using it to quickly check whilst cooking. I used Flexbox for the layout in CSS, as I found this was the best way to organise the elements neatly on the screen and to provide an experience that changes with the viewport. The buttons at the top of the page for instance will change from two rows of two buttons to a single row of 4 when the user moved to the tablet or a larger display. This was done to best use the real estate of the screens. I also decided to centralise the buttons on the full-sized PC display and remove the grey background as I felt this made the website look more professional on a large screen.

Software and language choices:
I decided to use Python for the backend of the website, to keep implementation simple. I also wanted to try out Flask in a personal project. Moving forward I will be using React.

I decided on MySQL for storage of the data as from my research this appeared to me amongst the most popular versions of SQL. I decided against using SQLite, which I’ve used previously, as I wanted to work with a version more commonly used in industry. This project was done before I studied Postgres.

I decided on using Visual Studio Code as it allowed me to work across various languages within the program, though I had to create a virtual environment to allow for the use of Flask.
