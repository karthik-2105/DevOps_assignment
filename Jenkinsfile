pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "calculator-app"  // Docker image name
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/karthik-2105/DevOps_assignment.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'pip install --no-cache-dir -r requirements.txt'
            }
        }
        stage('Run Unit Tests') {
            steps {
                bat 'pytest -v'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE% .'
            }
        }
    }
}
