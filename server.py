'''
 This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

'''Authors: Jacob Wakefield'''

from gevent import monkey
from Server import app
import webbrowser
from gevent.pywsgi import WSGIServer
from gevent.pool import Pool as gPool

PORT = 5000

def main(): 
    pool = gPool(1000) #create thread pool with a limit of 1000
    http_server = WSGIServer(('0.0.0.0', PORT), app, spawn=pool) #create wsgi server 
    
    url = "http://localhost:"+str(PORT)+"/"
    webbrowser.open(url, new=2) #Opens in new tab if possible
    http_server.serve_forever()

if __name__ == "__main__":    
    main()
