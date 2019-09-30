# CS291A: Project 0

This repository contains source code for a static webpage designed for CS291A, and analysis on average page load time and server rate limit.
Hosted at: [adityawadaskar.github.io](https://adityawadaskar.github.io)

## Website Analysis

#### On average, how many requests can ab complete in 10 seconds with various power of two concurrency levels between 1 and 256?
The below table was calculated with an average over 10 samples. The total computation time was approx. 10 samples x 10 s/sample x 9 = 900s

| Concurrency | Avg Requests in 10 seconds (HTTPS) |
| --- | --- |
| 1 | 278 |
| 2 | 561 |
| 4 | 1479 |
| 8 | 2861 |
| 16 | 5224 |
| 32 | 12069 |
| 64 | 17334 |
| 128 | 21564 |
| 256 | 23241 |

#### Why are there diminishing returns at higher concurrency levels?
At a certain point, the number of concurrent requests becomes too high and overloads the server - this can cause individual request time to increase, hence the diminishing returns.

#### What’s the difference when requesting HTTP and HTTPS?
The response for HTTP requests is approximately 2x faster than for HTTPS requests. This is likely because HTTPS has 2 round trips of communication when setting up the TLS handshake as opposed to HTTP's single round trip, hence doubling the time. Below are the results:

| Concurrency | Avg Requests in 10 seconds (HTTP) |
| --- | --- |
| 1 | 735 |
| 2 | 1242 |
| 4 | 3472 |
| 8 | 5501 |
| 16 | 11029 |
| 32 | 25916 |
| 64 | 45627 |
| 128 | 61406 |
| 256 | 86036 |

#### How can github respond so quickly?
Like most big websites, GitHub likely has a CDN (content delivery network) - with such a distributed system, it is faster to respond to requests from a server located closer to the user. A load balancing network also means that if a server is bogged down, another server will fulfill the request. Furthermore, repeated access to a particular site can mean that GitHub likely caches the webpage.

#### What is the site’s “Time to Interactive” according to PageSpeed Insights?
1.3s
