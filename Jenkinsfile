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
                sh '''
                docker build -t my-python-app:latest .
                '''
            }
        }

        stage('Load Image to Minikube') {
            steps {
                sh 'minikube image load my-python-app:latest'
            }
        }


        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                export KUBECONFIG=/var/lib/jenkins/.kube/config


                kubectl apply -f k8s/deployment.yaml
                kubectl apply -f k8s/service.yaml

                kubectl rollout restart deployment/python-app

                kubectl rollout status deployment/python-app

                kubectl get pods
                kubectl get svc
                '''
            }
        }
    }
}