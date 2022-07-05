from parsezeeklogs import ParseZeekLogs
import elasticsearch

filename = "/home/jaketay/Research/IoTScenarios/CTU-IoT-Malware-Capture-9-1/bro/conn.log.labeled"

# with open(filename , 'r') as f:
#     first_line = f.readline()
#     for line in f:
#         print(first_line)
#         first_line = f.readline()

log_iterator = ParseZeekLogs(filename, output_format="csv", safe_headers=False)
# Print the field line out
print(log_iterator.get_fields())

N = 100000
runCheck = 1

with open('../../Research/data/IoTScenarios/out_91.csv',"w") as outfile:
    for log_record in ParseZeekLogs(filename, output_format="csv", safe_headers=False, fields=["ts","id.orig_h","id.resp_h","tunnel_parents   label   detailed-label"]):
        if log_record is not None:
            #print(log_record)
            outfile.write(log_record + "\n")
            if N <= 0:
                print("Running X" + str(runCheck))
                runCheck += 1
                N = 100000
            N -= 1