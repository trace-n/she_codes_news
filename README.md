
# Tracey Nguyen: Django Project - She Codes News Website

## About This Project 

This Django project showcases a website for news articles. 

### High Level Overview of Project

- A News website has been created with Django with a local sqlite3 database. 
- Two apps have been created within the site - News and Users
- News app manages story viewing, creation, deletion
- Users app manages authentication, account management (view, edit)
- News articles can be displayed with latest stories shown as the highlight on the main index page
- Search can be completed without login from the navigation bar on each page
- New users can sign up for an account
- When a user is logged in, features enabled include: 
    - create, edit, delete stories belonging to them (admin can edit/delete for any user)
    - view, edit user profile
    - change password
    - favourite a story
    - view and remove favourites

## How to Run This Code
- 


## Database Schema
![ Screenshot of High Level Entity Relationship Diagram ]( ./images/erd.drawio.png "ERD")

## Project Features
- [X] Order stories by date![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] Styled "new story" form![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] Story images![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] Log-in/log-out![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] "Account view" page![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] "Create Account" page![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] View stories by author![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] "Log-in" button only visible when no user is logged in/"Log-out" buttononly visible when a user *is* logged in![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] "Create Story" functionality only available when user is logged in![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

## Additional Features:
- [X] Add categories to the stories and allow the user to search for stories bycategory.![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] Add the ability to update and delete stories (consider permissions - who should be allowed to update or and/or delete stories).![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] Add the ability to “favourite” stories and see a page with your favourite stories.![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] Our form for creating stories requires you to add the publication date,update this to automatically save the publication date as the day the story was first published (maybe you could then add a field to show when the story was updated).![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [X] Gracefully handle the error where someone tries to create a new story whenthey are not logged in.![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

 
## Wireframe

![ Screenshot of Wireframe ]( ./images/Wireframe_django_project.png "Wireframe")


## Future functionality/improvements

Additional features that were considered but not yet implemented:
- Comments for news articles
- Weather feature
- Personalisation of location of user to show weather for location
- User profile can load image for avatar

 