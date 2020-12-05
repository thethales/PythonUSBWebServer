# PythonUSBWebServer

A simple standalone http webserver based on python, leveraging Python's built-in ```http.server``` library




# Dev

```
pip install pyyaml

```



# Config YAML


```webbrowser```
 
|Key|Type|Description|Default|
|---|----|-----------|-------|
|port|```integer```| Specifies the web server port. Make sure to fill in a avaliable port, current version does not check for port avaliability | 8080 |
|directory| ```string```| Specifies the directory to run server and serve the webpages| Current directory|

```webbrowser```
 
|Key|Type|Description|Default|
|---|----|-----------|-------|
|open_url_after_launch| ```boolean```| If ```true``` opens the webserver url after launch on the default OS browser| ```true```|
|window| ```integer```| Displays the url using the default browser. If  0, the url is opened in the same browser window if possible. If the value is 1, a new browser window is opened if possible. If value is 2, a new browser page (“tab”) is opened if possible. | ```0```|
|autoraise| ```boolean``` | If autoraise is True, the window is raised if possible (note that under many window managers this will occur regardless of the setting of this variable). |```true```|
|url|```string``` |Specifies custom URL | _http://localhost:<server_port>_  e.g. _http://localhost:8080_|