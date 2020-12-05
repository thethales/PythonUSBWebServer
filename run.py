import os
import webbrowser
import yaml
from http.server import HTTPServer, CGIHTTPRequestHandler
from pathlib import Path

current_directory   = os.path.dirname(os.path.realpath(__file__))

try:
    config_file         = open("config.yaml")
    config              = yaml.load(config_file, Loader=yaml.FullLoader)
except:
  print("Unable to open configuration file. Make sure that the config.yaml is avalible at the .exe directory")





# Validate Config.yaml
if config["httpserver"]["port"] is None:
    print("Server port not configured, assuming default port: 8080")
    config["httpserver"]["port"] = 8080

if config["httpserver"]["directory"] is None:
    print("Server Directory not configured, assuming default directory: " + current_directory)
    config["httpserver"]["directory"] = current_directory

if config["webbrowser"]["open_url_after_launch"] is None:
    print("'Open URL After Launch' not configured, assuming default: True")
    config["webbrowser"]["open_url_after_launch"] = True

if config["webbrowser"]["window"] is None:
    print("'Browser tab configuration' not epecified, assuming default: 1 - A New Browser Windows is opned is possible")
    config["webbrowser"]["window"] = 1

if config["webbrowser"]["autoraise"] is None:
    print("'Browser windows autoraise' not epecified, assuming default: True")
    config["webbrowser"]["autoraise"] = True

if config["webbrowser"]["url"] is None:
    print("'Browser URL' not epecified, assuming default: http://localhost")
    config["webbrowser"]["url"] = 'http://localhost:' + str(config["httpserver"]["port"])





os.chdir(config["httpserver"]["directory"])
# Create server object 
server_object = HTTPServer(server_address=('', config["httpserver"]["port"]), RequestHandlerClass=CGIHTTPRequestHandler)

if config["webbrowser"]["open_url_after_launch"]:
    # Open Web Page on Default Browser if Possible
    webbrowser.open('http://localhost:8080', new=config["webbrowser"]["window"], autoraise=config["webbrowser"]["autoraise"])

server_object.serve_forever()



