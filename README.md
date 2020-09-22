# PCC Technical Task

Our take-home is a brief test of your fundamental programming knowledge. It's hopefully much shorter than most take-homes you will encounter. This is because we feel that your time is valuable, and we do not want our test to be biased against people who have a busy schedule.

We do not expect servers, or React apps so please don't feel like you need to spend hours adding these.
If you pass this test, you will have the opportunity to expand on it and demonstrate your skills during an on-site pair programming interview.

**The Task:**

The English Premier League is the top-tier league of soccer (football) teams, which consists of 20 teams. Every year, each team in the league play 38 matches (2 matches against every other team).

At the end of the season, the team with the most points wins the Premier League title. The bottom three teams are relegated to the Championship League, which is the league one tier below the Premier League. The top 4 teams are eligible to play in the UEFA Champions League the next season, and teams ranked 5 and 6 are eligible to play in the Europa League.

Each win is worth 3 points, each tie is worth 1 point, and a loss does not give a team any points.

We would like you to create a function which generates the Premier League table (ie: the standings).

Given the full list of matches in the season from
https://github.com/openfootball/football.json/blob/master/2016-17/en.1.json
your script must output a sorted array containing the following information for each team:

* rank
* team name
* wins
* draws
* losses
* goals for (total number of goals scored by the team across all matches)
* goals against (total number of goals scored against the team across all matches)
* goal difference
* points

The array must be sorted by rank. Rank is determined by points, then goal difference, then goals scored.

There is a starter script in main.py or here: https://repl.it/@rjmackay/pcc-tech-task-starter

**What we’re looking for:**

Clean, well structured code that outputs the correct results for the 2016-17 season. We are interested both in how you approach the problem and how you validate the output from your solution.
