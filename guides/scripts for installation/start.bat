powershell -Command Set-ExecutionPolicy RemoteSigned
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
wsl --set-default-version 2
bash ./ubuntu.sh
mstsc /v:localhost:3390
