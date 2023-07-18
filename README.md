
# Tracey Nguyen: Django Project - She Codes News Website

## About This Project 

This Django project showcases a website for news articles. 


## How to Run This Code
- 


## Database Schema
![ Screenshot of High Level Entity Relationship Diagram ]( ./images/ERD.png "ERD")

## Project Features
- [X] Order stories by date![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] Styled "new story" form![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] Story images![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] Log-in/log-out![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] "Account view" page![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] "Create Account" page![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] View stories by author![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] "Log-in" button only visible when no user is logged in/"Log-out" buttononly visible when a user *is* logged in![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] "Create Story" functionality only available when user is logged in![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

## Additional Features:
- [X] Add categories to the stories and allow the user to search for stories bycategory.![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] Add the ability to update and delete stories (consider permissions - who should be allowed to update or and/or delete stories).![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] Add the ability to “favourite” stories and see a page with your favourite stories.![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] Our form for creating stories requires you to add the publication date,update this to automatically save the publication date as the day the story was first published (maybe you could then add a field to show when the story was updated).![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] Gracefully handle the error where someone tries to create a new story whenthey are not logged in.![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )


## High Level Flow of Project

- News articles can be displayed with latest stories shown as the highlight on the main index page
- Search can be completed without login
- When a user is logged in, features enabled include: 
    - create, edit, delete stories belonging to them (admin can edit/delete for any user)
    - edit user profile
 
## Wireframe

![ Screenshot of Wireframe ]( ./images/Wireframe_django_project.png "Wireframe")




Functionality that has been provided includes:
- [X] Ordered stories by latest date
- [X] CSS styling for webpages
- [X] Adding a form to:
    - [X] create, edit, delete new stories
    - [X] create, edit, view user
- [X] Adding a field to store image URLs
- [X] Functional login/logout buttons
- [X] Search stories to view by a particular author (first/last name) or category
- [X] Show/hide relevant information, features based on whether user is logged in
- [X] Categories added for news articles
- [X] Publication date on create is automatically captured without user input when user creates news article
- [X] Last updated date is automatically captured without user input when user edits news article
- [X] Handle error when someone tries to create a new story when they are not logged in



## Future functionality/improvements

Additional features that were considered but not yet implemented:
- comments for news articles
- using media for to store image uploads
- enable user to favourite news articles and display/edit favourites
 