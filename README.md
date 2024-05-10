# GET DISCORD DEVELOPER BADGE

### Follow the below steps to get your discord developer badge for free


Make sure you have python installed. check it by running this command in command prompt, terminal.
```bash
python --version # Windows

python3 --version # Mac or Linux
```
output should be something like this
```bash
$ python --version
Python 3.12.3 # python version can be different for you
```

1. Go to [discord developer portal](https://discord.com/developers) and click on create new application.
   
     ![image](https://github.com/MannuVilasara/get-discord-developer-badge/assets/117009138/57cab251-4b66-4714-b391-d2bdc7825c7e)

2. Name it whatever u want, click on checkbox and click create.

    ![image](https://github.com/MannuVilasara/get-discord-developer-badge/assets/117009138/a4d8a466-4276-4cbf-bea6-3e42f97f6ce6)
    > some names get blocked like `discord` so make sure to not include word discord in the name
3. On the left side, click on Bot option to open Bot panel.

      ![image](https://github.com/MannuVilasara/get-discord-developer-badge/assets/117009138/64a90284-c3aa-4b94-a6cb-4a4f7f91e5da)

4. Enable these three options and click on Save Changes.

     ![image](https://github.com/MannuVilasara/get-discord-developer-badge/assets/117009138/ab5b8aed-5062-4ca5-8b74-79dd4896a32f)

5. Click on the reset token button to get a new token.

     ![image](https://github.com/MannuVilasara/get-discord-developer-badge/assets/117009138/4eb36726-004e-4e70-bc24-0d75d3443c9e)

6. Click on copy option to copy the token.

    ![image](https://github.com/MannuVilasara/get-discord-developer-badge/assets/117009138/2a076d41-32a0-4d41-a41e-aab9ca272eb4)

7. clone this repo locally using `https://github.com/MannuVilasara/get-discord-developer-badge` or Download the source code as zip.

     ![image](https://github.com/MannuVilasara/get-discord-developer-badge/assets/117009138/5f886ffb-ddc9-40d4-8343-9897467585fd)

8. You should see these files. open the config.py file with any text editor.

   ```bash
   .
   ├── config.py
   ├─ .gitignore
   ├── LICENSE
   ├── main.py
   ├── README.md
   └── requirements.txt
   ```

9. Replace `ENTER YOUR TOKEN HERE` with the token you copied in step 6. make sure to keep the token in quotues

    ![image](https://github.com/MannuVilasara/get-discord-developer-badge/assets/117009138/f183a57f-7287-4991-819c-8b7755659e01)


10. run the following commands.
    ```bash
    pip install -r requirements.txt
    ```
    ```bash
    python main.py # windows

    python3 main.py # mac or linux
    ```
11. You will see the link in your terminal. Click on that link to invite the bot in any server. Create a new server if you don't have one.

12. run the `/badge` command in server after inviting the bot and wait for 24 hours. click on the link provided by the bot to claim your `active-developer-badge`



