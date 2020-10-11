pipeline {
    dir("${env.WORKSPACE}/domain/test"){
        agent { dockerfile true }
        stages {
            stage('test') {
                steps {
                    sh 'python -m unittest domain.test.canvas_drawer'
                }
            }
        }
    }
}