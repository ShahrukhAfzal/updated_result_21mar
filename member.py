#!/home/shah/yes/bin/python

print("Content-Type: text/HTML")
print()



print("""
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Member SignUp - Register -</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet">
    <style type="text/css">
        @import url(http://fonts.googleapis.com/css?family=Roboto:400,300,100,500,700);
@import url(http://fonts.googleapis.com/css?family=Roboto+Condensed:400,300,700);

body {
    background: #fff;
	font-family: 'Roboto', sans-serif;
	color:#333;
	line-height: 22px;	
}
h1, h2, h3, h4, h5, h6 {
	font-family: 'Roboto Condensed', sans-serif;
	font-weight: 400;
	color:#111;
	margin-top:5px;
	margin-bottom:5px;
}
h1, h2, h3 {
	text-transform:uppercase;
}

input.upload {
    position: absolute;
    top: 0;
    right: 0;
    margin: 0;
    padding: 0;
    font-size: 12px;
    cursor: pointer;
    opacity: 1;
    filter: alpha(opacity=1);    
}

.form-inline .form-group{
    margin-left: 0;
    margin-right: 0;
}
.control-label {
    color:#333333;
}
    </style>
    <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>





<link href="all/css/common.css" rel="stylesheet" type="text/css" />
        <!----Media queries css--->
         <link href="all/css/style.css" type="text/css" rel="stylesheet" />
         <link href="all/css/theme1024.css" rel="stylesheet" type="text/css" />
        <link href="all/css/theme990.css" rel="stylesheet" type="text/css" />
        <link href="all/css/theme768.css" rel="stylesheet" type="text/css" />
        <link href="all/css/theme480.css" rel="stylesheet" type="text/css" />
        <link href="all/css/theme320.css" rel="stylesheet" type="text/css" />
        <link href="all/css/theme319.css" rel="stylesheet" type="text/css" />
    <link href="all/css/quickweb.css" rel="stylesheet" type="text/css" />
     <link href="all/fonts/style.css" rel="stylesheet" type="text/css" />   
   <link href="all/css/slider_css.css" type="text/css" rel="stylesheet" />
    <link href='https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,300,600,700,900' rel='stylesheet' type='text/css'/>

    <script src="all/js/jquery-ui.js"></script>
    <script src="all/js/jquery-1.11.3.min.js"></script>
    <script src="all/js/slider.js"></script>
    <script src="all/js/plugin.js"></script>
</head>
<body>
  

    <div class="main">
                    <header class="header">
                <div class="container">
                    <div class="col-12">
                   

                    <nav class="mob-menu-icon mb-1">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                       <span class="icon-bar"></span>
                   </nav>

                        
                    <nav class="col-8 menu mob-menu pull-right">
                        
                         <nav class="mob-menu-icon" style="padding: 26px 26px;width: 100%;box-sizing: border-box;border-bottom:2px solid #1565C0; ">
                        
                        <span class="icon-bar slide-icon-menu-color"></span>
                        <span class="icon-bar slide-icon-menu-color"></span>
                        <span class="icon-bar slide-icon-menu-color"></span>

                    </nav>
                      
                        <div class="menu-item-box center "><a href="index.html" class="menu-link">Home</a></div>
                     <div class="menu-item-box center "><a href="index.html#about" class="menu-link">About</a></div>
                        <div class="menu-item-box center "><a href="index.html#contact" class="menu-link">Contact</a></div>
                        <div class="menu-item-box center "><a href="i.html" class="menu-link">Login</a></div>
                        <div class="menu-item-box center "><a href="member.html" class="menu-link">Signup</a></div>
                        
                        

                        </nav>

                    </div>
                        </div>
            </header>
     <hr>





<body>
<div class="container">
	<div class="row">
    <div class="col-md-8">
      <section>      
        <h1 class="entry-title"><span>Sign Up</span> </h1>
        <hr>
            <form class="form-horizontal" method="post" name="signup" id="signup" enctype="multipart/form-data" action="signup.py">
        <div class="form-group">
          <label class="control-label col-sm-3">Email ID <span class="text-danger">*</span></label>
          <div class="col-md-8 col-sm-9">
              <div class="input-group">
              <span class="input-group-addon"><i class="glyphicon glyphicon-envelope"></i></span>
              <input type="email" class="form-control" name="email" id="emailid" placeholder="Enter your Email ID" value="" required>
            </div>
            <small1> Your Email Id is being used for ensuring the security of your account, authorization and access recovery. </small1> </div>
        </div>
        
        <div class="form-group">
          <label class="control-label col-sm-3">Set Password <span class="text-danger">*</span></label>
          <div class="col-md-5 col-sm-8">
            <div class="input-group">
              <span class="input-group-addon"><i class="glyphicon glyphicon-lock"></i></span>
              <input type="password" class="form-control" name="pwd" id="password" required placeholder="Choose password (5-15 chars)" value="">
           </div>   
          </div>
        </div>

        <div class="form-group">
          <label class="control-label col-sm-3">Full Name <span class="text-danger">*</span></label>
          <div class="col-md-8 col-sm-9">
            <input type="text" class="form-control" name="name" id="mem_name" required placeholder="Enter your Name here" value="">
          </div>
        </div>

          <div class="form-group">
          <label class="control-label col-sm-3">College Code<span class="text-danger">*</span></label>
          <div class="col-md-8 col-sm-9">
            <input type="text" class="form-control" name="college_code" id="mem_name"  placeholder="Enter your College Code here" value="" required>
          </div>
        </div>


        <div class="form-group">
          <label class="control-label col-sm-3">Gender <span class="text-danger">*</span></label>
          <div class="col-md-8 col-sm-9">
            <label>
            <input name="gender" type="radio" value="Male" checked required>
            Male </label>
               
            <label>
            <input name="gender" type="radio" value="Female" >
            Female </label>
          </div>
        </div>
        <div class="form-group">
          <label class="control-label col-sm-3">Contact No. <span class="text-danger">*</span></label>
          <div class="col-md-5 col-sm-8">
          	<div class="input-group">
              <span class="input-group-addon"><i class="glyphicon glyphicon-phone"></i></span>
            <input type="text" class="form-control" name="mobile" id="contactnum" required placeholder="Enter your Primary contact no." value="">
            </div>
          </div>
        </div>
        <div class="form-group">
          <div class="col-xs-offset-3 col-md-8 col-sm-9"><span class="text-muted"><span class="label label-danger">Note:-</span> By clicking Sign Up, you agree to our <a href="#">Terms</a> and that you have read our <a href="#">Policy</a>, including our <a href="#">Cookie Use</a>.</span> </div>
        </div>
        <div class="form-group">
          <div class="col-xs-offset-3 col-xs-10">
            <input name="Submit" type="submit" value="Sign Up" class="btn btn-primary" required>
          </div>
        </div>
      </form>
      </section>
    </div>
</div>
</div>
<script type="text/javascript">

</script>
</body>
</html>

""")