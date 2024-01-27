Lab - 8
Django Blog web site mini project 

Instructions :

- Setup the project given in this folder in your own machine.

- Perfrom migration ( makemigration and migrate commands)

- Create a super user.

- Run the project and login in the admin panel using super user.

- Create 2-3 normal users using admin panel.

- Create corresponding blogs and blog posts using admin panel.

- Now go to /blog/home and check the content of the blog and blog posts : Basically, this page combines the details from both tables blog and blog post and displays it in a single view. Refer corresponding view file and template file and understand the code.

----------------------------------------------------------------------------------------------------------
Now, add below functionalities in your project : 

**Extension-1**

- Add functionality to create a blog and blog post through web forms. For this, you need to define :
  - forms.py file : two classes, one for blog, other for blog post
  - view functions for adding blog and for adding blog post.
  - two templates : create_blog.html and create_blog_post.html

**Extension-2**

- Add necessary bootstrap elements to the tempaltes to make it attractive.

**Extension-3**

- Setup authentication ( Register, Login and Logout) in the project.
- Now, when the user creates a new blog, it automatically maps to the current logged in user instead of selecting a user from the dropdown list.


  
