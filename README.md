# March Madness Predictor with Statistics

# Intro
March Madness in my opinion is one of the most exhillarating times of the year. 64 teams, 63 games, 1 champion. The concept of the march madness bracket seems easy. Pick a winner for all 63 games, in the hopes of having a 100% accuracy and a shot at millions of dollars. However, this feat has never been done before. The game of basketball has many statistics: shooting percentage, free throw percentage, points per game, and so on. This got me thinking... is there a way to predict the winners of each game by comparing the statistics of two teams and choosing the "statistically better team"? Furthermore, there were two main reasons for writing this program. One, I dont follow college basketball except when it comes to March, therefore, I needed to compare the two teams in some way. Two, writing a program is much more efficient than manually comparing two teams for 63 games. 

# The program
### The stats
The first part of this whole project was figuring out which statistics I needed to use. After lots of online research and asking a couple friends that know much more basketball than I do, I compiled a list of the stats I thought were of the most importance in college basketball. These stats were:
- Effective field goal %
- Free throw %
- Field goal attempts
- Free throw attempts
- Offensive rating
- Defensive rating
- True shooting %
- Rebounds
- Points
- Wins
- Turnovers
- Opponent points
- Fouls
- Assists
- Blocks
- Steals

### Gathering the data 
At first, it seemed daunting. How was I going to import this season's NCAAB data into my program in an efficient way? Thankfully, there was a way. Using the [sportsreference API](https://sportsipy.readthedocs.io/en/latest/ncaab.html#module-sportsipy.ncaab.teams), I was able to directly take this seasons data and use it to make the bracket.

### Trial and error
The initial code was relatively simple. First, I would enter in the two team names that I would like to compare and get their respective dataframes (a simple way of accessing the season stats of each team). These dataframes were passed into a compare method which would find a category, see which team was better in the certain category, and finally, increment the "score" of whichever team 
