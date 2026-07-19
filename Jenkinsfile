pipeline {
    agent any
    parameters {
        string(name: 'NAME', defaultValue: 'World', description: 'Who should we greet?')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying the project for ${params.NAME}..."
            }
        }
    }
    post {
        always {
            echo 'This always runs, no matter what happened.'
        }
        success {
            echo 'Great news! The pipeline succeeded.'
        }
        failure {
            echo 'Uh oh, the pipeline failed. Someone should check this.'
        }
    }
}