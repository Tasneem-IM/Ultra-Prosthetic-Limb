from bs4 import BeautifulSoup

# HTML content as strings
data_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Data | Smart Prosthetic System</title>
</head>
<body>
  <div class="data-table-section">
    <h2>Sweat Levels</h2>
    <table>
      <thead>
        <tr><th>Date</th><th>Sweat Level</th></tr>
      </thead>
      <tbody>
        <tr><td>01/12/2025</td><td>Medium</td></tr>
        <tr><td>02/12/2025</td><td>High</td></tr>
        <tr><td>03/12/2025</td><td>Low</td></tr>
      </tbody>
    </table>
  </div>

  <div class="data-table-section">
    <h2>pH in Sweat</h2>
    <table>
      <thead>
        <tr><th>Date</th><th>pH Value</th></tr>
      </thead>
      <tbody>
        <tr><td>01/12/2025</td><td>6.5</td></tr>
        <tr><td>02/12/2025</td><td>7.0</td></tr>
        <tr><td>03/12/2025</td><td>6.2</td></tr>
        <tr><td>04/12/2025</td><td>6.8</td></tr>
        <tr><td>05/12/2025</td><td>7.1</td></tr>
      </tbody>
    </table>
  </div>

  <div class="data-table-section">
    <h2>Heart Rate (HR)</h2>
    <table>
      <thead>
        <tr><th>Date</th><th>HR (bpm)</th></tr>
      </thead>
      <tbody>
        <tr><td>01/12/2025</td><td>75</td></tr>
        <tr><td>02/12/2025</td><td>80</td></tr>
        <tr><td>03/12/2025</td><td>70</td></tr>
        <tr><td>04/12/2025</td><td>78</td></tr>
        <tr><td>05/12/2025</td><td>82</td></tr>
      </tbody>
    </table>
  </div>

  <div class="data-table-section">
    <h2>Oxygen Saturation (SpO2)</h2>
    <table>
      <thead>
        <tr><th>Date</th><th>SpO2 (%)</th></tr>
      </thead>
      <tbody>
        <tr><td>01/12/2025</td><td>98</td></tr>
        <tr><td>02/12/2025</td><td>97</td></tr>
        <tr><td>03/12/2025</td><td>98</td></tr>
        <tr><td>04/12/2025</td><td>96</td></tr>
        <tr><td>05/12/2025</td><td>99</td></tr>
      </tbody>
    </table>
  </div>
</body>
</html>
"""

# Load HTML content
def load_html_from_text(html_text):
    return BeautifulSoup(html_text, "html.parser")

# Extract data from the tables
def extract_data():
    soup = load_html_from_text(data_html)
    data = {
        "sweat_levels": [],
        "ph_levels": [],
        "heart_rate": [],
        "oxygen_saturation": []
    }

    # Extract sweat levels
    for section in soup.find_all("div", class_="data-table-section"):
        table = section.find("table")
        rows = table.find("tbody").find_all("tr")
        if "Sweat Levels" in section.h2.text:
            for row in rows:
                date, sweat_level = [td.text for td in row.find_all("td")]
                data["sweat_levels"].append({"date": date, "sweat_level": sweat_level})
        elif "pH in Sweat" in section.h2.text:
            for row in rows:
                date, ph_value = [td.text for td in row.find_all("td")]
                data["ph_levels"].append({"date": date, "ph_value": float(ph_value)})
        elif "Heart Rate" in section.h2.text:
            for row in rows:
                date, hr_value = [td.text for td in row.find_all("td")]
                data["heart_rate"].append({"date": date, "hr_value": int(hr_value)})
        elif "Oxygen Saturation" in section.h2.text:
            for row in rows:
                date, spo2_value = [td.text for td in row.find_all("td")]
                data["oxygen_saturation"].append({"date": date, "spo2_value": int(spo2_value)})

    return data

# Generate recommendations based on data
def generate_recommendations(data):
    print("\n--- Recommendations Based on Data ---")
    
    # Sweat Level recommendations
    for entry in data["sweat_levels"]:
        date = entry["date"]
        sweat_level = entry["sweat_level"]
        print(f"\nDate: {date} - Sweat Level: {sweat_level}")
        if sweat_level == "High":
            print("Recommendation: Reduce grip strength to avoid slipping due to excessive sweat.")
        elif sweat_level == "Medium":
            print("Recommendation: Moderate grip strength. Ensure limb ventilation is active.")
        elif sweat_level == "Low":
            print("Recommendation: Maintain normal settings. No adjustments needed.")
    
    # pH Level recommendations
    for entry in data["ph_levels"]:
        date = entry["date"]
        ph_value = entry["ph_value"]
        print(f"\nDate: {date} - pH Value: {ph_value}")
        if ph_value < 6.5:
            print("Recommendation: pH level is low. Consider monitoring more closely.")
        elif ph_value >= 7.0:
            print("Recommendation: pH level is slightly high. Maintain balanced hydration.")
        else:
            print("Recommendation: pH level is within normal range.")
    
    # Heart Rate recommendations
    for entry in data["heart_rate"]:
        date = entry["date"]
        hr_value = entry["hr_value"]
        print(f"\nDate: {date} - Heart Rate: {hr_value} bpm")
        if hr_value > 80:
            print("Recommendation: Heart rate is high. Monitor for potential stress or exertion.")
        elif hr_value < 70:
            print("Recommendation: Heart rate is low. Ensure sufficient rest and hydration.")
        else:
            print("Recommendation: Heart rate is normal.")
    
    # Oxygen Saturation recommendations
    for entry in data["oxygen_saturation"]:
        date = entry["date"]
        spo2_value = entry["spo2_value"]
        print(f"\nDate: {date} - Oxygen Saturation: {spo2_value}%")
        if spo2_value < 95:
            print("Recommendation: Oxygen saturation is low. Consider improving ventilation.")
        else:
            print("Recommendation: Oxygen saturation is within normal range.")

# Main function
if __name__ == "__main__":
    print("\nAnalyzing data...")
    data = extract_data()
    generate_recommendations(data)
