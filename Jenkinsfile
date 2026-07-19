pipeline {
    agent any
    parameters {
        string(name: 'NAME', defaultValue: 'World', description: 'Who should we greet?')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Checking Python is available...'
                bat 'python --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Running real tests...'
                bat 'python test_app.py'
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying the project for ${params.NAME}..."
                bat 'python app.py'
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