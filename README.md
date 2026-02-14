# ScanNZV — Web Attack Surface & CVE Intelligence Scanner

ScanNZV is a security scanning and monitoring tool that fingerprints a target website’s technology stack, maps detected components to CPE/CVE intelligence for rapid triage, and optionally validates findings using automated template-based checks. It is designed to support asset discovery, vulnerability assessment, and reporting in a repeatable workflow.

## 1. Key capabilities
- **URL availability monitoring**: background thread to continuously check target URL status.
- **Technology fingerprinting**: identify web technologies and versions to build an asset profile.
- **CPE/CVE mapping**: correlate detected stack with vulnerability intelligence for prioritization and scheduled database refresh keeps vulnerability intelligence up-to-date for reliable triage.
- **Automated validation**: run template-based checks to reduce false positives.
- **Monitoring & reporting**: monitor target availability/scan status, export reports, and send email notifications to support tracking and remediation.

## 2. Tech stack
Python (Flask), MySQL, Docker, and security tooling integration (tech fingerprinting + template-based scanners).

## 3. Deployment Instructions

### 3.1. Docker Deployment

#### 3.1.1. Requirements
- Software: Docker 20.10+, Docker Compose 1.29+.
- Network Configuration: Open ports 5000, 3306, 9050, 9051.

#### 3.1.2. Instructions

**Step 1:** Clone the repository from here.

**Step 2:** Navigate to the source directory and build the image using the following command:
```
docker build -t scannzv .
```

**Step 3:** Start the containers using the following command. This command should also be used for subsequent starts:
```
docker compose -f docker-compose.dev.yml up
```

**Step 4:** Mount the data volume. This command only needs to be run once during the initial setup:
```
docker exec -it scanningtool-scannzv-1 /bin/sh python flaskr/function/data_auto_update.py
```

**Step 5:** Access the application at `http://127.0.0.1:5000`

> Note: This deployment supports hot reload for development convenience. However, for full access and customization, direct deployment is recommended.

---

### 3.2. Direct Deployment

#### 3.2.1. Requirements
- External Tools: Nuclei ([Installation Guide](https://github.com/projectdiscovery/nuclei)), GeckoDriver + Firefox ([Installation Guide](https://firefox-source-docs.mozilla.org/testing/geckodriver/geckodriver/Usage.html)).
- Language: Python 3.13+.
- Database: MySQL 8.0 (Requires configuration).

#### 3.2.2. Instructions

**Step 1:** Clone the repository from here.

**Step 2:** Navigate to the source directory and create a virtual environment using:
```
python -m venv venv
```

> Note: On Windows, PowerShell might block virtual environment execution for security reasons. Run the following command to allow it:
```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Step 3:** Activate the virtual environment:
- On **Windows**:
```
.\venv\Scripts\activate
```
- On **Linux/MacOS**:
```
source venv/bin/activate
```

> This command must be run before starting the server.

**Step 4:** Install MySQL (recommended version 8.0.x) and configure the database settings in the `.env` file using the correct format.

**Step 5:** Start the application with:
```
python run.py
```