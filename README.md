# EZSec Backend
_Python application to identify vulnerabilities to SQL, NoSQL injections and XSS._

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

## Important security reccomendations
Whether you run this backend in your own PC or at a virtual machine, make sure to:
- Create an specific user which executes the application, and ensure they do not have superuser privileges. While the application uses shlex and popen to mitigate shell injections, a step further is making it imposible to indirectly ruin your computer.
- Never pentest against a domain/web application which isn't yours without having written permission. Testing and attempting to use EZsec agaisnt a domain without the owner's permission could warrant legal action agaisnt yourself for which we are not responsible for. Use the tool wisely.

## Acknowledgements
- [Charlie Belmer](https://github.com/Charlie-belmer). Creator of nosqli who was nice enough to guide us through the integration of his tool with our own.
- [Miroslav Stampar](https://github.com/stamparm). Creator of Damn Small XSS Scanner and part of the sqlmap project. Guided us through the usage and integration of sqlmap and DSXS.
- [Juan Manuel Madrid](https://www.linkedin.com/in/juanmanuelmadrid/?originalSubdomain=co). Guide and tutor for our graduation project.

## Us
- [Marco Antonio Pérez](https://www.linkedin.com/in/marcopza/)
- [Jose Manuel Ossorio](https://www.linkedin.com/in/jose-ossorio-945848155/)
