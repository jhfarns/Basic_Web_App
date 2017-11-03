<!DOCTYPE html>
<html>
	<head>
		<title>Squindistries Welcome Back Page</title>
	</head>
	<body>
        <form action=/web/logout>
            <input type=submit value='Logout'/>
        </form>
		<h1>Squidge is happy to see you again!</h1>
		<form action = '/web/login/existing' method='post'>
			<fieldset>
				<legend>Log In:</legend><br>
				Username:<br>
				<input type = 'text' name = 'username'><br><br>
				Password:<br>
				<input type = 'password' name = 'password'><br><br>
				<input type = 'submit' value ='submit'>
			</fieldset>
		</form> <br>
        <a href='/web/forgotpassword'>Did you for get your password?</a> 


		<h1>You haven't met Squidge yet!? Fill out the form below to sign up!</h1>
		<form action="/web/login/new" method="post">
			<fieldset>
				<legend>Sign Up:</legend><br>
				First Name:<br>
				<input type = 'text' name ='firstname'><br><br>
				Last Name:<br>
				<input type = 'text' name = 'lastname'><br><br>
				Email:<br>
				<input type = 'email' name = 'email'><br><br>
				Username:<br>
				<input type = 'text' name = 'username'><br><br>
				Password:<br>
				<input type = 'password' name = 'password'><br><br>
				<input type = 'submit' value ='submit'>
			</fieldset>
		</form>
	</body>
</html>
