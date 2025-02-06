# DNS FLooding Test

## Prerequisites
This test requires a DNS server to be running on the target machine. The firewall configuration must allow traffic on the DNS port.

## Configuration
To set up a DNS server on the target machine, ensure that `dnsmasq` is enabled and correctly configured.

Here is an example configuration to be added to `netvm.nix`:

```nix
# Enable and configure dnsmasq
services.dnsmasq = {
  enable = true;
  settings = {
    bogus-priv = true;
    domain-needed = true;
    interface = "wlp0s5f0";
    listen-address = [ "0.0.0.0" ];
    port = 1053;
  };
};
```

Ensure that your firewall settings allow incoming traffic on port `1053` for proper functionality.