function check() 
        {
            if (document.getElementById('serverpsw').value!=document.getElementById('confirmpsw').value)
            {
                document.getElementById('message').style.color = 'red';
                document.getElementById('message').innerHTML = 'Passwords do not match';
            }
        }
        function checkusername()
        {
            var a=document.getElementById("username").value;
            //alert(a);
            var u=/[A-Z]/g;
            var n=/[0-9]/g;
            if(a.match(u) && a.match(n))
            {
                document.getElementById("username1").innerHTML="";
            }
            else
            {
                document.getElementById('username1').style.color = 'red';
                document.getElementById("username1").innerHTML="Invalid Username";
            }
        }
        function popup()
        {
            var a=document.getElementById("Mname").value;
            b=document.getElementById("mail").value;
            c=document.getElementById("username").value;
            d=document.getElementById("serverpsw").value;
            e=document.getElementById("confirmpsw").value;
            f=document.getElementById("tlead").value;
            if(a==""||b==""||c==""||d==""||e==""||f=="")
            {
                alert("Please enter all fields");
            }
            else
            {
                alert("Manager Name: "+a+"\n"+"Mail: "+b+"\n"+"Username: "+c+"\n"+"Lead: "+f);
            }
        }