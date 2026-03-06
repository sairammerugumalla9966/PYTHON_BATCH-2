logs = [
    "INFO User logged in",
    "ERROR Database failed",
    "INFO Payment successful",
    "WARNING Low balance",
    "ERROR Timeout occurred"
]

log_count = {}
unique_levels = set()

for entry in logs:
    level = entry.split()[0]
    unique_levels.add(level)

    if level in log_count:
        log_count[level] += 1
    else:
        log_count[level] = 1

print("Log Counts:", log_count)
print("Unique Log Levels:", unique_levels)



'''
Log Counts: {'INFO': 2, 'ERROR': 2, 'WARNING': 1}
Unique Log Levels: {'INFO', 'ERROR', 'WARNING'}

'''