
```bash
GCP_PROJ_ID="my-proj-id"
GCP_REGION="europe-west2"
GCP_ARTIFACT_REG_REPO_NAME="temp-test"
GCP_ARTIFACT_REG_REPO_PATH=$GCP_REGION-docker.pkg.dev/$GCP_PROJ_ID/$GCP_ARTIFACT_REG_REPO_NAME
GCP_ARTIFACT_REG_REPO_DESCRIP="Storage for my toy docker containers while I was learning Google Kubernetes Engine (GKE)"
GCP_ARTIFACT_REG_CONTAINER_IMG_NAME="toy-flask-app"

gcloud config set project $GCP_PROJ_ID
gcloud config set run/region $GCP_REGION

# create the repository on google cloud artifact registry #
gcloud artifacts repositories create $GCP_ARTIFACT_REG_REPO_NAME  \
    --project=$GCP_PROJ_ID \
    --repository-format=docker \
    --location=$GCP_REGION \
    --description=$GCP_ARTIFACT_REG_REPO_DESCRIP

# build the docker image and push it to GCP artifact registry #
gcloud builds submit --tag $GCP_ARTIFACT_REG_REPO_PATH/$GCP_ARTIFACT_REG_CONTAINER_IMG_NAME .

# start the GKE cluster #
gcloud container clusters create-auto toy-flask-app-gke --location $GCP_REGION

# verify that I have access to the GKE cluster #
kubectl get nodes

# 

# delete the repository on google cloud artifact registry #
gcloud artifacts docker images delete $GCP_ARTIFACT_REG_REPO_PATH/$GCP_ARTIFACT_REG_CONTAINER_IMG_NAME
gcloud artifacts repositories delete $GCP_ARTIFACT_REG_REPO_NAME --location=$GCP_REGION
```


# References

* [Official Google Kubernetes Engine docs: Deploy an app in a container image to a GKE cluster](https://cloud.google.com/kubernetes-engine/docs/quickstarts/deploy-app-container-image#python)
