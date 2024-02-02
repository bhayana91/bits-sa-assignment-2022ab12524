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

Download Minikube

    brew install minikube

After running minikube start, which spins up a local cluster, running few commands to check the status of the cluster.
    ```
    kubectl version
    kubectl version --client
    minikube status
    minikube ip
    minikube service list
    ```
Now to get the deployment status, we run     
    kubectl get deployments

In order to get pods, run 
    kubectl get pods

To view pods,
    kubectl exec -it python-flask-app-deployment-8cb5c5c65-297qt -- /bin/sh

To describe the pod,
    kubectl describe pod python-flask-app-deployment-8cb5c5c65-jplmc

Now to check the application hosted by the pods, access the service using minikube IPs
    kubectl expose deployment python-flask-app-deployment --type=NodePort --port=8080
    minikube service python-flask-app-deployment

