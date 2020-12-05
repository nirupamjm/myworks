
# KochiOrgBook  Demo


## Steps

        Step 1 : docker pull nirupamjm/njmaxc
        Step 2 : sudo docker run -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --user="$(id --user):$(id --group)" nirupamjm/njmaxc:latest
