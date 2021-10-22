# Victorias Art Show
## By Monica Evans
### Flagstaff, AZ, UnitedStates
#### video link

##### Project Goal

A few months ago I was approced by a local artist who was a family friend. She mentioned that she was wanting to set up a
website for her artwork where she could sell prints but she did not know how.
At the time I did not know how to begin to make a website. She knew I was taking classes in computer science and asked that when I
get to website development in my studies that I reach out.
I really enjoyed week 8 and 9 problem sets. It was these assignments that gave me the cofidence to chose Victoria's Art Show as my
final project.

##### How did this all come together

We had previously used bootstrap in class and I set out to learn more regaurding bootstrap on W3.
It was there that I learned W3 had their own css framework. I had not specifically enjoyed using boot strap and I didnt want to
use a template for my website lay out. Instead I wanted to design the layout my self.
I completed the tutorial on W3.css and began desining the website.
To start I completed a webpage demo to show to Victoria so that she might have an idea of what her page could look like.
This demo page was called Monica's Art.

##### Design

My design:
- [x] Homepage
- [x] About the artist
- [x] Art Gallary
- [x] Inspiration behind the art
- [x] Contacting the artist
- [x] Next show
- [x] Ordering prints
- [] Request custom art

I wanted people to not only be able to view and buy Victoria's art. But also get to know a little bit about her. She has lived a very
full, hard, adventerous, brave life. I think that her experiences from life probably drive some of her art. I also wanted to give her
a place where her art could tell her story. I hope I have accomplised this.

##### Files

I designed the website in CS50 using flask like we have done in class. After completing the w3-css tutorial I started by setting up
my folders. Folders include Project, Static, and Templates.
W3 recommends creating a skeleton.html page and a style page that you use every time you desing a webpage.
So I desinged a basic skeleton page that I could also use for my layout.html and then my other web pages.
! [skeleton page](https://drive.google.com/file/d/1SQZbnG_6XyEiJEfsfbjLb0ia_sA5zPIz/view?usp=sharing)

From here I was able to build all of my other html pages.

##### Project

###### Application.py

After building the skeleton and layout page I went on to build the application file.
The application file imports os, cs50 SQL, flask redirect, render_template, request and flask mail.
It also has the app routes for all pages including about, art, contact, index, layout, print, artloth, bagend,
meg, sun, tom and tree.
Also app route email which gets information from the print page including name, email, painting and place.
Takes this info and adds it to the database.
Then order info back from data base so that it can be emailed to the user.

###### Order.db

This is a SQL database that I am using to store the order information regarding orders.
I made a point to not store sensitive information. The only information stored about the user is a email and name.
There is not registration for this page so that there are no passwords to store.
The information stored includes id (int) which is auto incremented, user name, user email, painting requested, and printing place.

##### Templates Folder

Here is listed the html files that form the web page

###### Index

index.html is a file that contains the main page and homepage of the website. My goal was that the homepage could lead to all other
pages in the website. Also that every thing would be a button and link to other pages. I wanted a navigation bar for both the pages
and the individual art work. A photo of the artist that when clicked would lead to the about me page. A banner that would lead to the
gallary and a slide show of all the art on the website that would also lead to the gallary.

###### About

This file creates a page that can be accessed from both the picture of the artist on the homepage and from the About nav bar link on the home page.
It has a different photo of the artist. Talks about the start of their art carrer and then future plans.

###### Art

This file creates the gallar or art walk webpage. Can be accessed from the nav bar by clicking on Art, by clicking on the homepage "Art Show"
banner, or by clicking on the slideshow.
This page has images of all avaiable art work which are also buttons leading to their own html pages. At the very bottom it also has
a buy prints button that will lead to the print page where prints can be purchased.

###### Contact

This file creates the contact page. Can be accessed from the nav bar contact button as well as the link at the bottom of the container
holding the artisit photo on the homepage.
This page has the nav bar as well as a three celled container that has information regarding
the next show, email and how to request custom art work.

###### Print

This file creates the print page which also serves as our purchase page.It can be accessed from the nav bar prints button or from
clicking on the specific painting from the paintings page.
This page lists the info regarding prints and where they can be printed with prices listed. As well as the option for a JPG or PDF file.
The form takes the users name and email as well as their painting and printing place of choice and enters it into the ticket table.
Then the a confirmation email is sent to the user telling them about the next steps for payment and shipping. Currently I have it set up
for users to pay using venmo. However I have put links on the print page for both Amazon merch and Google Merch to show Victoria that
how to set up a online store with either company. Users would then be taken by link to the store and all purchasing would happen there.
I did this because I did not feel comfortable accepting peoples credit cards on line. Also because Victoria is not tech savy and I
felt it would be too much for her to manage.

###### Individual Art pages

The following pages where created for each individual art page. They are as follows artloth, bagend, meg, sun, tom, and tree. All these
pages can be accessed from the home page from the art nav bar or from the art/gallary page. Each of the individual painting pages shows
the painting again and then has a inspiration button that when clicked opens a pannel that tells the story of the inspiration behind the
art work. When the painting itself is click it takes the user to the prints page.

##### Static Folder

This folder holds all the jpg files for the site including the atrist two portriats and the photos of all the art work. This allows
the pictures to be accessable but keeps them from clutering up the main or template folder and keeps everything organized.
It also holds the style sheet which honeslty after learning w3.css I didnt need to use. Everything I wished to complete I could easily do
with the w3.css classes. Typically I would have created buttons, text options, containers and whatever else in the css page but it did
not seem nesessary.

##### Requirments.txt

This text just stated what I used to make the website which was SQL, cs50, and w3.css.

##### README.md

The README file is this file and was created to explain what I had done for each file. I did have to learn markdown to creat this file
and I really enjoyed the abiblity to do that.
