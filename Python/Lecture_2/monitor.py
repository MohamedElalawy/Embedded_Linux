
import psutil
import time

def show_cpu():
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")

def show_memory():
    mem = psutil.virtual_memory()
    print(f"Memory Usage: {mem.percent}% ({mem.used / (1024**3):.2f} GB used of {mem.total / (1024**3):.2f} GB)")

def show_disk():
    disk = psutil.disk_usage('/')
    print(f"Disk Usage: {disk.percent}% ({disk.used / (1024**3):.2f} GB used of {disk.total / (1024**3):.2f} GB)")

def show_top_processes(n=5):
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    # Sort by CPU percent descending
    processes = sorted(processes, key=lambda p: p['cpu_percent'], reverse=True)
    print(f"\nTop {n} Processes by CPU usage:")
    for proc in processes[:n]:
        print(f"PID: {proc['pid']}, Name: {proc['name']}, CPU%: {proc['cpu_percent']}")

def main():
    while True:
        print("="*30)
        show_cpu()
        show_memory()
        show_disk()
        show_top_processes()
        time.sleep(5)  # Refresh every 5 seconds

if __name__ == "__main__":
    main()


