# HTTP Flooding Test

## Prerequisites
This test requires an HTTP server to be running on the target machine. The firewall configuration must allow traffic on the HTTP port.

To start a simple HTTP server for testing, run the following command on the target machine:

```sh
python3 -m http.server 8000 --bind 0.0.0.0
```

This will start a basic HTTP server on port **8000**, listening on all network interfaces (`0.0.0.0`). Ensure that the port is accessible from the network before proceeding with the test.