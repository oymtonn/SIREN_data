import serial

PORT = "/dev/cu.usbserial-140"
BAUD = 9600

output_file = "slave_data.csv"

with serial.Serial(PORT, BAUD, timeout=1) as ser, open(output_file, "a", buffering=1) as f:
    f.write("count,time_stamp,adc,sipm_voltage,deadtime,temperatureC\n")

    print(f"Logging {PORT} to {output_file}")
    print("Press Ctrl+C to stop.")

    while True:
        line = ser.readline().decode(errors="ignore").strip()

        if line:
            print(line)
            parts = line.split()

            if len(parts) == 6:
                f.write(",".join(parts) + "\n")
            else:
                f.write("# BAD LINE: " + line + "\n")