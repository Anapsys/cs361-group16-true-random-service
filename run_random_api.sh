# first make it executable in your Git Bash shell:
# chmod +x run_random_api.sh

#!/bin/bash

# start uvicorn let it run in the background
uvicorn random_number_generator:app --reload --host 127.0.0.1 --port 8010 &


sleep 2

# deliver to default browser 
explorer.exe "http://127.0.0.1:8010/random_number_generator"

echo "Server running on http://127.0.0.1:8010/random_number_generator"
