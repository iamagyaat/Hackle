import base64
import json
import sys
import jwt
from jwcrypto import jwk, jwe
from datetime import datetime

def b64url_decode(data):
    """Fix padding and decode base64url strings"""
    data += "=" * ((4 - len(data) % 4) % 4)
    return base64.urlsafe_b64decode(data.encode())

def analyze_token(token, public_key=None, private_key=None):
    parts = token.split(".")
    print("="*60)
    print("[*] Token Analysis Report")
    print("="*60)

    # JWS should have 3 parts, JWE should have 5
    if len(parts) == 3:
        print("[+] Detected: JWS (Signed JWT)")
        header = json.loads(b64url_decode(parts[0]))
        payload = json.loads(b64url_decode(parts[1]))
        signature = parts[2]

        print("\n--- Header ---")
        print(json.dumps(header, indent=4))
        print("\n--- Payload ---")
        print(json.dumps(payload, indent=4))

        # Check weaknesses
        if header.get("alg") == "none":
            print("[!] Weakness: 'alg' is set to 'none'. Token can be forged easily.")
        if header.get("alg") == "HS256" and public_key:
            print("[!] Warning: HS256 with a public key may allow key confusion attacks.")

        if "exp" in payload:
            exp = datetime.utcfromtimestamp(payload["exp"])
            print(f"[*] Token Expiry: {exp}")
            if (exp - datetime.utcnow()).days > 7:
                print("[!] Weakness: Token expiration is very long (greater than 7 days).")

        required_claims = ["iss", "aud", "iat"]
        for claim in required_claims:
            if claim not in payload:
                print(f"[!] Missing claim: {claim}")

        if "kid" in header:
            print("[!] Header includes 'kid'. Check for potential injection attacks.")

        # Verify signature if public key provided
        if public_key:
            try:
                decoded = jwt.decode(token, public_key, algorithms=[header["alg"]])
                print("[+] Signature verified successfully with provided public key.")
            except Exception as e:
                print(f"[!] Signature verification failed: {str(e)}")

    elif len(parts) == 5:
        print("[+] Detected: JWE (Encrypted JWT)")
        if private_key:
            try:
                key = jwk.JWK.from_pem(private_key.encode("utf-8"))
                jwetoken = jwe.JWE()
                jwetoken.deserialize(token, key=key)
                print("[+] Decryption successful!")
                print("\n--- Decrypted Payload ---")
                print(jwetoken.payload.decode("utf-8"))
            except Exception as e:
                print(f"[!] Failed to decrypt: {str(e)}")
        else:
            print("[!] Private key required for decryption but not provided.")

    else:
        print("[!] Not a valid JWT format (not 3 or 5 parts). Might not be JWT at all.")

    print("="*60)

# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <token> [public_key.pem] [private_key.pem]")
        sys.exit(1)

    token = sys.argv[1]
    public_key = None
    private_key = None

    if len(sys.argv) >= 3:
        with open(sys.argv[2], "r") as f:
            public_key = f.read()
    if len(sys.argv) >= 4:
        with open(sys.argv[3], "r") as f:
            private_key = f.read()

    analyze_token(token, public_key, private_key)
