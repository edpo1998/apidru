pipeline{
    environment{
        branch_name = "${BRANCH_NAME}"
        complete_job_name = "${JOB_NAME}"
        job_name = getJobName(complete_job_name)
        image = ''
        profile = getEnvironment(branch_name)
        registry_host = getRegistryHostName(branch_name)
        registry_group = getRegistryRepositoryGroup(branch_name)
        registry_repo = getRepositoryName(registry_group,job_name)
        registry_credentials = getRegistryCredentials(branch_name)
    }
    agent none

    stages{		        
        stage('Create image'){
             agent {
               label 'docker'
            }   
            steps{
                script{
                    image = docker.build registry_host + "/" + registry_repo + ":V${BUILD_NUMBER}"
                }
            }
        }

        stage('Push image'){
            agent {
               label 'docker'
            }   
            steps{
                script{
                    docker.withRegistry("https://" + registry_host + "/" + registry_repo, registry_credentials){
                        image.push("V${BUILD_NUMBER}")
                    }
                }
            }
        }
        
        stage('Remove image'){
            agent {
               label 'docker'
            }   
            steps{
                sh "docker rmi " + registry_host + "/" + registry_repo +":V${BUILD_NUMBER}"
            }
        }

		stage('spinnaker'){
                    agent {
                       label 'docker'
                    }
                    steps{
        				 sh 'echo "BUILD_NUMBER: ${BUILD_NUMBER}" >> build_properties.yaml'
                         sh 'echo "JOB_NAME: ${JOB_NAME}" >> build_properties.yaml'
                         sh 'echo "JOB_URL: ${JOB_URL}" >> build_properties.yaml'
                         sh 'echo IMAGE: "${registry_host}/${registry_repo}:V${BUILD_NUMBER}" >> build_properties.yaml'
                    }
        }
    }
	
	post { 
        always  { 
            node('docker') {
                script {
                    if(branch_name == 'master'){
                         echo '${currentBuild.result}' 
                         slackNotifier("${currentBuild.result}")
                        }
                    }
					archiveArtifacts artifacts: 'build_properties.yaml', fingerprint: true
                }
        }
    }
}

def getGitHubRepositoryName(originUrl){
    return originUrl.split("//")[1]
}

def getJobName(completeJobName){
    return completeJobName.tokenize("/")[0]
}

def getEnvironment(branchName){
    /*
        Obtiene el Profile al que debe realizarle el deploy
    */
    if(branchName=='develop'){
        return 'api_dru_develop'
    }else if(branchName=='master'){
        return 'api_dru_master'
    }
}

def getRegistryCredentials(branchName){
    if(branchName=='develop'){
        return 'registry_develop'
    }else if(branchName=='master'){
        return 'registry_master'
    }
}

def getRegistryHostName(branchName){
    if(branchName=='develop'){
        return "${REGISTRY_TEST}"
    }else if(branchName=='master'){
        return "${REGISTRY_PROD}"
    }
}

def getRegistryRepositoryGroup(branchName){
    if(branchName=='develop'){
        return "certificacion-devops"
    }else if(branchName=='master'){
        return "devops"
    }
}

def getRepositoryName(group, projectName){
	return group + "/" + projectName
}

def getSpinnakerDir(branchName){
    return "conf"
}

def slackNotifier(buildResult) {
  if ( buildResult == "SUCCESS" ) {
    slackSend color: "good", message: "Job: ${env.JOB_NAME} with buildnumber ${env.BUILD_NUMBER} was successful"
  }
  else if( buildResult == "FAILURE" ) { 
    slackSend color: "danger", message: "Job: ${env.JOB_NAME} with buildnumber ${env.BUILD_NUMBER} was failed"
    slackSend color: "danger", message: "Build URL: ${env.BUILD_URL}"
  }
  else if( buildResult == "UNSTABLE" ) { 
    slackSend color: "warning", message: "Job: ${env.JOB_NAME} with buildnumber ${env.BUILD_NUMBER} was unstable"
    slackSend color: "warning", message: "Build URL: ${env.BUILD_URL}"
  }
  else {
    slackSend color: "danger", message: "Job: ${env.JOB_NAME} with buildnumber ${env.BUILD_NUMBER} its result was unclear"	
    slackSend color: "danger", message: "Build URL: ${env.BUILD_URL}"
  }
}