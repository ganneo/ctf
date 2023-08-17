# keygenme-py Writeup

[keygenme-trial.py](https://mercury.picoctf.net/static/5a4198cd84f87c8a597cbd903d92fbf4/keygenme-trial.py)

After downloading the Fernet package and playing around with the program, I noticed that the enter license key option was most likely asking for the flag. Looking at the code I noticed that at the top we get the first half of the key: `picoCTF{1n_7h3_|<3y_of_`. Below in the `check_key` function we can see how the key that was inputted was validated. The code can be broken into 3 parts where the 1st and 2nd parts are checking to see if the length and static base of the key is the same with the `key_full_template_trial` variable. What we are really interested in are the `if` statements after that.

In the `if` statements we are comparing the key and a encrypted version of the `username_trail` variable. Tracking it back to where it was initiated I found out that it was just a binary string. In my case it was `ANDERSON` however it will be different for different users. So, we can generate the key by setting each ith value to its corresponding encrypted value from the `if` statements.

Running the python program results in the key: picoCTF{1n_7h3_|<3y_of_01582419}

Link to [code](../src/main/python/keygenme.py)