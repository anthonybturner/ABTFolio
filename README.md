Project Name: ABTFolio
Author: Anthony Turner

Description: ABTFolio is a dynamic and responsive portfolio website that showcases projects, technical skills, and experience. Built using React.js for the frontend, Axios for HTTP requests, and Python with Flask for the backend, this project serves as a full-stack demonstration of modern web development practices.

Key features include:

React.js for an intuitive, modern, and responsive UI.
Axios for managing asynchronous HTTP requests to interact with backend APIs.
Flask as the backend framework, handling server-side logic and API responses.
A simple database management system to handle project details and user data.
CI/CD Pipeline with Azure Pipelines
ABTFolio leverages Azure Pipelines to automate the entire deployment process. The pipeline is defined using a YAML configuration file, which sets up the necessary steps to deploy the React app and Flask backend to GoDaddy via FTP.

Deployment Process Explained:
React Build Process: The pipeline first installs the necessary dependencies for the React frontend, builds the app using npm run build, and prepares the build files for deployment. These files are then copied over to the static directory of the Flask app, ensuring that the frontend assets are properly served by Flask.

Backend Flask Setup: The pipeline ensures that the Python dependencies (Flask and other libraries) are installed in the correct environment. The backend is configured to serve both the static React files and handle API requests.

FTP Deployment via Azure Pipeline: The pipeline uses FTP to deploy the project to GoDaddy. The following steps are part of the deployment:

The built React app files are transferred to the correct folder on the GoDaddy server, ensuring that the static assets are available for serving.
The Flask application files, including the Python scripts, are uploaded to the appropriate directory on the server, ensuring the backend runs smoothly.
The pipeline automatically updates the remote server with the latest files from the repository, keeping the site up-to-date.
The entire deployment process is automated in Azure Pipelines using the YAML file, which defines the build, deployment steps, and the transfer of files to GoDaddy. This setup enables continuous integration and deployment (CI/CD) with minimal manual intervention, ensuring fast and reliable updates to the portfolio site.

Technologies Used:
Frontend: React.js, Axios
Backend: Python, Flask
Deployment: GoDaddy (FTP), Azure Pipelines (YAML)
Version Control: Git, GitHub