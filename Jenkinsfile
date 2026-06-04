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

        stage('Deploy') {

            steps {

                deployApp()

            }

        }

    }

}