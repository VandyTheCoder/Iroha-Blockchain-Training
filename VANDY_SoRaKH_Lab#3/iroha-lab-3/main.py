from iroha import Iroha, IrohaCrypto, IrohaGrpc

# Avialable Users
root_account = "root@sorakh"
root_private_key = "f101537e319568c765b2cc89698325604991dca57b9716b58016b253506cab70"
root_public_key = "313a07e6384776ed95447710d15e59148473ccfc052a681317a72a69f2a49910"

bob_account = "bob@sorakh"
bob_private_key = "14266dfe9f3905a014cb2ed7c251eebf8ff88651a17584be8acfde25281a7d67"
bob_public_key = "0801713ce823ad9d25245f14c90873c3863dee84dd70bf2ec8edf0a99cb1cbd5"

alice_account = "alice@sorakh"
alice_private_key = "ca65c781d9cf93632576c90d3323956cc2a05f75521511418c3d84f468b2aa38"
alice_public_key = "8892e1667a9b779e3a554296a9bfafcc8e800ec16c7d48512c74e851677d4a70"

# Avialable Assets
usd_asset = "usd#sorakh"
khr_asset = "khr#sorakh"

# Initialize Iroha Network Connection
network = IrohaGrpc("127.0.0.1:50052")

# Get Asset Information
def get_asset_info(account_id):
    iroha = Iroha(root_account)
    query = iroha.query("GetAccountAssets", account_id = account_id)
    IrohaCrypto.sign_query(query, root_private_key)
    response = network.send_query(query)
    return response

# Transfer Asset
def transfer_asset(initializer, private_key, sender, receiver, currency, amount):
    iroha = Iroha(initializer)
    command = iroha.transaction(
        [
            iroha.command(
                'TransferAsset',
                src_account_id = sender,
                dest_account_id = receiver,
                asset_id = currency,
                amount = amount
            )
        ]
    )
    IrohaCrypto.sign_transaction(command, private_key)
    network.send_tx(command)

# TEST: ===============================================================

# Get Asset Information: Account[BOB]
# print(get_asset_info(bob_account))

# Transfer Asset: Sender[BOB], Receiver[ROOT]
# transfer_asset(
#     initializer = bob_account,
#     private_key = bob_private_key,
#     sender = bob_account,
#     receiver = root_account,
#     currency = usd_asset,
#     amount = "10"
# )