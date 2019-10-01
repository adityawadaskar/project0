import os

AB_TEMPLATE = "ab -t 10 -c %d -n 400000 %swww.adityawadaskar.github.io/"
request_type = ["https://", "http://"]
concurrencies = [1, 2, 4, 8, 16, 32, 64, 128, 256]
samples = 10

for r in request_type:
    for c in concurrencies:
        n = 0
        for i in range(samples):
            cmd = AB_TEMPLATE % (c, r)
            response = os.popen(cmd).read()
            lines = response.split('\n')
            for line in lines:
                words = line.split()
                if len(words) > 2:
                    if words[0] == 'Complete' and words[1] == 'requests:':
                        n += int(words[2])

        avg = n / float(samples)
        statement = "Request: %s | Concurrency: %d | Avg Requests: %f" % (r, c, avg)
        print statement
        print "--------------------------------"
