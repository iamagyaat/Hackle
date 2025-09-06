import base64
import argparse

def encode_double(data: str) -> str:
    """
    Encode plain text into Base64, then Hex (string representation).
    """
    b64_encoded = base64.b64encode(data.encode())  # -> bytes
    hex_encoded = b64_encoded.hex()                # hex string
    return hex_encoded

def decode_double(encoded_data: str):
    """
    Decode Hex into Base64 bytes, then Base64 into plain text (if possible).
    If result is not valid UTF-8, return it as hex.
    """
    b64_bytes = bytes.fromhex(encoded_data)        # raw Base64 bytes
    raw_bytes = base64.b64decode(b64_bytes)        # decode base64

    try:
        # Try to return as text
        return raw_bytes.decode("utf-8")
    except UnicodeDecodeError:
        # If not valid UTF-8, return as hex string
        return raw_bytes.hex()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Double Encode/Decode (Base64 + Hex)")
    parser.add_argument("mode", choices=["encode", "decode"], help="Choose encode or decode")
    parser.add_argument("text", help="Text to encode/decode")

    args = parser.parse_args()

    if args.mode == "encode":
        result = encode_double(args.text)
        print(f"Encoded: {result}")
    else:
        result = decode_double(args.text)
        print(f"Decoded: {result}")
