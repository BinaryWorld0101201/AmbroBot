# AmbroBot
AmbroBot is a Bot that learns new commands as i get more things to study. Studying sometimes is boring. Coding is always fun (and a good excuse to not feel guilty about not studying).

It can set reminders, search series or movies for you, tell you if you should take the subway or not, and even help you solve system of linear equations!


## Installation
First clone the project and install requirements.
```bash
$ git clone https://github.com/Ambro17/AmbroBot.git
$ cd AmbroBot
$ pip install -r requirements.txt
```

Then open telegram and chat `@BotFather` to get a bot token. Once you have it add `PYTEL` environment variable with the token.
For example, if you use Linux with zsh shell you should add this line to the end of your ~/.zshrc file
`export PYTEL=<BotToken>`

If you are on windows you can do it with a GUI, or with powershell. See [this link](https://superuser.com/questions/949560/how-do-i-set-system-environment-variables-in-windows-10) for instructions

Additional environment variables are needed for the bot to work properly. 

```
TMDB_KEY # To access movies and series
DATABASE_URL # Database to persist information
CABA_SECRET # Transport updates
CABA_CLI_ID # Transport updates
```

## Bot in action

**Search series by name**

![Serie output](https://i.imgur.com/Kx0bvyz.jpg "Sherlock")



**Search movie by name**

![Movie output](https://i.imgur.com/mWRG1HH.jpg "Matrix")



**Get yts latest movies**

![Yts movies](https://i.imgur.com/wpq84zo.jpg "Yts")



**Get subte status of Buenos Aires City**

![Subte status](https://i.imgur.com/Z0Aacyd.png "Subte")



## Commands List
```/partido```

Outputs San Lorenzo's next match

```/dolar```

Outputs USD->ARS exchange rates from different banks.

```/remind <something>```

Set reminders of todo tasks with recurrent notifications

```/rofex```

Outputs the rofex expected USD->ARS exchange rate in the following months

```/posiciones```

Outputs Liga Argentina standings

```/subte```

Outputs status of CABA subway lines.

```/cartelera```

Outputs the most popular movies available at the cinemas

```/hoypido```

Outputs hoypido food offers of the week

```/pelicula <pelicula>```

Outputs rating, description and imdb, yt and .torrent links to the requested movie.

```/serie <serie>```

Outputs all series episodes along with small description of the series.

```/yts```

Show latest movies added on yts.ag

```/feriados```

Show next feriados for Argentina

```/aproximar```

Determine solution of diagonally dominant system of linear equations via Jacobi or Gauss Seidel iterative methods



## Credits

Feel free to modify this code to suit your needs. If you get inspired by this bot please reference this repo as source of inspiration.  ⭐️ Stars, issues and PRs are appreciated!
