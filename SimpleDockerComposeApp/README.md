### simple application using docker compose, flask, mysql and hopefully nginx

!!! Disclaimer this project is unfinished and unpolished. I couldn't finish what i wanted to do yet.
I used it to teach myself how to use docker compose with nginx !!!

To use you need Docker and docker compose (preferably on a Linux distribution)

here is a simple diagramm that represent how things work in my app:

![image](https://user-images.githubusercontent.com/49021870/195126564-eaf98fe3-43c7-4a79-9ec5-a2f4dfde691f.png)

to start the app with docker compose use:(sudo) docker compose up -d

and you should see something that look like this:

``` 

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
[+] Running 5/5
 ⠿ Network simpledockercomposeapp_backnet      Created                                                                                                                                                0.7s
 ⠿ Network simpledockercomposeapp_frontnet     Created                                                                                                                                                0.6s
 ⠿ Container simpledockercomposeapp-db-1       Healthy                                                                                                                                               17.1s
 ⠿ Container simpledockercomposeapp-backend-1  Started                                                                                                                                               19.8s
 ⠿ Container simpledockercomposeapp-proxy-1    Started  ```
 
My computer uses a VM with really limited ressources allocated so sometimes i get the db container unhealthy because it takes too much time to start.
If it happens to you don't worry and rerun the command "docker compose up -d" and it should work perfectly.


you should then be able to connect to the app with http://localhost:80/ and http://localhost:80/list

for now the first route "/" doesn't do anything except display an input bar, a title and a button.
the second route "/list" connect to the database and get countries and their capital.


