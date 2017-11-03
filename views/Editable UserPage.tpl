<DOCTYPE html>
<html> 
    <head>
        <title> User Page</title>
    </head>

    <body>
        <form action=/web/logout>
            <input type=submit value='Logout'/>
        </form>
        <form action=/web/update method=post>
            <h1>Here is your account information:</h1><br><br>
            <button type=button onclick="var inputs = document.getElementsByClassName('field');
for(var i = 0; i < inputs.length; i++) {
        inputs[i].disabled = false;
}")>Edit Me!</button><br>
            First Name:
            <input type='text' class=field name='firstname' disabled value={{user.firstname}}><br>
            Last Name:
            <input type='text' class=field name='lastname' disabled value={{user.lastname}}><br>
            User Name:
            <input type='text' class=field name='username' disabled value={{user.username}}><br>
            Email:
            <input type='email' class=field name='email' disabled value={{user.email}}><br>
            <input type='submit' class=field name='submit button' disabled value='Save'>
        </form> 
    </body>
</html>
