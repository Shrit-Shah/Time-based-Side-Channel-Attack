# Time based Side-Channel Attack
## Usage
To run the script, simply execute:
```bash
python timing_attack.py
```
## Algorithm

The script employs the following algorithm:

1. A target password (`stored_pwd`) is set, and an empty string (`temp`) is initialized to store the guessed password.
2. For each position in the password (from right to left), the script performs the following steps:
   - It creates a dictionary (`result`) to store the timing results for each candidate character.
   - For each lowercase letter in the alphabet, the script:
     - Constructs a potential password by appending the current guessed character to a string of 'a' characters.
     - Measures the time it takes to verify the password using the `verify_password` function.
     - Records the elapsed time for each verification attempt.
   - Calculates the median time from the recorded timings for each character.
   - Selects the character with the maximum median time as the guessed character for that position.
   - Updates the temporary guessed password (`temp`) with the guessed character.
3. The final guessed password is printed.

## Notes
- The timing differences in password verification are used to make educated guesses character by character.
- The script assumes a simple password and may require adjustments for more complex passwords.
- This demonstration is for educational purposes and emphasizes the vulnerability of timing-based attacks.
## Disclaimer
This script is intended for educational purposes only and should not be used for malicious activities. It highlights a potential security risk and encourages understanding the importance of secure password verification mechanisms.
