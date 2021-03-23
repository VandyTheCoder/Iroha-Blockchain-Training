1. Run Command ```docker-compose up -d``` - for starting up docker-compose.
2. Run Command ```docker ps``` - for getting list up-running container.
3. Select One of Iroha Node and Get Its' Container ID.
4. Run Command ```docker exec -it <container id> bash```.
5. After get in node Run Command ```iroha-cli -account_name root@sorakh``` - for login as root account.
6. Then add asset quantity for root and transfer to bob's account.
7. Run Command iroha-cli -account_name bob@sorakh.
8. Add Alice's signature(public key) to bob.
9. Grant permission(can_transfer) to alice.
10. Then Alice can transfer re-present as bob.
