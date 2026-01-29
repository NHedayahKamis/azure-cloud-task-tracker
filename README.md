# azure-cloud-task-tracker
This project is a full-stack Flask application independently architected and deployed to the Azure Cloud platform. It demonstrates a complete CI/CD lifecycle, from local development to automated cloud synchronization.
Technical Implementation:
-Backend: Python
-Deployment: Azure App Service (F1 Free Tier)
-CI/CD Pipeline: GitHub Actions with automated YAML workflows. 
-Container/Server Management: Gunicorn (WSGI HTTP Server)

Cloud Architecture & Lessons Learned:
During the deployment of this project, I successfully managed several real-world cloud infrastructure challenges:
-Resource Migration: Successfully performed a live migration of the application to a new Azure resource namespace (cloud-task-tracker).
-CI/CD Optimization: Consolidated redundant workflow files into a single, clean .github/workflows configuration to prevent deployment conflicts.
-Quota Management: Monitored and managed Azure's daily CPU and data-out limits (F1 tier), ensuring the application operates within strict resource constraints.

*Note on Availability: This application is hosted on the Azure F1 (Free) Tier. Due to Microsoft's daily CPU quota limits, the live site may occasionally display a 403 Forbidden Error toward the end of the day. This is an intentional architectural choice to demonstrate Cost-Effective cloud resource management.
