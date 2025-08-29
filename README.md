# Cloud Service Status Monitor

A Python-based command-line tool for monitoring the operational status of cloud services by fetching data from a provider's status API.

## Description

This tool allows users to quickly check the health of various cloud services (like compute, storage, and databases) by querying a status API endpoint. It's designed to be a simple, extensible monitor for anyone working with cloud infrastructure.

## How to Use

1.  Clone this repository or download the `cloud_service_monitor.py` file.
2.  Run the script from your terminal:
    ```
    python cloud_service_monitor.py
    ```
3.  When prompted, enter the URL for the cloud provider's status API.

## Features

-   **Real-Time Status**: Fetches live data from any JSON-based status API.
-   **Simple Interface**: Easy-to-use command-line prompts.
-   **Error Handling**: Manages network errors and bad responses gracefully.

**Note**: This tool requires the `requests` library. You can install it by running `pip install requests`.
