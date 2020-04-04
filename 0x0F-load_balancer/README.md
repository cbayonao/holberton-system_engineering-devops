# 0x0F. Load balancer


Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 16.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
Your Bash script must pass Shellcheck (version 0.3.7) without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing

Tasks

#### [0. Double the number of webservers](https://github.com/cbayonao/holberton-system_engineering-devops/blob/master/0x0F-load_balancer/0-custom_http_response-header)
Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
The name of the custom HTTP header must be X-Served-By
The value of the custom HTTP header must be the hostname of the server Nginx is running on
Write 0-custom_http_response-header so that it configures a brand new Ubuntu machine to the requirements asked in this task
#### [1. Install your load balancer](https://github.com/cbayonao/holberton-system_engineering-devops/blob/master/0x0F-load_balancer/1-install_load_balancer)
Install and configure HAproxy on your lb-01 server.
#### [2. Add a custom HTTP header with Puppet](https://github.com/cbayonao/holberton-system_engineering-devops/blob/master/0x0F-load_balancer/2-puppet_custom_http_response-header.pp)
Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.
