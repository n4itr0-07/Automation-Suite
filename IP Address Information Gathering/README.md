# IP Information Lookup Script

## Overview
This script allows you to perform an IP information lookup to gather geolocation details on a specified IP address. Using a simple command-line interface, it fetches data from the `ip-api.com` API, displaying key information like city, country, ISP, and timezone. The output is styled with color and emojis for clarity and readability.

## Requirements
- Python 3.x
- `colorama` library for colored output in the terminal
  ```bash
  pip install colorama
  ```

## How to Use
1. **Run the script**: Execute the script from the terminal:
   ```bash
   python ip_lookup.py
   ```
2. **Enter the target IP**: When prompted, input the IP address you'd like to look up.
3. **View the results**: The script will display detailed information about the IP in a styled format.

## Example Output
```
🌐 Enter the target IP: 8.8.8.8

🔍 IP Information Lookup 🔍
==============================
🌍 IP Address: 8.8.8.8
🏙️  City: Mountain View
📡 ISP: Google LLC
🌎 Country: United States
🏞️  Region: California
🕒 Timezone: America/Los_Angeles
==============================
✨ End of Information ✨
```

## Notes
- **Rate Limiting**: The `ip-api.com` API has usage limits for free-tier requests. Consider the limits if making frequent lookups.
- **Styling**: Output styling is supported via the `colorama` library, which is initialized at the start of the script for automatic reset after each print.

---  
