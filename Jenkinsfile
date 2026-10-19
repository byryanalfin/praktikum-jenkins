   pipeline {
       agent any
       environment {
           DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
           DOCKER_IMAGE = 'byryanalfin/praktikum-jenkins'
       }
       stages {
           stage('Build Docker Image') {
               steps {
                   script {
                       bat "docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} ."
                   }
               }
           }
           stage('Push to Docker Hub') {
               steps {
                   script {
                       bat """
                           docker login -u ${DOCKERHUB_CREDENTIALS_USR} -p ${DOCKERHUB_CREDENTIALS_PSW}
                           docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
                       """
                   }
               }
           }
       }
   }
