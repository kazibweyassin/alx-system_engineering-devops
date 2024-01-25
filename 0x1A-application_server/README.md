
# 0x1A Application Server

## Overview

This project focuses on setting up and configuring an application server to serve dynamic content for an Airbnb clone. The project includes tasks related to setting up the development environment, configuring Gunicorn for production, configuring Nginx to serve the application, and serving different routes with query parameters.

## Project Structure

The project is organized into different tasks, each addressing specific aspects of the application server setup. Here's an overview of the tasks:

1. **Set up development with Python**
   - Clone the Airbnb Clone v2 repository.
   - Configure Flask application to serve content from `/airbnb-onepage/` on port 5000.

2. **Set up production with Gunicorn**
   - Install Gunicorn and necessary libraries.
   - Configure Gunicorn to serve content on port 5000.
   - Verify the setup with a sample request.

3. **Serve a page with Nginx**
   - Configure Nginx to serve content from the route `/airbnb-onepage/`.
   - Proxy requests to the Gunicorn process on port 5000.
   - Test the configuration locally and on the public IP.

4. **Add a route with query parameters**
   - Configure Nginx to proxy requests to two different Gunicorn processes on ports 5000 and 5001.
   - Test the setup with different routes and query parameters.

5. **Serve your AirBnB clone**
   - Clone the Airbnb Clone v4 repository.
   - Configure Gunicorn to serve content from `web_dynamic/2-hbnb.py` on port 5003.
   - Configure Nginx to serve static assets and proxy requests to the Gunicorn process.
   - Verify the setup and ensure proper rendering of the web page.

## Instructions for Each Task

### Task 0:

```bash
# Example commands and usage for Task 0
python3 -m web_flask.0-hello_route

