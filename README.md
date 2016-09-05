### Requirement
```
python 2.7
pip
Docker
```

### Set up
0. Install Docker.
1. Clone or download the repo. `cd` to the repo. `git checkout Docker` to choose Docker branch.
2. Need to update all git submodule as well: `git submodule update --recursive`.
3. Build the docker `docker build -t static-server .`
4. After build, run the docker with `docker run -p 8000:80 -d static-server`. (default run on host port 8000)
5. Now checkout the served images, for example, `localhost:8000/items/aegis_lg.png`.

### Config
- For Docker configs, update in `Dockerfile`. You can set up environment varible in `Dockerfile` such as Databse connection.
- For Cron job configs, update in `crontab`.
- For the script to run crawler, check `run_crawler.sh` in crawler folder.

### Filename Specification
##### Heroes
```
HERO_NAME_full.png
HERO_NAME_lg.png
HERO_NAME_sb.png
HERO_NAME_vert.jpg
```
e.g. `axe_full.png`

##### Items
```
ITEM_NAME_eg.png
ITEM_NAME_lg.png
```
e.g. `basher_lg.png`

##### Leagues
```
LEAGUE_ID_ticket.png
LEAGUE_ID_ticket_large.png
LEAGUE_ID_ingame.png
```
e.g. `1490_ticket.png`

##### Teams
```
TEAM_ID_logo.png
TEAM_ID_sponsor.png
```
e.g. `15_ticket.png`

### TODO
* Teams的数据库连接
