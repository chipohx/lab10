pipeline {
    agent any

    environment {
        VENV = "${WORKSPACE}/venv"
        PATH = "${WORKSPACE}/venv/bin:${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv $VENV
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python main.py'
            }
        }
    }
}
