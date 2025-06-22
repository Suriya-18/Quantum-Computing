def xor_bits(a, b):
    return [x ^ y for x, y in zip(a, b)]

alice_key = [random.randint(0, 1) for _ in range(8)]
trusted_node_key = [random.randint(0, 1) for _ in range(8)]
encrypted_key = xor_bits(alice_key, trusted_node_key)
received_key = xor_bits(encrypted_key, trusted_node_key)

print("Alice's Key: ", alice_key)
print("Encrypted:   ", encrypted_key)
print("Received:    ", received_key)
