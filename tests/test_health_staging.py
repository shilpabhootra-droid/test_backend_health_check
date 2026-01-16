import requests
import json
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: test_health_aramco.py
Author: Shilpa Bhootra
Date: 2026-01-16
Version: 1.0
Description:
This script processes information from health endpoint and generates summary reports
Contact: shilpa.bhootra@intuigence.com
Dependencies: requirements, json
"""

def check_health():
    url = "https://app.staging.intuigence.ai/v2/api/health"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    print("Health Check Response:")
    print(json.dumps(data, indent=2))
    print("\n" + "=" * 50 + "\n")

    all_healthy = True

    if isinstance(data, dict):
        if "status" in data:
            status = data["status"]
            if status != "healthy":
                print(f"❌ Main status: {status}")
                all_healthy = False
            else:
                print(f"✓ Main status: healthy")

        services = data.get("services", data.get("components", {}))
        if isinstance(services, dict):
            for service_name, service_info in services.items():
                if isinstance(service_info, dict):
                    status = service_info.get("status", "unknown")
                elif isinstance(service_info, str):
                    status = service_info
                else:
                    status = "unknown"

                if status != "healthy":
                    print(f"❌ {service_name}: {status}")
                    all_healthy = False
                else:
                    print(f"✓ {service_name}: healthy")

    print("\n" + "=" * 50)
    assert all_healthy, "One or more services are not healthy!"
    print("\n✓ All services are healthy!")


if __name__ == "__main__":
    check_health()