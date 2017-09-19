# sql-logs-analysis

Python Project for Udacity Full Stack Nanodegree: Analyses Server logs file with SQL queries

## Installation

First, fork this repository, or Download it as a .zip from Github.

In your Terminal, navigate to the directory where the files were downloaded, and execute  `beginanalysis.py` with your python interpreter.

On a Mac, this means

```sh
$ python beginanalysis.py
```

## Before you begin

1. You must have 'psycopg2' module installed

2. You need a 'news' database set up through postGREsql.  This can be done by downloading 'newsdata.sql' from the [zipped file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), extracting, navigating to that directory and running
```sh
$ psql -d news -f newsdata.sql
```

3. Ensure 'beginanalysis.py' is in the same directory as 'newsdata.sql'.

## How to Contribute

Contributions are welcome!

First, fork this repository.

Next, clone this repository to your desktop to make changes.

```sh
$ git clone {git@github.com:nathanoldridge/sql-logs-analysis.git}
$ cd sql-logs-analysis
```

Once you've pushed changes to your local repository, you can issue a pull request by clicking on the green pull request icon.

Instead of cloning the repository to your desktop, you can also go to `README.md` in your fork on GitHub.com, hit the Edit button (the button with the pencil) to edit the file in your browser, then hit the `Propose file change` button, and finally make a pull request. 

## License

The contents of this repository are covered under [the Unlicense](https://choosealicense.com/licenses/unlicense/)

## Contact

Questions, comments and suggestions can be sent to Nathan Oldridge at <http://www.tnathan.com>
