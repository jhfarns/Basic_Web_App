<!DOCTYPE html>
<html> 
    <head>
        <title> User Page</title>
    </head>

    <body>
        <h1> Hello {{user.first_name}} {{user.last_name}} Welcome to your user page!</h1> <br>
        <h3> Your account information is listed below</h3> <br>
        <ul>
            <li>First Name: {{user.first_name}}</li>
            <li>Last Name: {{user.last_name}}</li>
            <li>User Name: {{user.username}}</li>
            <li>Email: {{user.email}}</li>
    </body>
</html>
