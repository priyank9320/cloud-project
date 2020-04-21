# cloud-project

The link to the website is : http://flask-alb-1207280611.us-east-1.elb.amazonaws.com/



Description of the functionality :

This cloud application was built on the AWS Educate Account (which is a limited access account).

The application consists of two containers : Flask-Home and Flask-Api , which run in the same EC2 instance.

The Flask-Home container can be used by just entering the url of the app as the route it is using is just "/" . The Home container connects to the RDS(Mysql) database and displays all the data in a table format.

The Flask-Api container can be used by using the route "/api/<operation name>" . The operation name refers to the three text processing operations that can be done by this web app.

1. Spelling correction : The user can enter a text and also an id which can be used as tag to mark the text entered, and on submitting the text the app will correct all the spelling mistakes in it. The route for this functionality is "/api/spell" .
2. Space correction : The user can enter text which can contain words without spaces, and the functionality will split the words and save the text with proper spaces. The route for this functionality is "/api/space" .
3. Translation : The user can enter text in any language and the functionality will translate the text into English by using the Google Translate API . The route for this functionality is "/api/translate" .

Once the user performs any of the above mentioned actions the processed text gets saved in the database along with the original text and id appended with the date and time of the action performed. This data can be seen by visiting the home page, which uses the route "/" .

The application uses a Application Load Balancer(ALB), and the request goes to the ALB endpoint and then according to the ALB rules it gets routed to the '/ ' or the '/api/*' route .

Couldn't enable autoscaling as we don't have the access to do that in the AWS Educate account.



Below is an example image which shows how the cloud application is structured :

![Cluster-Service-Task-Container-Diagram.png](https://www.bogotobogo.com/DevOps/Docker/images/Docker-Flask-ECS/Cluster-Service-Task-Container-Diagram.png)







Commands used to create containers and push to ECR:

1. create container image: sudo docker build -t flask-api .
2. create repository in the ECR : aws ecr create-repository --repository-name ecs-flask-api
3. login in the ECR : sudo $(aws ecr get-login --no-include-email --region us-east-1)
4. tag the image : sudo docker tag flask-api 510068942181.dkr.ecr.us-east-1.amazonaws.com/ecs-flask-api
5. push the images to the ECR (Elastic Container Repository) : sudo docker push 510068942181.dkr.ecr.us-east-1.amazonaws.com/ecs-flask-api



to login we first need to update the credentials, which can be found in the AWS account welcome page after login , in the "account details" button . The aws_access_key_id , aws_session_access_key, aws_session_token values need to be updated in the "~/.aws/credentials" file to be able to login in the ECR through the terminal.





References :

1. Deploying Flask app to ECS : https://www.bogotobogo.com/DevOps/Docker/Docker-Flask-ALB-ECS.php
2. Learn Flask for Python : https://www.youtube.com/watch?v=Z1RJmh_OqeA

3. AWS fundamentals : https://www.coursera.org/learn/aws-fundamentals-going-cloud-native
4. Elastic Load Balancers : https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html
5. Launching RDS database instance : https://www.youtube.com/watch?v=xzCgeRxSzy4&t=957s

6. Gentle Introduction to How AWS ECS Works with Example Tutorial : https://medium.com/boltops/gentle-introduction-to-how-aws-ecs-works-with-example-tutorial-cea3d27ce63d
