# dev_portfolio_simplified
Customizable Professional Developer Portfolio for Beginners with Docker Stack

<a href="https://youtu.be/RZpMevjnLR8"><img src="https://github.com/user-attachments/assets/d32f32b1-a656-41ab-affd-5d58415d5023" width=600px></a>

## Instructions

```
docker compose up
```

OR 

```
docker build -t my-portfolio .
docker swarm init
docker stack deploy -c docker-compose.yml my-portfolio
```

THEN TYPE IN THE BROWSER: 
<br>
`localhost:80` or `localhost`

TO UPDATE DATABASE WHILE SITE IS LIVE:

```
docker exec 562fba672bdd python3 /app/init_db.py
```
