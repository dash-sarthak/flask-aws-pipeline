env.name = 'xcel2json'
pipeline{
    stage('pulling code'){
        //we are pulling the code from github
        git ('https://github.com/dash-sarthak/flask-aws-pipeline.git')
        
        //check if dockerfile exists
        if(!fileExists("Dockerfile"){
            error('Dockerfile kidar hai?')
        }
    }
    stage('Build docker image'){
        //building the docker image
        sh "sudo docker build -t $name ."
    }
    stage('Running the container'){
        //running container
        sh "sudo docker run -p 3000:5000 --name $name -d $name"
    }
}
