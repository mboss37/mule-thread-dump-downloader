import re
import pandas as pd
import matplotlib.pyplot as plt
import json

def parse_log_file(filename):
    data = []
    with open(filename, 'r') as file:
        prev_line = ''
        for line in file:
            if '"flowLatency"' in line:
                try:
                    # Extract flowLatency from the current line
                    json_data_current = json.loads(line)
                    latency = json_data_current.get("flowLatency", None)

                    # Extract timestamp from the previous line
                    json_data_prev = json.loads(prev_line)
                    flow_end_time = json_data_prev.get("flowEndTime", None)
                    if flow_end_time:
                        timestamp = pd.to_datetime(flow_end_time, utc=True)

                    if timestamp and latency is not None:
                        data.append((timestamp, latency))
                except (json.JSONDecodeError, ValueError, AttributeError):
                    # Handle parsing errors
                    continue
            prev_line = line

    print(f"Found {len(data)} data points")
    return data


# def create_bar_chart(data):
#     df = pd.DataFrame(data, columns=['Timestamp', 'Latency'])
#     df.set_index('Timestamp', inplace=True)  # Set the index to the Timestamp column

#     # Ensure that the index is a DatetimeIndex
#     if not isinstance(df.index, pd.DatetimeIndex):
#         df.index = pd.to_datetime(df.index)

#     hourly_avg = df.resample('H').mean()  # Resample and calculate the average

#     # Plotting
#     hourly_avg.plot(kind='bar', figsize=(12, 6))
#     plt.title('Average API Latency Per Hour')
#     plt.xlabel('Hour')
#     plt.ylabel('Average Latency (ms)')
#     plt.show()
