### Requirement
```
python 2.7
pip
```
### Set up
1. Clone or download the repo. cd into `crawler` folder,
2. Run `pip install -r requirement.txt` to install python packages.
3. Create a `config.yaml` based on `conig.yaml.example`.
4. Fill in the steam api key in `crawler/config.yaml`. You can also specify the images output path (default `images/`).
5. Run crawler. e.g. `python items_crawler.py`.
6. When it finish, check the result in `images/xxx`.

### Config
If there are any update in items or heros, you need to manually update information in `model/heros.yaml` or `model/items.yaml`

### Filename Specification
##### Heros
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

### TODO
* 战队队员
* 战队Logo