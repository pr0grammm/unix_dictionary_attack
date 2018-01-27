# unix_dictionary_attack
Unix dictionary attack to crack MD5 and SHA512 hashes.
The tool can only crack passwords formed by characters in the UTF-8 character list.
The script scans a shadow file and cracks unix passwords by comparing the passwords 
to hashes of words in a user-provided wordlist. 

### Usage
```sudo python3 crack.py path_to_shadow_file path_to_wordlist```
