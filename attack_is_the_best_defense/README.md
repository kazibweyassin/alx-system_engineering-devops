

ssed

:ss:%d
 nginx on an ubuntu 16.06 server with redirect

# install nginx
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /var/www/html/

# configure default index page
echo 'School for the win!' > temp.html
sudo cp temp.html /var/www/html/index.html
rm temp.html

# configure 404 page
sudo mkdir -p /var/www/err/html
sudo touch /var/www/err/html/404.html
echo "Ceci n'est pas une page" | sudo tee /var/www/err/html/404.html

# configure redirect and 404 page in sites available
temp="server \{\n\tlisten 80 default_server;\n\tlisten \[::\]:80 default_server;\n\troot \/var\/www\/html;\n\tindex index.html index.htm index.nginx-debian.html;\n\tserver_name _;\n\terror_page 404 \/404.html;\n\tlocation \/404.html \{\n\t\troot \/var\/www\/err\/html;\n\t\tinternal;\n\t\}\n\tlocation \/redirect_me \{\n\t\treturn 301 https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4;\n\t\}\n\tlocation \/ \{\n\t\ttry_files \$uri \$uri\/ =404;\n\t\}\n\}"

sudo mkdir -p /etc/nginx/sites-available
sudo touch tempsite
echo "." | sudo tee tempsite
sudo sed -i -E "s/./$temp/" tempsite
sudo cp tempsite /etc/nginx/sites-available/default
sudo rm tempsite
sudo service nginx stop
sudo service nginx start
