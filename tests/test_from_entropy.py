#!/usr/bin/env python3

from eth_wallet.wallet import Wallet

import pytest


ENTROPY = "50f002376c81c96e430b48f1fe71df57"
PASSPHRASE = "meherett"
LANGUAGE = "french"


def test_from_entropy():

    wallet = Wallet()
    wallet.from_entropy(entropy=ENTROPY, passphrase=PASSPHRASE, language=LANGUAGE)

    wallet.from_path("m/44'/60'/0'/0/0'")

    assert wallet.entropy() == "50f002376c81c96e430b48f1fe71df57"
    assert wallet.mnemonic() == \
        "éluder incendie libre sécréter beurre persil amovible fleur tuteur unique gyrostat ouragan"
    assert wallet.language() == "french"
    assert wallet.passphrase() == "meherett"
    assert wallet.seed() == "bd421c81fbbb1cea7910851857817ac18f1fce9b9577a3e732ad28ae8ba4e097b072c48e694e5053df5db" \
                            "8a86d5cbacbbfee02b42d12c554d06313a0dadacf6b"
    assert wallet.private_key() == "656905e908b7349a8a894dda3fe1d1792a5d3484a29175e318caa8bd8dbfb10e"
    assert wallet.public_key() == "03d9ce6ac4d32b2b711016d4eddf3c28c2169e2f5a393a59569f9232ce21ec2fdf"
    assert wallet.uncompressed() == \
        "d9ce6ac4d32b2b711016d4eddf3c28c2169e2f5a393a59569f9232ce21ec2fdf621eb61a050b753b6fb775e4a319aa15682df03d3" \
        "93ac3dc798c03f68a977355"
    assert wallet.compressed() == "03d9ce6ac4d32b2b711016d4eddf3c28c2169e2f5a393a59569f9232ce21ec2fdf"
    assert wallet.wallet_import_format() == "Kzcqd9d9jTzbeh7bNSjGkqQhNNFXnPT7gWopsLSuYbP3MEUAwwJC"
    assert wallet.finger_print() == "f91947eb"
    assert wallet.chain_code() == "d7b70a1271342a03662b93112c388662b7e96714913c358e0dd3db57702259ef"
    assert wallet.path() == "m/44'/60'/0'/0/0'"
    assert wallet.address() == "0x9A610e8A2B40d010C9804451742233E182052851"

    assert wallet.extended_key(private_key=True, encoded=False) == \
        "0488ade40589afb94b80000000d7b70a1271342a03662b93112c388662b7e96714913c358e0dd3db57702259ef00656905e908b73" \
        "49a8a894dda3fe1d1792a5d3484a29175e318caa8bd8dbfb10e"
    assert wallet.extended_key(private_key=False, encoded=False) == \
        "0488b21e0589afb94b80000000d7b70a1271342a03662b93112c388662b7e96714913c358e0dd3db57702259ef03d9ce6ac4d32b2" \
        "b711016d4eddf3c28c2169e2f5a393a59569f9232ce21ec2fdf"
    assert wallet.extended_key(private_key=True, encoded=True) == \
        "xprvA3SPJ3k2vNjT7Fa3V6dg8vEieXud4ARAhLwFd4GM6i4TxsjADB4wrm2AzhcYjc5nSEkXB9EX4kuGeZS4v9Ut2PNpZdAR9zKvqiBFA" \
        "sqGrqv"
    assert wallet.extended_key(private_key=False, encoded=True) == \
        "xpub6GRjhZGvkkHkKjeWb8AgW4BTCZk7Td924ZrrRSfxf3bSqg4JkiPCQZLer1UKXzncTRrVvy5Lpc9SQNjJPqjoiMLRjqzPnYiAnbXx212kVLC"

    assert wallet.dumps() == {
        "entropy": "50f002376c81c96e430b48f1fe71df57",
        "mnemonic": "éluder incendie libre sécréter beurre persil amovible fleur tuteur unique gyrostat ouragan",
        "language": "french",
        "passphrase": "meherett",
        "seed": "bd421c81fbbb1cea7910851857817ac18f1fce9b9577a3e732ad28ae8ba4e097b072c48e694e5053df5db8a86d5cbacbbfee02b42d12c554d06313a0dadacf6b",
        "root_private_key": "5464f216361795edff8cdde60381fb52d9dc2b67a5fa1307caadb5ef5a041df192d4e95bbb37efcfad579f3319ab685b4aae0a448eddde606e6d3b0f0c6d5f57",
        "root_public_key": "8458cbbf8183c95f480b5b2d06f7faa9993e946e2bb9e55f9d7a033bbc8bcbeaeae6bab68b074725ca4efdcbc0986de0384f192cae4c6184fe1f3c4523252824",
        "uncompressed": "d9ce6ac4d32b2b711016d4eddf3c28c2169e2f5a393a59569f9232ce21ec2fdf621eb61a050b753b6fb775e4a319aa15682df03d393ac3dc798c03f68a977355",
        "compressed": "03d9ce6ac4d32b2b711016d4eddf3c28c2169e2f5a393a59569f9232ce21ec2fdf",
        "chain_code": "d7b70a1271342a03662b93112c388662b7e96714913c358e0dd3db57702259ef",
        "private_key": "656905e908b7349a8a894dda3fe1d1792a5d3484a29175e318caa8bd8dbfb10e",
        "public_key": "03d9ce6ac4d32b2b711016d4eddf3c28c2169e2f5a393a59569f9232ce21ec2fdf",
        "wif": "Kzcqd9d9jTzbeh7bNSjGkqQhNNFXnPT7gWopsLSuYbP3MEUAwwJC",
        "finger_print": "f91947eb",
        "path": "m/44'/60'/0'/0/0'",
        "address": "0x9A610e8A2B40d010C9804451742233E182052851",
        "serialized": {
            "private_key_hex": "0488ade40589afb94b80000000d7b70a1271342a03662b93112c388662b7e96714913c358e0dd3db57702259ef00656905e908b7349a8a894dda3fe1d1792a5d3484a29175e318caa8bd8dbfb10e",
            "public_key_hex": "0488b21e0589afb94b80000000d7b70a1271342a03662b93112c388662b7e96714913c358e0dd3db57702259ef03d9ce6ac4d32b2b711016d4eddf3c28c2169e2f5a393a59569f9232ce21ec2fdf",
            "private_key_base58": "xprvA3SPJ3k2vNjT7Fa3V6dg8vEieXud4ARAhLwFd4GM6i4TxsjADB4wrm2AzhcYjc5nSEkXB9EX4kuGeZS4v9Ut2PNpZdAR9zKvqiBFAsqGrqv",
            "public_key_base58": "xpub6GRjhZGvkkHkKjeWb8AgW4BTCZk7Td924ZrrRSfxf3bSqg4JkiPCQZLer1UKXzncTRrVvy5Lpc9SQNjJPqjoiMLRjqzPnYiAnbXx212kVLC"
        }
    }

    with pytest.raises(ValueError, match=r"Invalid language, .*"):
        wallet.from_entropy(entropy=ENTROPY, passphrase=PASSPHRASE, language=None)
