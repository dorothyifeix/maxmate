import os
import subprocess
import psutil
import winreg

class MaxMate:
    def __init__(self):
        self.startup_folder = os.path.join(os.environ['APPDATA'], 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')

    def disable_unnecessary_startup_programs(self):
        """Disables unnecessary startup programs for faster boot."""
        print("Disabling unnecessary startup programs...")

        # Example: Disabling OneDrive from startup
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_ALL_ACCESS) as key:
                winreg.DeleteValue(key, 'OneDrive')
            print("OneDrive disabled from startup.")
        except FileNotFoundError:
            print("OneDrive was not found in startup.")

    def optimize_boot_settings(self):
        """Optimizes the boot settings for better resource management."""
        print("Optimizing boot settings...")

        # Example: Setting the number of processors for boot
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Control\Session Manager\Configuration Manager', 0, winreg.KEY_ALL_ACCESS) as key:
                winreg.SetValueEx(key, "BootExecute", 0, winreg.REG_MULTI_SZ, ["autocheck autochk *"])
            print("Boot settings optimized.")
        except Exception as e:
            print(f"Error optimizing boot settings: {e}")

    def clear_temp_files(self):
        """Clears temporary files to free up resources."""
        print("Clearing temporary files...")
        temp_dir = os.environ.get('TEMP', None)
        if temp_dir:
            for filename in os.listdir(temp_dir):
                file_path = os.path.join(temp_dir, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        os.rmdir(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")
            print("Temporary files cleared.")
        else:
            print("No temporary directory found.")

    def manage_services(self):
        """Disables unnecessary services for quicker startup."""
        print("Managing unnecessary services...")

        # Example: Disabling Windows Search service
        try:
            subprocess.run(['sc', 'config', 'WSearch', 'start=disabled'], check=True)
            print("Windows Search service disabled.")
        except subprocess.CalledProcessError as e:
            print(f"Error disabling Windows Search service: {e}")

    def run_all_optimizations(self):
        """Runs all optimizations."""
        self.disable_unnecessary_startup_programs()
        self.optimize_boot_settings()
        self.clear_temp_files()
        self.manage_services()
        print("All optimizations complete!")

if __name__ == "__main__":
    max_mate = MaxMate()
    max_mate.run_all_optimizations()