# Commands on EC2 instance

### ps aux

![image1](/week1/ej_2_linux_basics/img/image1.png)

## Practice 1

```bash
# Start a background process
sleep 300 &

# Note the PID it shows
# Now find it
ps aux | grep sleep

# See its parent
ps -o pid,ppid,cmd -p <PID>
```
![image2](/week1/ej_2_linux_basics/img/image2.png)

## Practice 2

```bash
# Terminal 1:
stress-ng --cpu 2 --timeout 120s

# Terminal 2:
# Monitor and answer:
# 1. What's the load average?
uptime
Answer: 1.20 at time of execution

# 2. Which process is using CPU?
top
Answer: 27189, 27190

# 3. What's the total CPU usage?
top    # Look at %Cpu(s) line
Answer: 100% cpu usage for each process
```
![image3](/week1/ej_2_linux_basics/img/image3.png)

## Practice 3

### Find out:
#### 1. How much memory is available?
free -h | grep Mem | awk '{print $7}'
Answer: 104Mi

#### 2. What process uses most memory?
ps aux --sort=-%mem | head -2
Answer: ec2-user   29708 98.8 28.1 323340 264040 pts/0   R+   11:24   0:37 stress-ng-vm [run]

#### 3. How much memory does stress-ng use?
pgrep stress-ng | head -1 | xargs ps -o pid,cmd,%mem -p
Answer:     

```bash
PID CMD                         %MEM
29704 stress-ng --vm 2 --vm-bytes  0.7
```

![image4](/week1/ej_2_linux_basics/img/image4.png)

## Exercise 1: CPU Hunt

```bash
# Generate CPU load
stress-ng --cpu 2 --timeout 300s &

# Your tasks:
# 1. Find the PID of stress-ng
pgrep stress-ng

# 2. What's its CPU usage?
ps -p <PID> -o %cpu

# 3. Lower its priority
renice 10 <PID>

# 4. Monitor for 30 seconds
top -p <PID> -d 1 -n 30

# 5. Kill it
kill <PID>
```
![image5](/week1/ej_2_linux_basics/img/image5.png)

## Exercise 2: Memory Investigation

```bash
# Generate memory load
stress-ng --vm 1 --vm-bytes 500M --timeout 300s &

# Your tasks:
# 1. How much memory is it using?
ps aux | grep stress-ng | grep -v grep | awk '{print $4 "%"}'

# 2. Get exact RSS value
ps -p <PID> -o rss

# 3. Watch it for 1 minute
watch -n 5 "ps -p <PID> -o pid,cmd,%mem,rss"

# 4. Check if system is swapping
vmstat 1 10 | awk '{print $7, $8}'
```
![image6](/week1/ej_2_linux_basics/img/image6.png)
---

## Exercise 3: I/O Testing

```bash
# Generate I/O
dd if=/dev/zero of=/tmp/bigfile bs=1M count=5000 &
DD_PID=$!

# Your tasks:
# 1. What's the iowait?
iostat 1 5 | grep -A1 avg-cpu

# 2. Which process is doing I/O?
sudo iotop -o -b -n 1

# 3. How much data written?
iostat -x 1 5 | grep nvme

# 4. Kill the dd process
kill $DD_PID
rm /tmp/bigfile
```
![image7](/week1/ej_2_linux_basics/img/image7.png)