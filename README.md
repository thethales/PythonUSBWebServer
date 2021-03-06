# PythonUSBWebServer

![](img/logo_pythonusbwebserver.ico)


A simple standalone http webserver based on python, leveraging Python's built-in ```http.server``` library.
allowing for the delivery of any static content on your local desktop environment trough your browser.


## What is for ?

![PythonUSBWebServer](docs/screenshots/PythonUSBWebServer_2020-12-05_19-06-10.png)

Originally, I designed this software to bundle [MdWiki](http://dynalon.github.io/mdwiki/#!index.md) static web pages into a singles package. But given the nature of a Webserver, it can be used to a wide variaty of cases, for example in a USB drive or a shared folder.

_Note: using this software as a web server exposed to the public internet _it's not recommended_, since that would require probably a whole new tier of security measures._


## How To Use

1. Just drop both the _.exe_ and _config.yaml_ into any windows folder (You can grab the lastest version [here](https://github.com/thethales/PythonUSBWebServer/releases))
2. That's it. The server will serve the files following the configurations of the [config.yaml](config.yaml) file.



# Development


For developing new features for this repo or your own, you can follow the instructions listed below. (Any pull request or issues are more than welcome).

1. Check the [prerequistes list](README.md#Development##Prerequisites) and confirm that everything is in order
2. Clone the repository

    ```shell
    git clone https://github.com/thethales/PythonUSBWebServer

    ```

3. Install Python dependencies

    ```shell
    pip install pyyaml
    pip install auto-py-to-exe

    ```

## Prerequisites

- This project is based on the Python Programming Language and requires Python 3.8 or above. You can obtain a free copy of Python [here](https://www.python.org/downloads/)
- To generate the Windows binaries you will need the [Auto-Py-To-Exe](https://pypi.org/project/auto-py-to-exe/), see the Python Dependencies for instructions.


# Configuring and Setup

The webserver offers some customization parameters. The full list is presented below. All parameters are kept at the ```config.yaml``` file.

```httpserver```: This parent key, holds all configuration attributes related to the ```http.server``
 
|Key|Type|Description|Default|
|---|----|-----------|-------|
|port|```integer```| Specifies the web server port. Make sure to fill in a avaliable port, current version does not check for port avaliability | 8080 |
|directory| ```string```| Specifies the directory to run server and serve the webpages| Current directory|

```webbrowser```: This parent key, defines attributes for the optional _open webpage_ function
 
|Key|Type|Description|Default|
|---|----|-----------|-------|
|open_url_after_launch| ```boolean```| If ```true``` opens the webserver url after launch on the default OS browser| ```true```|
|window| ```integer```| Displays the url using the default browser. If  0, the url is opened in the same browser window if possible. If the value is 1, a new browser window is opened if possible. If value is 2, a new browser page (“tab”) is opened if possible. | ```0```|
|autoraise| ```boolean``` | If autoraise is True, the window is raised if possible (note that under many window managers this will occur regardless of the setting of this variable). |```true```|
|url|```string``` |Specifies custom URL | _http://localhost:<server_port>_  e.g. _http://localhost:8080_|

# FAQ

```Q:``` What platforms are supported ?

```A:``` Currently only windows is officially supported, though, since the software is designed in Python, you can run the script in any platform. To do so, make sure to download both [run.py](run.py) and [config.yaml](config.yaml)



```Q:``` PHP ?

```A:``` That crossed my mind, but I have yet to look at it.
