@Library("shared-library") _
// https://www.youtube.com/watch?v=TBtEXD062rA&ab_channel=KKJavaTutorials
pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                // call a function from the shared-library
                helloWorld(name: "Mr Blobby", dayOfWeek: "Saturday");
            }
        }
    }
}