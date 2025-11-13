Python Libraries Required:

pip install opencv-Python

pip install yt-dlp

pip install numpy

pip install fastapi

pip install uvicorn

------------------------------

To run it:
Go to a Git bash shell (make sure it's in the right directory) and run:

(only run it once to make the .sh file executable)
chmod +x run_random_api.sh 

(after running the above script you can just run this each time)
./run_random_api.sh

After running it, you should see a long list of things.
I include important values here just to show the bigger picture of what's being returned.

Such as:

You will see a 3D array like this:
(This is the dimensions of the frame from the livestream)

[[[  0   0   0]
  [  0   0   0]
  [ 41  24  27]
  ...
  [  0   0   0]
  [  0   0   0]
  [  0   0   0]]]


Frame Dimensions:
(1080, 1920, 3)
^^^^ The video is in 1080px so it make sense, it will reflect it as such.
1920px accross and 3 channels of BGR values (color) for each pixel.

Random Pixel Indices = 38 1678 1
(From the function, this is just an example indices that makes up a single pixel)

Random Pixel [BGR Values] = [121  17  23]
(This is an example of the BGR values of a random selectd pixel)

Random Pixel BGR Value = 17
^^^^^ The API returns a dictionary object:
{"Random Number": n}

Note: The 3D array, Frame Dimensions, Random Pixel Indices, Random Pixel [BGR Values]
are all just print statements in the terminal. The only value being returned into a browser
is the "Random Pixel BGR Value" which is a dictionary object that you can fetch via JS.

Note: @app.get("/random_number_generator") this is the GET request for the function.

Note: the script will create a _pycache_ folder with logs