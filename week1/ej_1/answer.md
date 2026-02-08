# on one shell
docker-compose up 

on another shell(terminal)
chmod u+x log-collection.sh
./log-collection.sh


# open one more terminal 

follow exercise.md

# Step 1: Create Directory and Files

![imagen1](/week1/ej_1/img/image1.png)

# Step 2: Start the Lab

```bash
# Start containers
docker-compose up -d
```

![imagen2](/week1/ej_1/img/image2.png)

```bash
# Check if containers are running
docker ps

# You should see:
# - flask-app (running Flask on port 8080)
# - log-generator (generating traffic)
```

![imagen3](/week1/ej_1/img/image3.png)


# Step 3: View Logs in Real-Time

```bash
# View Flask app logs (this is your access log)
docker logs -f flask-app

# You'll see Apache-style logs like:
# 192.168.1.100 - - [27/Jan/2026:10:30:45 +0000] "GET /api/users HTTP/1.1" 200 2341 "-" "Mozilla/5.0..."
```

v

### Step 4: Save Logs to File for Analysis

```bash
# Save current logs to file
docker logs flask-app > access.log

# Or continuously save logs
docker logs -f flask-app >> access.log
```

![imagen5](/week1/ej_1/img/image5.png)

### Step 5: Start Analyzing

```bash
# Now use all the commands from the lab!

# Top 10 IPs
awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -10

# Error rate
awk '$9 >= 400' access.log | wc -l

# Most hit endpoints
awk '{print $7}' access.log | sort | uniq -c | sort -nr | head -10

# Follow logs live with grep
docker logs -f flask-app | grep --color=auto -E " (4|5)[0-9]{2} "
```

![imagen6](/week1/ej_1/img/image6.png)

* Note: Made one command to prove all working good. All other steps described are some sort of greping the access.log.

