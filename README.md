
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
    - sign out

## How to Run This Code
- An overview of Django setup is below
- Root directory is she_codes_news
- Apps are hosted in subdirectory referenced as she_codes_news = she_codes_news/she_codes_news/ 
- All other directories are referenced from root she_codes_news main directory

### Initial setup 
Step | Location | Command | Screenshots 
| :--- | :--- | :--- | :---
Clone template code for project | github | https://github.com/SheCodesAus/plus-django-news-project-template |  
Copy repo and rename to your own repo | github | Click "Use this template" and select name - "she_codes_news" | ![ git clone ]( ./images/git_template.png "git clone")
Go to your new Github repo created | github | Click "Code" button to get url to clone |  ![ git code ]( ./images/git_code.png "git code")
Go to terminal | root | git clone <your_link_goes_here> |
Check pip version | Root | python -m pip --version | ![ pip version ]( ./images/pip_install.png "pip version")
Install pip version (if required/no version found) | Root | python -m ensurepip --upgrade | 
Create virtual environment | Root | python -m venv venv | 
Activate virtual environment | Root | . venv/Scripts/activate |
Install Django library requirements | Root | python -m pip install -r requirements.txt |
Check installation successful | Root | python -m pip freeze | ![ pip freeze ]( ./images/pip_freeze.png "pip freeze")
Launch VS code | VS code | code . | 
Make initial migrations | /she_codes_news | cd she_codes_news <br> python manage.py migrate | ![ migrate ]( ./images/migrate.png "migrate")
Run local web server | /she codes_news | python manage.py runserver |  ![ runserver ]( ./images/runserver.png "runserver")
URL to launch main She Codes News Website homepage | /she codes_news | http://127.0.0.1:8000/news | Website loads
 

### Run Each Time for Local Web Server 
- This will be run in root directory she_codes_news where requirements.txt file is stored

Step | Location | Command |  
| :--- | :--- | :--- 
Activate virtual environment | Root | . venv/Scripts/activate
Run local web server | /she codes_news | python manage.py runserver
URL to launch main She Codes News Website homepage | http://127.0.0.1:8000/news
Turn off virtual environment | Root | deactivate 



## Database Schema

There are 3 database tables: 
- NewsStory - store the news stories, author, published date, content, image
- CustomUser - store the registered user account information
- Favourites - stores the user and news article that has been set as a favourite

![ Screenshot of High Level Entity Relationship Diagram ]( ./images/erd.drawio.png "ERD")

## Project Features
- [X] Order stories by latest date under "Latest News" section
    - Stories ordered by date descending for the latest updated 4 stories

    ![ Stories ordered by latest date under "Latest News" ]( ./images/order_stories.png "Latest news" )

- [X] Styled "new story" form
    - Mandatory fields: Title, category, URL, content

    ![ Add New Story Form ]( ./images/styled_new_story.png "Add New Story Form"  )

- [X] Story images
    - User can create story with a url for image
    - When image cannot be found, a default image is displayed
    - The field is mandatory and validated against URL format
 
    ![ Create story ]( ./images/New_story.png "Create story")    

- [X] Log-in/log-out
    - Login page for user to enter username and password
    - User can also "Sign up" if they do not have a login account
    - User is taken back to news homepage with updated nav bar
    - User can sign out from nav bar from sign out icon and is taken back to news homepage

    ![ Login page  ]( ./images/Login.png "Login page")
    ![ Log out  ]( ./images/Nav_bar_logged_in_new_story.png "Signout")    

- [X] "Account view" page
    - User can view account details
    - User can edit account from "View Account" page
    -   User can change password from the "Edit Account" page
        - User will be sent to password change completed page after password change

    ![ View Account ]( ./images/Account_view.png "View account")    
    ![ Edit Account ]( ./images/Account_edit.png "Edit account")    
    ![ Change Password ]( ./images/password_change.png "Change password")    
    ![ Change Password Done ]( ./images/password_done.png "Change password done")    

- [X] "Create Account" page
    - User can click on "Sign Up" from nav bar to create account 
    - User is taken to "Login" page after account created

    ![ Create Account ]( ./images/Create_account.png "Create account")        

- [X] View stories by author
    - Separate search field for author from category search to enable reuse of specific category search
    - Search will return a "Search Results" page
    - Search results will search either first or last name of author based on icontains filter
    - Search results will search in addition to author first/last name with category if entered
    - Search results will search only category if no author entered based on icontains filter
    - Search results will display no results available if no match found on criteria entered
    - No login required for search functionality

    ![ News categories search ]( ./images/Search_auth_cat.png "News categories search")    
    ![ News categories search results ]( ./images/search_results.png "News categories search results")    
    ![ News categories search author ]( ./images/search_auth.png "News categories search author")   
    ![ News categories search category ]( ./images/search_cat.png "News categories search category")           
    ![ News categories search no results ]( ./images/Search_no_results.png "News categories no search results")    

- [X] "Log-in" button only visible when no user is logged in/"Log-out" button only visible when a user *is* logged in

    ![ Nav bar not logged in  ]( ./images/Nav_bar.png "Login button")
    ![ Nav bar logged in ]( ./images/nav_bar_logged_in.png "Signout  button")    

- [X] "Create Story" functionality only available when user is logged in
    - "Add New Story" button is only displayed after user is logged in under the news category header section of the news homepage

    ![ Create story logged in  ]( ./images/Nav_bar_logged_in_new_story.png "Create story button")   
    ![ Create story ]( ./images/New_story.png "Create story")        

## Additional Features:
- [X] Add categories to the stories and allow the user to search for stories by category.
    - New story creation has a category drop down based on choices
    - News categories are displayed as links on the homepage under the header section
    - Separate search field for category from search by author to enable the News Category to reuse the search filter by category to show a search results page for   specific category selected.    
    - Search is managed with icontains filter for query 
    - No search results displayed if no results

    ![ News categories for create story ]( ./images/new_story_cat.png "News category")    
    ![ News categories and search stories by categories ]( ./images/Nav_bar.png "Search option in navigation bar - News categories under header")
    ![ News categories selection from category bar under header ]( ./images/Search_entertainment_category.png "News categories Entertainment")
    ![ Search by category via search bar ]( ./images/Search_category_nav_bar.png "Search by category")
    ![ Search by category results displayed]( ./images/Search_results_cat_nav_bar.png "Search by category results displayed")    
    ![ News categories search no results ]( ./images/Search_no_results.png "News categories no search results")    

- [X] Add the ability to update and delete stories (consider permissions - who should be allowed to update or and/or delete stories).
    - A user can update/ delete a story if they are the author of the story
    - A superuser/ admin can also update/ delete a story of another user
    - From the single story page, option appears to edit/ delete story via the pencil icon to edit story and bin icon to delete story
    - Favourites icon is also displayed, outline heart icon or solid heart icon, depending if user has favourited story 

    ![ Single story options for authenticated user ]( ./images/single_story_user_auth_options.png "Story options for authenticated user")
    ![ Edit story ]( ./images/user_edit_story.png "Edit story")
    ![ Delete story ]( ./images/Delete_story.png "Delete story")

- [X] Add the ability to “favourite” stories and see a page with your favourite stories.
    - When user is logged in, user can favourite/ unfavourite story from a single story detail view by clicking the heart icon
    - Favourites icon will be displayed as outline heart icon or solid heart icon, depending if user has favourited story 
    - From navigation bar, heart icon allows user to go to "Favourite News" page to view all favourites and remove favourites

    ![ Favourite story ]( ./images/favourite_story.png "Favourite story")
    ![ Unfavourite story ]( ./images/unfavourite_story.png "Unfavourite story")
    ![ View all favourites and remove ]( ./images/Fav_page_view_remove.png "View all favourites and remove")    

- [X] Our form for creating stories requires you to add the publication date,update this to automatically save the publication date as the day the story was first published (maybe you could then add a field to show when the story was updated).
    - Publication date is saved automatically on creation of new story
    - Changed date is saved automatically when a story is updated
    - These fields are not displayed on "New Story" creation or on "Edit Story" as they are automatically updated

    ![ Publication and change date of story ]( ./images/Publication_updated_date.png "Story publication/change date")

- [X] Gracefully handle the error where someone tries to create a new story whenthey are not logged in.
    - If a user is not authenticated for a page, they are redirected to the login page which also has a link to Sign up if the user does not have an account

    ![ User not authenticated ]( ./images/Error_user_not_authenticated.png "User not authenticated")

 
## Wireframe

A high level flow of the website functionality is provided below.

![ Screenshot of Wireframe ]( ./images/Wireframe_django_project.png "Wireframe")


## Future functionality/improvements

Additional features not yet implemented:
- Comments for news articles
- Weather feature
- Personalisation of location of user to show weather for location
- User profile can load image for avatar

 