pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'echo "Building..."'
                sh 'touch build.txt'
                sh 'ls -la'
                sh 'pwd'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Testing..."'
                sh 'mv build.txt test.txt'
                sh 'ls -la'
                sh 'pwd'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying..."'
                sh 'mv test.txt deploy.txt'
                sh 'ls -la'
                sh 'pwd'
            }
        }
    }
}
