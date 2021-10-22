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

##### Debated Choices
- [x] payment
- [x] filter
- [] template design
-

###### Payment Debate

Orginally I was going to either write my own css file to create my desing or learn bootstrap.
I did not really enjoy useing bootstrap in class and could not decided if I wanted to use 4 or 5. I liked that 5 had all the new features
but it was not compatable with some broswers so I began the bootstrap 4 tutorial on w3. That is when I saw the information for
w3.css. I read through the intro of both w3.css and bootstrap 4 and decided to use w3.css because it seemed more intuitve while reading
the w3.css intro page which descirbes all the feature I began to see the website I could create. It sparked more ideas that bootstrap 4.
I would eventually like to learn bootstrap simply to understand more css systems.
The other big debate I had was purchasing options. In the begining Victoria had told me she would like to have a website where she could
sell prints but not the orginals. So I new we would need to have not only a way to print prints on demand but also to accept payments.
At this point I was not intrested in accepting payments on the website.

- [x] amazon merch
- [x] google merch
- [x] venmo
- [x] paypal
~~ - [] square ~~
- [x] Etsy
Amazon and Google would both be good options for creating online store fronts where purchases could occur and be logged. I also mostly
use Amazon and Google for my printing need so I was familer with thier printing services and the quality of their prints.
I also liked that if we chose the Venmo route to start. Once payment was recieved Victoria could order the print from either Amazon or
Google and have it directly sent to the users home.
Paypal is the option for payment only that I believe would be best becuase it would allow us to have a button on the site that directly
lead the user to paypals secure payment process.
Unfortunately Square was not an option.
At this time Venmo does not really support a ton of business transactions. The venmo website states its services
were design for individuals to pay their friend or people they already know. Not unknown entities or businesses.
Because Flagstaff is a smaller community and because Victoria is active in both the general communtity and the are community.
I feel like venmo could be both a good and legal option while she decides which longterm option she would like. Most of the purchases
would be from people in our community and would know victoria on a personal level. Especially for commissions/custom art pieces.
Etsy would also be a good option. A store front could be created. Etsy will also help you get the domain name for the website and has
website hosting built in. So we would not need to find another host or pay for a domain name. Most hosting sites can be free but domain
names are about 12 $ a year and the first year for the domain name is free with etsy. I believe esty would be the best storefront and
payment rolled into one.
Unfortunately I have been unable to speak or meet with Victoria since I developed this demo site due to illness and COVID.

###### Filter debate

Orginally I had differnt options for every print including grayscale, sepia, and opacity. Each filter had three options min, normal and
max. This is a featur offered throught w3.css which I thoguht was cool. And some of paintings did look cool with the extra options.
However I decided that this altered the orginal art piece and cluttered up the website. I did keep the orginal layout for this feature
incase we decided to use it.
You can see an example by clicking on the style button that is on the homepage.
Orgianly the indiviaul pages such as artloth.html had four pictures the original, grayscale, sepia and opacity image.
When if orginal was clicked the user would be direct to the print/purchase page.
If the image with a filter was clicked such as grayscale, sepia, or opacity. The user was directed to another page that had the orginal
print, then the 3 filter settings for that option. Ex would be orginal, grayscale-min, grayscale and grayscale-max. When on of these
were clicked it lead the user to the print/purchase page.

###### Template debate

For this progject I really wanted the website to look professional however I really did not want to use a template. So I started looking
into bootstrap.css on w3 and planned to do the online tutorial. That is when I found the w3.css tutorial. As I stated early the intro
page showed all the features and it seemed perfect for desiging by own layout for this page. I did look at the template for both
bootstrap and w3.css. None of them really meet what I wanted.
