# SedonaNet

## Current Services 
- Portainer CE
- Nginx Proxy Manager
- Adguard Home
- Vaultwarden
- S3 Backup Manager

## Initial Server Setup

Scripts are located in the `scripts` directory.

Before running any script, you will need to run the below command
```
[sudo] chmod u+x <<SCRIPT_NAME>>
```

SedonaNet requires the scripts to be run in this order:
1. `docker_setup.sh`
2. `portainer_setup.sh`

All other Docker-based applications can be managed through Portainer.

## Documentation

Documentation can be found in this [repo's wiki](https://github.com/kammetherell/sedonanet/wiki).