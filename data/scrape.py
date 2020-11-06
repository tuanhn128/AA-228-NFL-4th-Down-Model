import pandas as pd
import os

# Code for scraping, cleaning, and saving compressed versions of play-by-play data.
# Gets every play from every year going back to 2006.
# References for nflfastR repository we used to pull the data from:
# https://github.com/mrcaseb/nflfastR
# https://gist.github.com/Deryck97/dff8d33e9f841568201a2a0d5519ac5e

if __name__ == '__main__':
    years = range(2006, 2021)
    data = pd.DataFrame()
    for yr in years:
        print('Year ' + str(yr) + ' started!')
        yearData = pd.read_csv('https://github.com/guga31bb/nflfastR-data/blob/master/data/play_by_play_'
                               + str(yr) + '.csv.gz?raw=True', compression='gzip', low_memory=False)
        data = data.append(yearData, sort=True)
    data.drop(['passer_player_name', 'passer_player_id', 'rusher_player_name', 'rusher_player_id',
               'receiver_player_name', 'receiver_player_id'], axis=1, inplace=True)
    data.to_csv('data.csv', compression='gzip', index=False)