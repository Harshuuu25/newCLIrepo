# !/bin/bash
# use this for your user data (script from top to bottom)
# install httpd(linux 2 version )
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello World from $(hostname -f)</h>" > /var/www/html/index.html 