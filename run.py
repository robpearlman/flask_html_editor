# run.py

import os
from project import app

#for production
#port = int(os.environ.get('PORT', 5000)) 
#app.run(host='0.0.0.0', port=port)

#for testing
#app.run(debug=True)

if __name__ == '__main__':
    if app.config['DEBUG']:
        app.run(debug=True, host='0.0.0.0')
    else:
        port = int(os.environ.get('PORT', 5000)) 
        app.run(host='0.0.0.0', port=port)
