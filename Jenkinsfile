pipeline {

    agent any

 

    stages 

    {

        stage('Hello') 

        {

            steps 
            {
                echo "Hi"
            }
 


        }
    
        stage('Docker') 

        {

            
            steps 

            {

                bat 'docker-compose up --build -d'

            }
            

        }
        stage('Isha') 

        {


            steps 

            {

                bat 'dir'

            }
            

        }

    

    }

}