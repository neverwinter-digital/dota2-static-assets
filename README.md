### Requirement
```
python 2.7
pip
Docker
```

### Set up
0. Install Docker.
1. Clone or download the repo. `cd` to the repo. `git checkout Docker` to choose Docker branch.
2. Need to update all git submodule as well: `git submodule update --init --recursive`.
3. Run `cat Dockerfile.example | envsubst >> "Dockerfile"` to populate the Dockerfile with environment variables.
4. Build the docker `docker build -t static-server .`
5. After build, run the docker with `docker run -t -p <port>:80 -d static-server -v /mnt/static_server:/var/www` on the specific port you want. You can also specify the volumn for the docker data.
6. Now checkout the served images, for example, `<ip>:<port>/items/aegis_lg.png`.

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
