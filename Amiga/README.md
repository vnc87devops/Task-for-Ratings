Firstly I have done the coding using python

created dockerfile with set of commands and build image from that

ex: docker build -t imagename .

docker build -t myimage .
Run the container using dockerimage by passing arguments like

ex: docker run imageName python /src/python.py(file address) "movie name"

docker run myimage python /src/python.py "avatar"

Finally we can get the Rotten Tomatoes value

ex: Rotten Tomatoes:82%
