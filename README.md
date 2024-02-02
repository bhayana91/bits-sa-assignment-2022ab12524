# BITS Assignment Solution

Docker HUB Repo [URL](https://hub.docker.com/r/sidhantbhayana170/bits-assignment/tags)

Docker Build command to build the image

    docker build -t sidhantbhayana170/bits-assignment:2022ab12524 .

Docker run container locally to test

    docker run --name my-container -d -p 8080:8080 sidhantbhayana170/bits-assignment:2022ab12524

Docker push image to the hub personal repository

    docker push sidhantbhayana170/bits-assignment:2022ab12524

Docker pull image from the hub repo

    docker pull sidhantbhayana170/bits-assignment:2022ab12524
