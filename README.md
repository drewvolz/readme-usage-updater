# Readme Usage Updater

Updating usage for command line applications can be a chore, but it doesn't have to be!

This scripting can be thought of as 3 parts:
  - markup in your README,
  - a python script that diffs and updates,
  - conveniences which invoke the above step (via a Makefile, package.json script, etc).

## Usage

✨ This section below will update as the program is run either by invoking `./script/update-usage.py` or `make`.

<!--- START USAGE -->
```shell script
usage: readmeUsageUpdater [-h]

Update README usage as soon as the help is changed.

optional arguments:
  -h, --help  show this help message and exit
```
<!--- END USAGE -->

## Adopting this pattern in your project

1. Surround your current README's usage with a markdown comment followed by the markdown which precedes it:

   Add `<!--- START USAGE -->` and `<!--- END USAGE -->` around your usage markdown, e.g.

	    <!--- START USAGE -->
	    ```shell script
        <YOUR PROGRAM'S USAGE HERE>
	    ```
	    <!--- END USAGE -->

2. Edit `script/update-usage.py` which compares your program's usage against your current README. Note:
	  - Be sure you either match or change `shell script` to match your own document inside `update-usage.py`.
	  - Be sure you replace the program's name with the one you'd like to invoke e.g. replace `readmeUsageUpdater` with something else.

3. Invoke the script however you find most convenient. For one example, I've relied on `make` so there is a Makefile.

	```sh
	make
	```


## Play around

While this pattern does not require `argparser` as a dependency, this example is built to require it.

Requires Python 3.6+.

```shell script
$ pip install -r requirements-dev.txt
$ python3 example.py
```

Go ahead and modify the argparser definition in `example.py` and invoke the updater. The README should update.

1. Uncomment lines 19-23 and save (or modify another part of the argparser definition).

    ```py
    parser.add_argument('-o',
                         '--options',
                         required=False,
                         action='append',
                         help='the options to pass to the program')
	```

2. Run `make` or `python3 ./script/update-usage.py`
3. Run `git diff README.md` to see the changes.
