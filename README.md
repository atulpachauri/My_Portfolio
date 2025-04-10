# dev_portfolio_simplified
Customizable Professional Developer Portfolio for Beginners with Docker Stack

**REPO IN THE WORKS - NOT READY YET**

## Instructions

```
docker build -t my-portfolio .
docker run -p 80:5000 -v .:/app my-portfolio
```

OR 

```
docker swarm init
docker stack deploy -c docker-compose.yml my-portfolio
```

THEN TYPE IN THE BROWSER: 
<br>
`localhost:80` or `localhost`