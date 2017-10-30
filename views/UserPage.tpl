<!DOCTYPE html>
<html> 
    <head>
        <title> User Page</title>
    </head>

    <body>
        <form action=/web/logout>
		<input type=submit value='Logout'/>
        </form>
        <h1> Hello {{user.firstname}} {{user.lastname}} Welcome to your user page!</h1> <br>
        <h3> Your account information is listed below</h3> <br>
        <ul>
            <li>First Name: {{user.firstname}}</li>
            <li>Last Name: {{user.lastname}}</li>
            <li>User Name: {{user.username}}</li>
            <li>Email: {{user.email}}</li>
    </body>
</html>
