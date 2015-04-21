#!/bin/bash
#http://fosshelp.blogspot.in/2015/04/cannot-verify-rawgithubcoms-certificate.html

cd /etc/ssl/certs

#Download DigiCert Root Certificate "DigiCert High Assurance EV Root CA" from 
#following site.
sudo wget https://www.digicert.com/CACerts/DigiCertHighAssuranceEVRootCA.crt --no-check-certificate

#Unfortunately these are encoded and need to be converted into text.
sudo openssl x509 -inform DES -in DigiCertHighAssuranceEVRootCA.crt -out DigiCertHighAssuranceEVRootCA.crt -text

#The final step is running c_rehash within "/etc/ssl/certs" to scan directories
#and take a hash value of each '.pem' and '.crt' file in the directory. It then
#creates symbolic links for each of the files named by the hash value. Programs
#on the system (like curl or wget) expect to find the certificates they require
#in this c_rehash'ed format. 
sudo c_rehash .

