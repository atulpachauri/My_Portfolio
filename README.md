# dev_portfolio_simplified
Customizable Professional Developer Portfolio for Beginners with Docker Stack

<a href="https://youtu.be/RZpMevjnLR8"><img src="https://github.com/user-attachments/assets/8ce05e61-6050-4c82-8c1e-f45e16c88919" width=600px></a>

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
