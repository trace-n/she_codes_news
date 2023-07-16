# Plus Resources: Django Project  

## Overview 

This Django project showcases a website for news articles. 

Functionality that has been provided includes:
- Ordered stories by latest date
- CSS styling for webpages
- Adding a form to:
    - create, edit, delete new stories
    - create, edit, view user
- Adding a field to store image URLs
- Functional login/logout buttons
- Search stories to view by a particular author (first/last name) or category
- Show/hide relevant information, features based on whether user is logged in
- Categories added for news articles
- Publication date on create is automatically captured without user input when user creates news article
- Last updated date is automatically captured without user input when user edits news article
- Handle error when someone tries to create a new story when they are not logged in

## High Level Flow of Project

- News articles can be displayed with latest stories shown as the highlight on the main index page
- Search can be completed without login
- When a user is logged in, features enabled include: 
    - create, edit, delete stories belonging to them (admin can edit/delete for any user)
    - edit user profile
 
## Screenshots of wireframe

![ Screenshot of wireframe ]( ./images/Wireframe_django_project.png "Wireframe")


## Future functionality/improvements

Additional features that were considered but not yet implemented:
- comments for news articles
- using media for to store image uploads
- enable user to favourite news articles and display/edit favourites
 