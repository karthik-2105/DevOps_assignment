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
                sh 'pip install --no-cache-dir -r requirements.txt'
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh 'pytest -v'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }
    }
}
