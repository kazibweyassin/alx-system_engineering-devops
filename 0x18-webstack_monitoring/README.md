# Webstack Monitoring Project

## Overview

This project focuses on implementing web stack monitoring, covering both application and server monitoring. The goal is to gather data about running software and ensure it behaves as expected (application monitoring) and collect data about virtual or physical servers to prevent overload (server monitoring). The project is initiated by Sylvain Kalache, co-founder at Holberton School.

## Concepts

- **Monitoring**
- **Server**

## Background Context

"You cannot fix or improve what you cannot measure" is a fundamental principle in the tech industry. In the age of data-ism, monitoring the performance of our software systems is crucial. This project aims to implement tools for measuring and analyzing the behavior of servers. Web stack monitoring is categorized into application monitoring and server monitoring.

### Web Stack Monitoring Categories:

1. **Application Monitoring:**
   - Obtaining data about running software.
   - Ensuring software behaves as expected.

2. **Server Monitoring:**
   - Obtaining data about virtual or physical servers.
   - Preventing server overload (CPU, memory, disk, or network).

## Learning Objectives

Upon completion of this project, you should be able to explain:

1. The importance of monitoring.
2. The two main areas of monitoring.
3. The purpose of access logs for a web server (e.g., Nginx).
4. The role of error logs for a web server (e.g., Nginx).

## Requirements

### General

- **Allowed Editors:** vi, vim, emacs
- **Interpretation:** Ubuntu 16.04 LTS
- **File Endings:** All files should end with a new line
- **Bash Scripts:** Must be executable
- **Shellcheck:** Your Bash script must pass Shellcheck (version 0.3.7) without any error
- **Shebang:** The first line of all Bash scripts should be `#!/usr/bin/env bash`
- **Comments:** The second line of all Bash scripts should be a comment explaining the script's purpose.

### Servers

| Name            | Username | IP              | State   |
| --------------- | -------- | --------------- | ------- |
| 272417-web-01   | ubuntu   | 3.83.245.138    | running |
| 272417-web-02   | ubuntu   | 34.239.248.8    | running |
| 272417-lb-01    | ubuntu   | 52.201.211.192  | running |

## Tasks

### 0. Sign up for Datadog and install datadog-agent

- Head to [Datadog](https://www.datadoghq.com/) and sign up for a free account.
- Select statistics from your current stack for Datadog to monitor.
- Follow the provided instructions to install the Datadog agent on `web-01`.
- Create an application key.
- Copy-paste your Datadog API key and application key in your Intranet user profile.
- Ensure `web-01` is visible in Datadog under the hostname `XX-web-01`.
- Validate using the provided API.
- If needed, update the hostname of your server.

### 1. Monitor some metrics

- Set up monitors in the Datadog dashboard to check:
  - The number of read requests issued to the device per second.
  - The number of write requests issued to the device per second.

### 2. Create a dashboard

- Create a new dashboard.
- Add at least 4 widgets to the dashboard, monitoring various metrics.
- Create the answer file `2-setup_datadog` with the dashboard_id on the first line.

## Copyright - Plagiarism

- Come up with solutions for the tasks independently.
- No copying and pasting of someone else’s work.
- Strictly forbidden to publish any content of this project.
- Any form of plagiarism will result in removal from the program.

## Copyright

© 2024 ALX, All rights reserved.:
