@Library('company-lib') _

pipeline {

    agent any

    stages {

        stage('Checkout') {

            steps {

                echo "Cloning GitHub Repository"

            }

        }

        stage('Build') {

            steps {

                buildApp()

            }

        }

        stage('Test') {

            steps {

                testApp()

            }

        }

        stage('Docker Build') {

            steps {

                echo "Building Docker Image"

                sh '''
                docker build -t my-python-app:latest .
                '''

            }

        }

        stage('Deploy Docker') {
            steps {
                echo "Deploying Docker Container"

                sh '''
                docker rm -f my-python-app || true

                docker run -d \
                --name my-python-app \
                -p 5000:5000 \
                my-python-app:latest
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                minikube image load my-python-app:latest

                kubectl apply -f k8s/deployment.yaml
                kubectl apply -f k8s/service.yaml
                '''
            }
        }

    }

}