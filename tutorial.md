Nginx:
Think about  you have run up many instances of your application and 
every each of them is dedicated to a particular port so that your
application is available to users in many ports.
Now It is confusing for user to guess on which port there is too much load.
In that part nginx gives a hand and says to user you do not 
necessarily know all the ports that application serves on
just one default port 443 of nginx.
Nginx takes all the request from users and smartly manages 
the load. It knows which server has low amount of load 
redirect the request that port.
The other thing nginx does is loading up cache and it caches
requests to be served for the next time it gets the same request
it servers without talking to infrastructure again and again.


static files are served by nginx (js, css, jpg)-
it is because web servers are specialized for serving static
files.

nginx web server talks to application server(gunicorn) and 
it speacks to web framework(django)

nginx acts as a proxy, as a webserver, and as a load balancer
it servers static content like a webserver, it forwards request
to backend services like a proxy and depending of the load of
applications nginx find out appropriate instace to forward
request