pipeline {
    agent any

    stages {
        stage('python version') {
            steps {
              bat 'python --version'
            }
        }
        stage('Run Python Scripts') {
            steps {
                withPythonEnv('python') {
                    bat 'pip install -r requirements.txt'
                    bat 'python -m pytest spotify_api/ -v -s --alluredir reports/allure/allure-results'
                }
            }
        }
        stage('reports') {
            steps {
                script {
                    allure ([
                        includeProperties: false,
                        jdk:'',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure-results']]
                    ])
                 }
            }
        }
    }
}