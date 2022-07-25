# Jacros Graphic Design


## Contents
- [Introduction](#introduction)
- [UX](#ux)
- [Technologies](#technologies)
- [Features](#features)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credit)
- [Acknowledgements](#acknowledgements)


## Introduction
My submission for my P5, e-commerce applications, Project. This is a website offering my services as a graphic designer.
The website contains information about past projects I've worked on, a payment and quotes system, a review system where reviews can be edited and deleted by users and a newsletter sign up page. Information will be stored on a PostgreSQL database and will be able to be maintained and edited by the superuser.


### Demo

https://jacros-graphic-design.herokuapp.com/ - Live link to website!

## UX

Utilising UX design is essential these days to provide meaningful and relevant experiences to the user. To provide more balance and structure to my UX design I opted to use the five planes method to design and implement on my website.

### Strategy

**Vision**

The vision of the website is to show users past projects I have worked on and also giving them an easy and safe way to pay for my services.
By signing up to the newsletter users can stay uptodate with projects I'm working on and new skills I've acquired. Potential users can also read reviews left my previous customers to get a better understanding of what I can offer. 

**Aims**

1. Provide a stylish, easy to use and intuitive website.
2. Implement a payment service, using Stripe, which is safe and easy to use.
3. Create a contact form for information on jobs and requests from users.
4. Provide users with information on past projects
5. Enable users to Login/Logout, autofilling information when logged in to save time when leaving reviews or filling in quotes form.
6. Allow users to create, edit and delete reviews they have left.
7. Have a newsletter users can signup to to stay uptodate on jobs I'm working on and new skills I've acquired.


**User Stories**

- As a User I want a stylish looking well thoughout website so that i can find everything i want and access information easily
- As a Site Admin I want to be able to login to see orders so that i can maintain and manage customer purchases
- As a User I want to be able to log in and log out so that i can keep my information safe and see any products/services have i purchased
- As a User I want to be able to leave, update, delete and read reviews so that i read about previous customers experiences and leave my own experiences for other consumers
- As a User I want to be able to pay for good and services safely and securely so that i can not worry about my information being stolen
- As a User I want to be able to register so that i can log in when i return in future
- As a User I want to be able to request a quote so that i can get an understanding of costs before making a decision to buy
- As a User I want to see messages when logging in and logging out so that i can be sure the action was undertaken
- As a User I want to be able to change my password so that i can do so if the need arises and keep my account/information safe
- As a User I want to be able to contact the owner so that i can get specific information relevant to me
- As a User I want to see a professional looking homepage that will draw me in so that i can find out more information in an easy manner
- As a User I want to be able to easily navigate the site so that i can easily view all the content
- As a User I want a stylish looking well thoughout website so that i can find everything i want and access information easily



### Scope

Based on my user stories these are the features I felt needed implementing:

- Homepage/About page with information about who we are, what we do and previous projects worked on.
- A navigation bar to take you to the pages on the site
- Registration page so that customers could register
- Payments/quotes page so users can request quotes or pay for services through Stripe payments.
- Login and Logout, powered by Django AllAuth, so user could safely log in and out.
- Contact Us page, with form, so customers with special requests could get in touch
- A reviews page with full CRUD functionality
- A newsletter signup page so users can stay uptodate with projects I'm working on 



### Structure

The website is relatively simple in it's structure. Everything is clearly labeled and easily navigational so the user can get to what they need easily. All the major aspects of the website have their own page:
- Landing page with an animated logo
- About page to learn information about me
- Payments section split into two pages, one for making a payment and another for getting a quote.
- Members area for signing in or signing up and if signed in for seeing your account page or logging out.
- Contact us section split into two pages, one for sending a contact form and another for signing up to a newsletter.
- Reviews page for leaving, editing or deleting reviews.
- Navbar on each page to allow for easy navigation through the website.
- Footer containing social links at the bottom of each page

### Databases

I have three apps that require databases. They are contact app, payments app and reviews app.

These apps have customs models and forms to enable users to get in contact, sign up for a newletter, get a quote, make a payment and then full CRUD functionality on the reviews section.

#### Contact App

The contact app is split into two sections. One is for a contact from and the other for signing up to a newsletter.
The contact form has a custom model, and related form, which requires user to enter their name, email address, phone number, date and a textarea for leaving their message.
Users do not have to be registered to use this feature.

The newsletter form is a simpler version of the contact form. It only required users to input their name, phone number and email address in order to sign up for the newsletter.

The information from both forms is then sent to the database which can then me managed by the admin on the backend.


#### Payments App

The payments app also has two sections. One for getting a quote and another for making a payment.
The quote section has a custom model and form to enable the user to get a quote for a job/project.
The user is required to fill in their name, phone number, email address, a project type from a list of dropdown options, a deadline date and then a message box for all additional information. A unique quote id number is also generated and attached to the quote for ease of management for the admin.

The payments section is created using Stripe. It is made using custom JavaScript to handle the card payments and the overall submission of the payments form.
It is all linked to my Stripe account which deals with receiving payments. The views.py file contains the relevant views to handle the stripe payments form created by the JavaScript. There is also custom CSS to help with the styling of the payment form.


#### Reviews

The reviews app is where I implemented the CRUD functionality for my website.
In order to leave a review you must be registered and logged in.

The reviews app has a custom model which required users to input a title, the body of the review itself and then a rating between 1 and 5.
The user name and date of creation are automatically attached to the review. After a review has been left the user can edit or delete a review. They can only do this if the user id of the logged in user matched the user id of the user who created the review. This is to prevent other users deleting reviews they did not write. By enabling the user to be able to edit and delete their reviews after they have created them it gives the reviews app full CRUD functionality.


### Skeleton

[Wireframes for this project](assets/documents/p4-wireframes.pdf)

My wireframes were created using Balsamiq and represent the simplicity I was going for.

Using bootstrap I tried to give everything uniform and similar so the user would feel comfortable navigating around the site.
I tried to keep as close to my wireframes as possible when creating the various pages.

### Surface


## Technologies

The following is a list of the various technologies I used along with what they were used for:

- Django:
Django is the framework that has been used to build the over project and its apps.
- Python:
Python is the core programming language used to write all of the code in this application to make it fully functional.
- Bootstrap:
Used for creating responsive design.
- Google Fonts:
Used to obtain the fonts linked in the header, fonts used were Raleway and Lobster
- Font Awesome:
Used to obtain the icons used on the high scores and rules pages.
- Google Developer Tools:
Used as a primary method of fixing spacing issues, finding bugs, and testing responsiveness across the project.
- GitHub:
Used to store code for the project after being pushed.
- Git:
Used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
- Gitpod:
Used as the development environment.
- Heroku:
Used to deploy my application..
- Pep8:
Used to test my code for any issues or errors.
- Unicorn Revealer:
Used to detect overflow of elements, which allowed me to quickly debug any issues.
- Coloors:
Used to create a colour palette for the design.
- Cloudinary:
Used to store all of my static files and images.
- W3C Markup Validation Service:
Used to validate all HTML code written and used in this webpage.
- W3C CSS Validation Service:
Used to validate all CSS code written and used in this webpage.
- PostgreSQL:
I have used Heroku's PostgreSQL relational database in deployment to store the data for my models.

## Features

**Features Implemented**






## Testing

### Manual Testing

#### NavBar


#### Registration/Login/Logout

After testing the navbar to ensure everything was working I then decided to test the allauth registration and login.
I filled in the registration form and was able to create a new user. 

![registration form](https://github.com/jackcrosbie/p4-restuarant-project/blob/main/assets/documents/images/registration-form.png?raw=true)

This all worked correctly and brought me to the relevant pages.
After my registration was complete I then checked I could log in as the newly created user. This again all worked as hoped so I was able to move on.

Next i tested the log out functionality was working. I clicked the log out button on the first navbar and was prompted to confirm I wanted to log out.
After confirming I wanted to log out I was logged out and no longer had access to the accounts page. This meant I couldn't see, edit or delete reservations made.
This was the outcome I had hoped for.


## Deployment

The master branch of this repository has been used for the deployed version of this application.

Using Github & Gitpod
To deploy my command-line interface application, I had to use the Code Institute Python Essentials Template, as this enables the application to be properly viewed on Heroku using a mock terminal.

- Click the Use This Template button.  
-  Add a repository name and brief description.
-  Click the Create Repository from Template to create your repository.
-  To create a Gitpod workspace you then need to click Gitpod, this can take a few minutes.
-  When you want to work on the project it is best to open the workspace from Gitpod (rather than Github) as this will open your previous workspace rather than creating a new one. You should pin the workspace so that it isn't deleted.
-  Committing your work should be done often and should have clear/explanatory messages, use the following commands to make your commits:
   -  git add .: adds all modified files to a staging area
   -  git commit -m "A message explaining your commit": commits all changes to a local repository.
   -  git push: pushes all your committed changes to your Github repository.

### Creating an Application with Heroku

I followed the below steps using the Code Institute tutorial:

- The following command in the Gitpod CLI will create the relevant files needed for Heroku to install your project dependencies pip3 freeze --local > requirements.txt. Please note this file should be added to a .gitignore file to prevent the file from being committed.
1. Go to Heroku.com and log in; if you do not already have an account then you will need to create one.
2. Click the New dropdown and select Create New App.
3. Enter a name for your new project, all Heroku apps need to have a unique name, you will be prompted if you need to change it.
4. Select the region you are working in.

Heroku Settings You will need to set your Environment Variables - this is a key step to ensuring your application is deployed properly.

- In the Settings tab, click on Reveal Config Vars and set the following variables:
  - If using credentials you will need to add the credentials as a variable, the key is the name 'CREDS' and the value is the contents of your creds JSON
  - Add key: PORT & value 8000
- Buildpacks are also required for proper deployment, simply click Add buildpack and search for the ones that you require.
  - For this project I needed to add Heroku Postgres.

Heroku Deployment In the Deploy tab:

- Connect your Heroku account to your Github Repository following these steps:
  - Click on the Deploy tab and choose Github-Connect to Github.
  - Enter the GitHub repository name and click on Search.
  - Choose the correct repository for your application and click on Connect.
- You can then choose to deploy the project manually or automatically, automatic deployment will generate a new application every time you push a change to Github, whereas manual deployment requires you to push the Deploy Branch button whenever you want a change made.
- Once you have chosen your deployment method and have clicked Deploy Branch your application will be built and you should see the below View button, click this to open your application:

## Credit

All the code used is entirely original and written by me. However I drew on resources such as Stack Overflow, django.docs, tutor support and Slack to fix various bugs and issues i encountered.

### Acknowledgements

As always I want to thank my mentor, Daisy McGirr for her fantastic advice, support and feedback throughout this project and beyond. I would also like to thank my peer Daisy Gunn for always being helpful, full of advice and willing to listen.
