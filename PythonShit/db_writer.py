import cx_Oracle

writer = {
    "id": 1,
    "name": "Bitcoin",
    "symbol": "BTC",
    "slug": "bitcoin",
    "num_market_pairs": 8537,
    "date_added": "2013-04-28T00:00:00.000Z",
    "cmc_rank": 1,
    "last_updated": "2021-10-03T21:12:02.000Z",
    "price": 48163.65748827895,
    "volume_24h": 27017622875.13175,
    "percent_change_1h": -1.26783014,
    "percent_change_24h": 0.12180723,
    "percent_change_7d": 10.51834374,
    "percent_change_30d": -4.13727638,
    "percent_change_60d": 20.88102849,
    "percent_change_90d": 41.56757615,
    "market_cap": 907104692402.748,
    "market_cap_dominance": 42.2011,
    "fully_diluted_market_cap": 1011436807253.86,
    }
cx_Oracle.init_oracle_client("D:\Tools\Oracle18c\instantclient_19_12")
conn = cx_Oracle.connect(user="system", password="Blanadeurs@87", dsn="localhost:1521")
c = conn.cursor()
sutff_in_string = f"insert into crypto_coins(id,name,symbol,slug,num_market_pairs,date_added,cmc_rank,last_updated," \
                  f"price,volume_24h,percent_change_1h,percent_change_24h,percent_change_7d,percent_change_30d," \
                  f"percent_change_60d,percent_change_90d,market_cap,market_cap_dominance,fully_diluted_market_cap) " \
                  f"values ({writer['id']}, {writer['name']}, {writer['symbol']}, {writer['slug']}, {writer['num_market_pairs']}," \
                  f"{writer['date_added']}, {writer['cmc_rank']}, {writer['last_updated']}, {writer['price']}, {writer['volume_24h']}," \
                  f"{writer['percent_change_1h']}, {writer['percent_change_24h']}, {writer['percent_change_7d']}," \
                  f"{writer['percent_change_30d']}, {writer['percent_change_60d']}, {writer['percent_change_90d']}," \
                  f"{writer['market_cap']}, {writer['market_cap_dominance']}, {writer['fully_diluted_market_cap']}); "
print(sutff_in_string)
c.execute(sutff_in_string)
c.execute('select * from crypto_coins')
for row in c:
    print(row[0], '-', row[1])
conn.close()
