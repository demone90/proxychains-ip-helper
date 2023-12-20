## Why do you need this repo?
Bored to always copy and paste a bunch of IP addresses with port and protocol in your local /etc/proxychains.conf file.
Then I got you here. Use this simple python helper to copy IP addresses from a text file (downloaded via the web) and append them
into your config file to start proxychaining like a pro (addresses are appended at the end of the file)

## How to run the helper?
Since the end goal is to update the system's /etc/proxychains.conf file the command needs sudo permissions to work.

```
sudo python3 proxychains-ip-helper.py

```
The script will request for which protocol (http, socks4 or socks5) the entries will be included AND a path to the txt file with the proxie's IP addresses


## Proxies IP addresses

Finding free proxies IP addresses is possible but use them with caution. If something is free it should always ring a bell. Use them monstly for learning purposes in ethical hacking and
never to harm someone or something without permissions.

## Tools used

- ChatGPT to write down the initial code structure
- https://github.com/TheSpeedX/PROXY-List to look up proxies IP addresses (updated each hour)
- https://hidemy.io/en/proxy-list/ to generate the actual txt file with active and usable IPs
- Kali Linux to test it

## WIP
Auto generation of a txt file with valid IP addresses to use

## Feedback
Let me know what do you think and how we could improve the script to even make a better job
