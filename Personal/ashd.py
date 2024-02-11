from math import ceil

size_tb = 45.1
disk_size_gb = 2000
rpm = 15000
seek_time_ms = 6.5
io_size_kb = 128
transfer_rate_mbs = 89
app_iops = 8947

dc = (size_tb * 1024) / disk_size_gb
ts = seek_time_ms / 1000 + 0.5 / (rpm / 60) + io_size_kb / (transfer_rate_mbs * 1024)
s = 0.7 * (1 / ts)
dp = app_iops / s
max = max(dp, dc)

print(ceil(max))
