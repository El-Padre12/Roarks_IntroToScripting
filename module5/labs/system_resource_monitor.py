# Angel Chavez
# Aug 28th, 2025
# Python 3.13.5
# lightweight python script that checks CPU, memory, and disk-usage in real time

import psutil
import time
import os
import sys

def clear_screen():
    """
    Clears the console screen.
    This is cross-platform.
    """
    os.system('cls' if os.name == 'nt' else 'clear') # checks operating system and does action based off that.

def get_main_disk_path():
    """
    Returns the appropriate path for the main disk based on the operating system.
    """
    if sys.platform == "win32":
        return "C:\\"
    else: # linux, darwin (macOS), etc.
        return "/"

def monitor_system_usage(duration=30, interval=5):
    """
    Gathers and displays system usage statistics periodically.

    Args:
        duration (int): The total duration in seconds for the monitoring.
        interval (int): The interval in seconds between each refresh.
    """
    main_disk_path = get_main_disk_path()
    end_time = time.time() + duration

    while time.time() < end_time:
        clear_screen()
        
        # CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)  # Blocking interval for accuracy
        
        # Memory usage
        memory = psutil.virtual_memory()
        memory_used_mb = memory.used / (1024 * 1024)
        memory_total_mb = memory.total / (1024 * 1024)
        memory_percent = memory.percent
        
        # Disk usage for main drive
        try:
            disk = psutil.disk_usage(main_disk_path)
            disk_used_gb = disk.used / (1024 * 1024 * 1024)
            disk_total_gb = disk.total / (1024 * 1024 * 1024)
            disk_percent = disk.percent
        except FileNotFoundError:
            print(f"Error: The disk path '{main_disk_path}' was not found.")
            disk_percent = 0
            disk_used_gb = 0
            disk_total_gb = 0
        
        # Display Results
        
        print("--- System Usage Monitor ---")
        print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        print("CPU:")
        print(f"  Current usage: {cpu_percent:.1f}%")
        
        print("\nMemory:")
        print(f"  Used: {memory_used_mb:.2f} MB")
        print(f"  Available: {memory_total_mb:.2f} MB")
        print(f"  Usage: {memory_percent:.1f}%")

        if disk_total_gb > 0:
            print(f"\nDisk ({main_disk_path}):")
            print(f"  Used: {disk_used_gb:.2f} GB")
            print(f"  Total: {disk_total_gb:.2f} GB")
            print(f"  Usage: {disk_percent:.1f}%")
        
        # Check Thresholds and Alert User
        
        alert_needed = False
        print("\n--- Alerts ---")
        
        if cpu_percent > 80:
            print(f"ALERT: CPU usage is high: {cpu_percent:.1f}%")
            alert_needed = True
            
        if memory_percent > 75:
            print(f"ALERT: Memory usage is high: {memory_percent:.1f}%")
            alert_needed = True
            
        if disk_percent > 90:
            print(f"ALERT: Disk usage is high: {disk_percent:.1f}%")
            alert_needed = True
            
        if not alert_needed:
            print("Thresholds are within acceptable ranges.")
            
        # Wait for the next interval
        time.sleep(interval)

if __name__ == "__main__":
    try:
        monitor_system_usage()
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")