
# cloud_service_monitor.py

import requests

class CloudServiceMonitor:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_status(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}


def main():
    print('Cloud Service Status Monitor')
    api_url = input('Enter the cloud provider status API URL: ')
    monitor = CloudServiceMonitor(api_url)
    status = monitor.get_status()

    if 'error' in status:
        print(f'Failed to fetch status: {status["error"]}')
    else:
        print('Service Status:')
        for service, state in status.items():
            print(f'- {service}: {state}')


if __name__ == '__main__':
    main()
