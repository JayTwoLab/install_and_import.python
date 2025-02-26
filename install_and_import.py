
import importlib.util
import subprocess
import sys
import os

def is_conda_env():
    """Check if the current environment is Conda."""
    return "conda" in sys.version or "Continuum" in sys.version or "conda" in sys.executable

def install_and_import(package, use_conda=None):
    """
    Automatically installs and imports a package.
    - use_conda: True to force Conda, False to force pip, None to auto-detect.
    """
    if importlib.util.find_spec(package) is None:
        print(f"'{package}' module not found. Installing...")

        # Auto-detect the environment
        if use_conda is None:
            use_conda = is_conda_env()

        try:
            if use_conda:
                print(f"🔹 Conda environment detected. Running 'conda install {package}'...")
                subprocess.run(["conda", "install", package, "-y"], check=True)
            else:
                print(f"🔹 Using pip: Running 'pip install {package}'...")
                subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
        except Exception as e:
            print(f"🚨 Error occurred while installing '{package}': {e}")
            return
    
    # Import the installed package dynamically
    globals()[package] = __import__(package)
    print(f"✅ '{package}' has been successfully installed and imported.")

# Example usage
install_and_import("scipy")  # Auto-detects and installs using the appropriate package manager
install_and_import("numpy", use_conda=True)  # Forces Conda installation
install_and_import("pandas", use_conda=False)  # Forces pip installation

