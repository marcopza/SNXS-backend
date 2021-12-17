# SNXS Backend
_SQL, NoSQL injection and XXS Scanner._

## Tools and Libraries
- [Shlex](https://docs.python.org/3/library/shlex.html)
- [Subprocess](https://docs.python.org/3/library/subprocess.html)
- [Django](https://www.djangoproject.com)
- [nosqli](https://github.com/Charlie-belmer/nosqli)
- [sqlmap](https://github.com/sqlmapproject/sqlmap)
- [DSXS(Dam Small XSS Scanner)](https://github.com/stamparm/DSXS)

## How to install needed tools
### Sqlmap
Follow the instructions described [here](https://github.com/sqlmapproject/sqlmap/blob/master/README.md). Make sure the executable is saved in a directory included in the Path. Also, the executable should be named sqlmap; rename if needed.
### NoSQLi
Download the latest binary version for Linux [here](https://github.com/Charlie-belmer/nosqli/releases)
First, make sure you give the executable proper permissions:
````shell
chmod +x 'executable_name'
````
Then, add the executable to a directory included in your _PATH_. Generally, you can just add the file to the /usr/local/bin directory. If you are unsure which directories belong are included in your path via running:
````shell
echo $PATH
````
Once the file's there, you should rename your file to _nosqli_. If not done, the application won't run.
### Go
Click [here](https://go.dev/dl/) to learn how to install Go.
### Python 3
Click [here](https://www.python.org/downloads/) to learn how to install Python3.
### Frontend
Click [here](https://github.com/jmossorio99/SNXS-frontend) to access the React GUI designed for this project.
## How to Run in development mode
Clone the repository:
````shell
git clone https://github.com/marcopza/SNXS-backend.git
````
Navigate to the folder and execute the following command:
````shell
python3 manage.py runserver
````
## Important security reccomendations
Whether you run this backend in your own PC or at a virtual machine, make sure to:
- Create an specific user which executes the application, and ensure they do not have superuser privileges. While the application uses shlex and popen to mitigate shell injections, a step further is making it imposible to indirectly ruin your computer.
- Never pentest against a domain/web application which isn't yours without having written permission. Testing and attempting to use SNXS agaisnt a domain without the owner's permission could warrant legal action agaisnt yourself for which we are not responsible for. Use the tool wisely.

## Outputs and vulnerability coverage:
Our application is in no shape or form a silver bullet for detecting SQL, NoSQL injections and XSS. There are a few points to have in mind:
- Only MongoDB injections are scanned; NoSQLi reports it does work to a certain degree to JS based databases.
- False positives and false negatives are always a possibility when using the application; make sure to properly test each of the vulnerabilities to make ensure the existance of one. Remember to always have written consent!

## Acknowledgements
- [Charlie Belmer](https://github.com/Charlie-belmer). Creator of nosqli who was nice enough to guide us through the integration of his tool with our own.
- [Miroslav Stampar](https://github.com/stamparm). Creator of Damn Small XSS Scanner and part of the sqlmap project. Guided us through the usage and integration of sqlmap and DSXS.
- [Juan Manuel Madrid](https://www.linkedin.com/in/juanmanuelmadrid/?originalSubdomain=co). Guide and tutor for our graduation project.

## Us
- [Marco Antonio Pérez](https://www.linkedin.com/in/marcopza/)
- [Jose Manuel Ossorio](https://www.linkedin.com/in/jose-ossorio-945848155/)
