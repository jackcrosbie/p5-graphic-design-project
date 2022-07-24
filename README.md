I# Jack's Bistro


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



### Demo

https://jacksbistro.herokuapp.com/ - Live link to website!

## UX

Utilising UX design is essential these days to provide meaningful and relevant experiences to the user. To provide more balance and structure to my UX design I opted to use the five planes method to design and implement on my website.

### Strategy

**Vision**



**Aims**


**User Stories**



### Scope

Based on my user stories these are the features I felt needed implementing:



### Structure



### Databases



#### Reservations





#### Contact Us



#### Menu



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
