# March Madness Predictor with Statistics

# Intro
March Madness in my opinion is one of the most exhillarating times of the year. 64 teams, 63 games, 1 champion. The concept of the march madness bracket seems easy. Pick a winner for all 63 games, in the hopes of having a 100% accuracy and a shot at millions of dollars. However, this feat has never been done before. The game of basketball has many statistics: shooting percentage, free throw percentage, points per game, and so on. This got me thinking... is there a way to predict the winners of each game by comparing the statistics of two teams and choosing the "statistically better team"? Furthermore, there were two main reasons for this data analytics program. One, I dont follow college basketball except when it comes to March, therefore, I needed to compare the two teams in some way. Two, writing a program is much more efficient than manually comparing two teams 63 times.

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
For this project, I used [sportsreference's API](https://sportsipy.readthedocs.io/en/latest/ncaab.html#module-sportsipy.ncaab.teams) which was an efficient way to gather and use the data. 

### Trial and error
The initial idea was relatively simple. First, I would enter in the two team names that I would like to compare and get their respective dataframes (a simple way of accessing the season stats of each team). These dataframes were passed into a compare method which would take a category, see which team was better in the certain category, and finally, increment the "score" of whichever team was better in said category.

After running the code for the first time, it came to my attention that not every team had played the same amount of regular season games for some reason. For example, Virginia played 25 games (18-7 overall record) whereas Baylor played 28 games (26-2 overall record). This would mean that the amount of points, rebounds, etc (anything that isn't a percentage) could possibly be higher for the team that played more games. To fix this, any statistic that wasn't a percentage would be divided by the amount of games that the team played. The new category list looked like this (dont worry about the numbers, I will explain that in the next paragraph) : 
- 4 Effective field goal % 
- 3 Free throw %
- 3 Field goal attempts / game
- 3 Free throw attempts / game
- 3 Offensive rating
- 3 Defensive rating
- 2 True shooting %
- 2 Rebounds / game
- 2 Points / game
- 2 Wins / game
- 2 Turnovers / game
- 2 Opponent points / game
- 2 Fouls / game
- 1 Assists / game
- 1 Blocks / game
- 1 Steals / game

Doing this fixed the problem of unequal stats, but brought up another problem. I simulated the entire bracket and ended up with an unusal winner - 14 seeded Colgate. After a bit of investigation, I realized the reason behind this. Some statistics (like effective field goal % and free throw %) play a bigger role / have more importance than others (like steals per game), however, I was giving equal importance to all of these. The most logical solution was to give each category a certain "weight" indicating their importance. This in turn would increment the teams points by that weight. For example, if team A had a higher EFG% and team B had a higher assist/game value, team A would get 4 points and team B would only get 1. The numbers in the list above denote each categories "weights".

The final addition I made to the program was to factor in strength of schedule and pace (# of possessions per game). Strength of schedule was necessary as some teams had relatively easier schedules than others, meaning this needed to be factored in. Pace was added in order to make the max amount of points an odd number (to avoid ties). These categories were weighted 2 and 3 respectively.
